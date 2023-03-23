import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import time

nltk.download('vader_lexicon')
print(
  "Disclaimer: This program is not fully refined. If you feel uncertain about the safety of a loved one, please contact the authorities to ensure their well-being. The purpose of this program is for users to input comments from their family members that they find suspicious. The program will then analyze the statement and determine if it indicates suicidal tendencies. By using this program, you agree that any harm caused by it is not the fault of its creator, contributors or Replit.com."
)
time.sleep(15)


def get_sentiment(text):
  sia = SentimentIntensityAnalyzer()
  sentiment = sia.polarity_scores(text)
  print(f"Positive: {sentiment['pos']}")
  print(f"Negative: {sentiment['neg']}")
  print(f"Neutral: {sentiment['neu']}")
  return sentiment['compound']


input_text = str(
  input(
    "Please enter the statement or note from your loved one that you find concerning: "
  ))

sia = SentimentIntensityAnalyzer()
sentiment = sia.polarity_scores(input_text)

num = sentiment['neg'] - sentiment['neu']
ov = sentiment['compound']
sentiment_value = get_sentiment(input_text)
print(f"Overall Sentiment: {sentiment_value}")
if num > 0.150:
  print("suicide possiblity, please contact officials")
elif ov < -0.5:
  print("suicide possiblity, please contact officials")
else:
  print("suicide not detected but keep close watch if uncertain")
