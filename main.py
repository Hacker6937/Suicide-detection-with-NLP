import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import time
nltk.download('vader_lexicon')
print("note: This program is not fully refined if you feel uncertain about a loved one please call the police and make sure they are safe")
time.sleep(5)
def get_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    print(f"Positive: {sentiment['pos']}")
    print(f"Negative: {sentiment['neg']}")
    print(f"Neutral: {sentiment['neu']}")
    return sentiment['compound']
input_text = str(input("Please type what the loved one said that you are unsure about or what was written on their note: "))

sia = SentimentIntensityAnalyzer()
sentiment = sia.polarity_scores(input_text)

num = sentiment['neg']-sentiment['neu']

sentiment_value = get_sentiment(input_text)
print(f"Overall Sentiment: {sentiment_value}")
if num > 0.150:
  print("suicide possiblity, please contact loved one or officials")
else:
  print("suicide not detected but keep close watch if uncertain")