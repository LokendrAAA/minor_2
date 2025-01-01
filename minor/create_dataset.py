# File: create_dataset.py

import pandas as pd
from data_loader import load_cpp_files_from_folder  # Importing the file loading function

# Assuming you have AI-generated code samples in this file
from data.ai_generated_code_samples import ai_generated_codes  # Import your AI-generated samples

# Load human-written C++ samples from a folder
folder_path = "D:\\phy 1\\Project_CodeNet_C++1000.tar\\Project_CodeNet_C++1000\\p00004"
  # Replace with the path to your C++ files folder
human_cpp_files = load_cpp_files_from_folder(folder_path)

# Convert human C++ files to DataFrame
human_df = pd.DataFrame(human_cpp_files)
human_df['label'] = 0  # Label 0 for human-written code

# Convert AI-generated samples to DataFrame
ai_df = pd.DataFrame(ai_generated_codes)
ai_df['label'] = 1  # Label 1 for AI-generated code

# Combine both datasets
combined_df = pd.concat([human_df, ai_df], ignore_index=True)

# Save the combined dataset (optional)
combined_df.to_csv("combined_code_dataset.csv", index=False)
