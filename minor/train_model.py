# File: train_model.py

from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset
import pandas as pd

# Import the human-written and AI-generated code samples
from data.human_code_samples import human_codes
from data.ai_generated_code_samples import ai_generated_codes

# Convert the human-written and AI-generated code samples into DataFrames
human_df = pd.DataFrame(human_codes)
human_df['label'] = 0  # Label 0 for human-written code

ai_df = pd.DataFrame(ai_generated_codes)
ai_df['label'] = 1  # Label 1 for AI-generated code

# Ensure there is a 'code' column. If the column is named differently, change this line.
# Assuming your code samples are stored in a column named 'code':
human_df.rename(columns={human_df.columns[0]: "code"}, inplace=True)  # Ensure the first column is named 'code'
ai_df.rename(columns={ai_df.columns[0]: "code"}, inplace=True)  # Ensure the first column is named 'code'

# Combine the datasets
combined_df = pd.concat([human_df, ai_df], ignore_index=True)

# Load tokenizer for CodeBERT
tokenizer = AutoTokenizer.from_pretrained('microsoft/codebert-base')

# Tokenize the dataset
def tokenize_function(examples):
    return tokenizer(examples["code"], truncation=True, padding="max_length", max_length=512)

# Convert DataFrame to Hugging Face Dataset
dataset = Dataset.from_pandas(combined_df)

# Tokenize the dataset
dataset = dataset.map(tokenize_function, batched=True)

# Remove the 'code' column as it is no longer needed
dataset = dataset.remove_columns(['code'])

# Split into training and testing datasets (80% training, 20% testing)
train_test_split_ratio = 0.2
train_dataset, test_dataset = dataset.train_test_split(test_size=train_test_split_ratio).values()

# Set dataset format for PyTorch
train_dataset.set_format("torch")
test_dataset.set_format("torch")

# Load pre-trained CodeBERT for sequence classification
model = AutoModelForSequenceClassification.from_pretrained('microsoft/codebert-base', num_labels=2)

# Define training arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    num_train_epochs=3,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    logging_dir='./logs',
    logging_steps=10,
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
)

# Train the model
trainer.train()

# Save the model and tokenizer
model.save_pretrained("./fine_tuned_codebert")
tokenizer.save_pretrained("./fine_tuned_codebert")
