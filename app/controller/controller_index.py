from main import app
from flask import request, render_template, redirect, url_for
import google.generativeai as genai


@app.route('/')
def index():
    response = request.args.get('response')
    return render_template('index.html', response=response)

@app.route('/chat',  methods=['GET', 'POST'])
def chat():
    message = request.form.get('name')

    genai.configure(api_key="")

    # Set up the model
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"
    },
    ]

    system_instruction = "voce é um psicologo que so responde perguntas sobre e somente sobre estes temas,\nTerapia comportamental cognitiva (TCC)\nTerapia comportamental dialética (TCD)\nTerapia centrada na pessoa\nTerapia humanista\nTerapia psicodinâmica\nTerapia baseada em evidências\nPsicologia positiva\nIntervenções de estilo de vida\nTécnicas de enfrentamento\nHabilidades de regulação emocional\nValores tradicionais\nNormas sociais\nPapéis de gênero\nEstruturas familiares\nReligião e espiritualidade\n\nvoce e brasileiro e responde em portugues\nvoce e sempre conservador nas responstas \nvoce esta em um consultorio haja como se estivesse no local, e  seu paciente sao as perguntas\nseu nome e dr.gustavo"

    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                generation_config=generation_config,
                                system_instruction=system_instruction,
                                safety_settings=safety_settings)

    convo = model.start_chat(history=[
    
    ])
    print(message)
    convo.send_message(message)
    return redirect(url_for('index', response = convo.last.text))
