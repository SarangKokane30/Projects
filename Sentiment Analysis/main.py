from extractor import extract_comments
from cleaner import clean_comments
from sentiment_analyzer import perform_analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_overall_sentiment():
    # Load sentiment results
    df = pd.read_csv('sentiment_results.csv')

    # Count sentiment labels
    sentiment_counts = df['Sentiment_Label'].value_counts()

    # Plot bar chart
    plt.figure(figsize=(10, 6))
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette='viridis')
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Comments')
    plt.show()

def main():
    print("Extracting comments...")
    extract_comments("https://www.youtube.com/watch?v=qbE0fzZ2Nfo")
                     
    print("Cleaning comments...")
    clean_comments()

    print("Analyzing sentiment...")
    perform_analysis()

    print("Visualizing overall sentiment...")
    visualize_overall_sentiment()


if __name__ == '__main__':
    main()







