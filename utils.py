import json
import pandas as pd

# Loading the conversion dataset
def load_data(file_path='medical_chatbot_conversations.json'):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Converting to DataFrame for easy processing
def clean_data(data):
    conversations = []
    for entry in data:
        try:
            user_message = next(msg['text'] for msg in entry['messages'] if msg['role'] == 'user')
            bot_response = next(msg['text'] for msg in entry['messages'] if msg['role'] == 'bot')
            conversations.append({"user": user_message, "bot": bot_response})
        except StopIteration:
            continue
    return pd.DataFrame(conversations)

#Cleaning the data
data = load_data()
cleaned_data = clean_data(data)
print("Data Loaded and Cleaned!")
