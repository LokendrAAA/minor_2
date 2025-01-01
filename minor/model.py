# File: test_model.py

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the fine-tuned model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("./fine_tuned_codebert")
tokenizer = AutoTokenizer.from_pretrained("./fine_tuned_codebert")

# Sample C++ code for testing (replace this with new C++ samples)
sample_code = "int main() {  std::cout << 'Hello, World!'; return 0; }"

# Tokenize the sample code
inputs = tokenizer(sample_code, return_tensors="pt", truncation=True, padding=True, max_length=512)

# Perform inference
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_label = torch.argmax(logits, dim=1).item()

# Output prediction result
if predicted_label == 0:
    print("Prediction: Human-Written Code")
else:
    print("Prediction: AI-Generated Code")
