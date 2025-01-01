# utils/preprocess.py

from transformers import AutoTokenizer

# Initialize the tokenizer (CodeBERT tokenizer)
tokenizer = AutoTokenizer.from_pretrained('microsoft/codebert-base')

def preprocess_code(code_snippet):
    """
    Tokenizes the code snippet using CodeBERT tokenizer.
    
    Args:
        code_snippet (str): The code to tokenize.
    
    Returns:
        dict: Tokenized inputs.
    """
    inputs = tokenizer(code_snippet, return_tensors="pt", truncation=True, padding=True, max_length=512)
    return inputs
