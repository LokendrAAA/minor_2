import pandas as pd
from data.human_check import human_written_code_samples
from data.ai_check import ai_generated_code_samples
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def create_dataframe():
    """
    Combines human-written and AI-generated code samples into a single DataFrame.
    """
    # Creating DataFrame from human and AI-generated code
    human_df = pd.DataFrame(human_written_code_samples)
    human_df['label'] = 0  # 0 for Human-Written
    
    ai_df = pd.DataFrame(ai_generated_code_samples)
    ai_df['label'] = 1  # 1 for AI-Generated
    
    combined_df = pd.concat([human_df, ai_df], ignore_index=True)
    return combined_df

def main():
    # Step 1: Create the dataset
    df = create_dataframe()
    print("Dataset Created:")
    print(df.head())
    
    # Step 2: Load the fine-tuned model
    model = AutoModelForSequenceClassification.from_pretrained("./fine_tuned_model")
    tokenizer = AutoTokenizer.from_pretrained("./fine_tuned_model")
    print("Fine-tuned Model Loaded.")
    
    # Step 3: Classify each code sample
    results = []
    for index, row in df.iterrows():
        # Assuming the first column contains the C++ code
        code = row[0]  # Get the C++ code directly from the first column
        true_label = row['label']
        inputs = tokenizer(code, return_tensors="pt", truncation=True, padding=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            prediction = torch.argmax(logits, dim=1).item()
        predicted_label = prediction
        results.append({
            "id": index,  # You can use the index as an ID if there's no specific ID column
            "true_label": true_label,
            "predicted_label": predicted_label,
            "prediction": "AI-Generated" if predicted_label == 1 else "Human-Written"
        })
        print(f"Sample {index} - Predicted: {results[-1]['prediction']}")
    
    # Step 4: Create a results DataFrame
    results_df = pd.DataFrame(results)
    
    # Step 5: Evaluate the model
    accuracy = (results_df['true_label'] == results_df['predicted_label']).mean()
    print(f"\nAccuracy: {accuracy * 100:.2f}%")
    
    # Step 6: Save the results
    results_df.to_csv("classification_results_fine_tuned.csv", index=False)
    print("Results saved to classification_results_fine_tuned.csv")
   
    conf_matrix = confusion_matrix(results_df['true_label'], results_df['predicted_label'])
    plt.figure(figsize=(10, 7))
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Human-Written', 'AI-Generated'], yticklabels=['Human-Written', 'AI-Generated'])
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.title('Confusion Matrix')
    plt.show()

if __name__ == "__main__":
    main()
