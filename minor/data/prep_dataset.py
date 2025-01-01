# data/prep_dataset.py

import pandas as pd
from sklearn.model_selection import train_test_split
from data.human_code_samples import human_codes
from data.ai_generated_code_samples import ai_generated_codes

def prepare_dataset():
    # Create DataFrames from both human and AI-generated code samples
    human_df = pd.DataFrame(human_codes)
    human_df['label'] = 0  # 0 for Human-Written
    
    ai_df = pd.DataFrame(ai_generated_codes)
    ai_df['label'] = 1  # 1 for AI-Generated
    
    # Combine both datasets
    df = pd.concat([human_df, ai_df], ignore_index=True)

    # Split into training and testing datasets (80% train, 20% test)
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

    return train_df, test_df

if __name__ == "__main__":
    train_df, test_df = prepare_dataset()
    print("Training set:\n", train_df.head())
    print("Test set:\n", test_df.head())
