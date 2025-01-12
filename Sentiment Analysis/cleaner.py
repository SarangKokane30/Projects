import pandas as pd
import re

def clean_comment(text):
    text = str(text).lower()  # Convert to string and lowercase
    text = re.sub(r'http\S+|www\S+', '', text)  # Remove URLs
    text = re.sub(r'[^a-z\s]', '', text)        # Keep only alphabets and spaces
    return text.strip()  # Remove extra spaces

def clean_comments():
    input_file = 'youtube_comments.csv'
    output_file = 'cleaned_comments.csv'

    try:
        df = pd.read_csv(input_file)  # Read the CSV file
        df['Cleaned_Comment'] = df['Comment'].apply(clean_comment)  # Clean comments
        df['Cleaned_Comment'].dropna()
        df.to_csv(output_file, index=False)  # Save cleaned comments
        print(f"Cleaned comments saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    clean_comments()
