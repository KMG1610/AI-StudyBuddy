import google.generativeai as genai
import gradio as gr
import os
import pypdf
import docx
import time

# Configuration
try:
    API_KEY = os.environ.get("GEMINI_API_KEY")
    genai.configure(api_key=API_KEY)
    
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    selected_model_name = next((m for m in available_models if 'flash' in m), available_models[0])
    model = genai.GenerativeModel(selected_model_name)
except Exception:
    model = None 

# Backend Logic
def extract_text_from_file(file_path):
    text = ""
    try:
        if not file_path: return ""
        # Hugging Face passes file path as string
        filename = file_path.lower()
        if filename.endswith('.pdf'):
            reader = pypdf.PdfReader(file_path)
            for page in reader.pages: text += page.extract_text() + "\n"
        elif filename.endswith('.docx'):
            doc = docx.Document(file_path)
            for para in doc.paragraphs: text += para.text + "\n"
        elif filename.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as f: text = f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"
    return text

def study_buddy_logic(text_input, file_inputs, mode, progress=gr.Progress()):
    yield "⏳ Connecting...", "", gr.update(visible=True)
    time.sleep(0.4)

    if model is None: 
        yield "❌ Error: API Key missing. Check Settings > Secrets.", "", gr.update()
        return

    progress(0.1, desc="System check...")
    
    combined_text = text_input
    if file_inputs:
        total = len(file_inputs)
        for idx, f in enumerate(file_inputs):
            progress(0.2 + (0.2 * (idx/total)), desc=f"Scanning File {idx+1}...")
            time.sleep(0.2)
            ext = extract_text_from_file(f)
            if ext.startswith("Error"): 
                yield f"⚠️ File Error: {ext}", "", gr.update()
                return
            combined_text += f"\n\n--- FILE {idx+1} ---\n{ext}"

    if not combined_text.strip(): 
        yield "⚠️ Waiting for content...", "", gr.update()
        return

    progress(0.5, desc="Analyzing data...")
    time.sleep(0.3)
    
    prompts = {
        "Explain Concept": f"Act as an expert tutor. Explain this simply:\n\n{combined_text}",
        "Summarize Notes": f"Summarize into bullet points:\n\n{combined_text}",
        "Generate Quiz": f"Create 5 multiple choice questions with answers at the end:\n\n{combined_text}",
        "Create Flashcards": f"Create 5 Q&A flashcards:\n\n{combined_text}"
    }

    try:
        progress(0.6, desc="Generating...")
        yield "🧠 Thinking...", "", gr.update()
        
        response_stream = model.generate_content(prompts[mode], stream=True)
        partial_text = ""
        for chunk in response_stream:
            partial_text += chunk.text
            yield partial_text, partial_text, gr.update()
            
    except Exception as e:
        yield f"❌ API Error: {str(e)}", "", gr.update()

def clear_all():
    return None, None, "", ""

# CSS Styling
custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700;800&display=swap');

.gradio-container {
    font-family: 'Outfit', sans-serif !important;
    background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%) !important;
}

#input-card, #output-card {
    background: rgba(255, 255, 255, 0.98) !important;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 20px 40px -5px rgba(0, 0, 0, 0.3) !important;
    border: 1px solid rgba(255, 255, 255, 0.5);
}

.custom-header {
    color: #000000 !important;
    font-size: 1.6rem !important;
    font-weight: 800 !important;
    margin-bottom: 5px !important;
    margin-top: 0px !important;
    line-height: 1.2 !important;
}

#output-card .prose, #output-card .prose * {
    color: #000000 !important;
    font-size: 1rem !important;
    opacity: 1 !important;
}

.upload-container span { color: #475569 !important; }
.file-name { color: #ffffff !important; font-weight: 600 !important; }
.upload-container { min-height: 120px !important; margin-top: 0px !important; }

button.primary {
    background: #4c1d95 !important; 
    color: #ffffff !important;
    font-weight: 700 !important;
    border: none !important;
}
button.primary:hover {
    background: #7c3aed !important; 
    transform: translateY(-2px);
}
#clear-btn, #copy-btn {
    background: #4c1d95 !important;
    color: white !important;
}

.header-container {
    background: white;
    padding: 15px;
    border-radius: 16px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    display: flex; align-items: center; justify-content: center;
    gap: 15px; margin-bottom: 25px;
}
.logo-box {
    width: 50px; height: 50px;
    background: linear-gradient(135deg, #4f46e5, #9333ea);
    border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
    font-size: 26px; color: white !important;
}
.badge {
    background: #4f46e5; color: white !important;
    font-size: 0.8rem; padding: 4px 10px; border-radius: 8px;
    font-weight: 700; vertical-align: middle; margin-left: 10px;
}
#copy-btn-row { display: flex; justify-content: flex-end; align-items: center; margin-bottom: 5px; }
"""

copy_js = """(x) => { navigator.clipboard.writeText(x); return "✅ Copied!"; }"""

theme = gr.themes.Soft(primary_hue="violet", neutral_hue="slate")

# App Layout
with gr.Blocks(theme=theme, css=custom_css, title="AI Study Buddy PRO") as app:
    
    gr.HTML("""
        <div class="header-container">
            <div class="logo-box">🚀</div>
            <div>
                <h1 style="margin:0; font-size:1.8rem; font-weight:800; color:#1f2937;">AI Study Buddy <span class="badge">PRO</span></h1>
                <p style="margin:0; color:#6b7280; font-size:0.95rem;">Advanced Academic Assistant</p>
            </div>
        </div>
    """)
    
    with gr.Row():
        # Left Column
        with gr.Column(elem_id="input-card"):
            gr.HTML('<h3 class="custom-header">📥 Input Data</h3>')
            
            file_upload = gr.File(
                label="", 
                file_types=[".pdf", ".docx", ".txt"],
                file_count="multiple",
                height=140
            )
            
            text_input = gr.Textbox(
                lines=4, 
                label="", 
                placeholder="Or paste your lecture notes here..."
            )
            
            gr.HTML('<h3 class="custom-header" style="margin-top: 15px !important;">⚙️ Modes</h3>')
            
            mode_selector = gr.Radio(
                ["Explain Concept", "Summarize Notes", "Generate Quiz", "Create Flashcards"],
                show_label=False, 
                value="Summarize Notes"
            )
            
            with gr.Row():
                clear_btn = gr.Button("🗑️ Clear", elem_id="clear-btn")
                submit_btn = gr.Button("⚡ Start Analysis", variant="primary", size="lg")

        # Right Column
        with gr.Column(elem_id="output-card"):
            with gr.Row(elem_id="copy-btn-row"):
                gr.HTML('<h3 class="custom-header" style="margin-bottom:0 !important; flex-grow:1;">💡 AI Output</h3>')
                copy_btn = gr.Button("📋 Copy", size="sm", scale=0, elem_id="copy-btn")
            
            output_display = gr.Markdown()
            hidden_buffer = gr.Textbox(visible=False)
            
            gr.HTML('<div style="text-align:right; font-size:0.8rem; color:#9ca3af; margin-top:20px;">Powered by Google Gemini</div>')

    # Interactions
    submit_btn.click(
        fn=study_buddy_logic, 
        inputs=[text_input, file_upload, mode_selector], 
        outputs=[output_display, hidden_buffer, clear_btn]
    )
    
    copy_btn.click(fn=None, inputs=[hidden_buffer], outputs=[copy_btn], js=copy_js)
    
    clear_btn.click(
        fn=clear_all,
        inputs=[],
        outputs=[file_upload, text_input, output_display, hidden_buffer]
    )

app.launch()
