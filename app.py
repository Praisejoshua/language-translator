import pandas as pd
from googletrans import Translator

def translate_text(input_text, target_language='fr'):
    translator = Translator()
    translated_text = translator.translate(input_text, dest=target_language)
    return translated_text.text

#creating a function to translate datarame(text to be translated), and text to be translated to (french)
def translate_dataset(df, target_language='fr'):
    df['translated_text'] = df['text'].apply(lambda x: translate_text(x, target_language))
    return df

# Load the dataset
file_path = './data/eng_-french.csv'  
your_dataframe = pd.read_csv(file_path)

# User input 
user_input = input("\nEnter the English word to be translated to French: ")

# Create a DataFrame with the user input
user_dataframe = pd.DataFrame({'text': [user_input]})

# Perform the translation
user_dataframe_translated = translate_dataset(user_dataframe, target_language='fr')

# Display the translation
print(f"\nOriginal text (English): {user_input}")
print(f"Translated text (French): {user_dataframe_translated['translated_text'].iloc[0]}")
