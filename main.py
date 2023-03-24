import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
print(
  "Disclaimer: This program is not fully refined. If you feel uncertain about the safety of a loved one, please contact the authorities to ensure their well-being. The purpose of this program is for users to input comments from their family members that they find suspicious. The program will then analyze the statement and determine if it indicates suicidal tendencies. By using this program, you agree that any harm caused by it is not the fault of its creator, contributors or replit.com."
)

def get_sentiment(text):
    if not text:
        print("Error: Please enter a valid input.")
        return None
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    sentiment_scores = {
        'Positive': sentiment['pos'],
        'Negative': sentiment['neg'],
        'Neutral': sentiment['neu'],
        'Overall': sentiment['compound']
    }
    return sentiment_scores

input_text = str(
  input(
    "Please enter the statement or note from your loved one that you find concerning: "
  ))

sentiment_scores = get_sentiment(input_text)
if sentiment_scores:
    for key, value in sentiment_scores.items():
        print(f"{key} Sentiment: {value}")

    num = sentiment_scores['Negative'] - sentiment_scores['Neutral']
    ov = sentiment_scores['Overall']

    if num > 0.150:
      print("There is a possibility of suicidal tendencies. Please contact officials for assistance.")
    elif ov < -0.5:
      print("There is a possibility of suicidal tendencies. Please contact officials for assistance.")
    else:
      print("Suicidal tendencies were not detected but keep close watch if uncertain.")