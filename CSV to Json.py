import pandas as pd
import json
from sklearn.model_selection import train_test_split

file = './Symptom2Disease.csv'
df = pd.read_csv(file)

# Perform a stratified train-test split based on the label column
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42, stratify=df['label'])

# Function to save a DataFrame to a JSONL file in the chat format
def save_to_jsonl_format(dataframe, output_file):
    with open(output_file, 'w') as outfile:
        for index, row in dataframe.iterrows():
            # Create the chat format dictionary
            chat_data = {
                "messages": [
                    {"role": "user", "content": f"Symptoms: {row['text']}"},
                    {"role": "assistant", "content": f"Disease: {row['label']}"}
                ]
            }
            # Write the dictionary as a JSON string
            outfile.write(json.dumps(chat_data) + '\n')

# Save the training and testing sets to separate JSONL files
save_to_jsonl_format(train_df, 'train_data_chat.jsonl')
save_to_jsonl_format(test_df, 'test_data_chat.jsonl')
