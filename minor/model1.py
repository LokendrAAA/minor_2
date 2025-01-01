from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

app = Flask(__name__)
CORS(app)

# Load fine-tuned model and tokenizer
model_dir = "./fine_tuned_codebert"  # Replace with your actual model directory path
tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForSequenceClassification.from_pretrained(model_dir)
model.eval()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_code', methods=['POST'])
def check_code():
    data = request.json
    code = data.get('code', '')

    # Tokenize and predict
    inputs = tokenizer(code, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_label = torch.argmax(logits, dim=1).item()

    # Interpret prediction result
    result = "Human-Written Code" if predicted_label == 0 else "AI-Generated Code"
    
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
