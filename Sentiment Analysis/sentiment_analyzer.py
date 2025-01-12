import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    score = analyzer.polarity_scores(str(text))['compound']  # Get sentiment score
    if score > 0.05:
        return 'Positive'
    elif score < -0.05:
        return 'Negative'
    else:
        return 'Neutral'

def perform_analysis():
    input_file = 'cleaned_comments.csv'
    output_file = 'sentiment_results.csv'

    try:
        # Read the input file
        df = pd.read_csv(input_file)
        
        # Perform sentiment analysis
        df['Sentiment_Label'] = df['Cleaned_Comment'].apply(analyze_sentiment)
        
        # Save the results
        df.to_csv(output_file, index=False)
        print(f"Sentiment analysis saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    perform_analysis()