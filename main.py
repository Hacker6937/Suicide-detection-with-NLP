import tkinter as tk
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')


def get_sentiment(text):
  if not text:
    result_label["text"] = "Error: Please enter a valid input."
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


def analyze_sentiment():
  input_text = text_entry.get("1.0", tk.END).strip()
  sentiment_scores = get_sentiment(input_text)

  if sentiment_scores:
    result_text = ""
    for key, value in sentiment_scores.items():
      result_text += f"{key} Sentiment: {value}\n"

    num = sentiment_scores['Negative'] - sentiment_scores['Neutral']
    ov = sentiment_scores['Overall']

    if num > 0.150:
      result_text += "There is a possibility of suicidal tendencies. Please contact officials for assistance."
    elif ov < -0.5:
      result_text += "There is a possibility of suicidal tendencies. Please contact officials for assistance."
    else:
      result_text += "Suicidal tendencies were not detected but keep close watch if uncertain."

    result_label["text"] = result_text


root = tk.Tk()
root.title("Sentiment Analyzer")
root.geometry("400x300")

disclaimer_frame = tk.Frame(root)
disclaimer_frame.pack()

disclaimer_scrollbar = tk.Scrollbar(disclaimer_frame)
disclaimer_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

disclaimer_text = tk.Text(disclaimer_frame,
                          wrap=tk.WORD,
                          yscrollcommand=disclaimer_scrollbar.set)
disclaimer_text.insert(
  tk.END,
  "Disclaimer: This program is not fully refined. If you feel uncertain about the safety of a loved one, please contact the authorities to ensure their well-being. The purpose of this program is for users to input comments from their family members that they find suspicious. The program will then analyze the statement and determine if it indicates suicidal tendencies. By using this program, you agree that any harm caused by it is not the fault of its creator, contributors or Replit.com."
)
disclaimer_text.config(state=tk.DISABLED)
disclaimer_text.pack()

disclaimer_scrollbar.config(command=disclaimer_text.yview)

text_entry_label = tk.Label(
  root,
  text=
  "Please enter the statement or note from your loved one that you find concerning:"
)
text_entry_label.pack()

text_entry = tk.Text(root, height=5)
text_entry.pack()

analyze_button = tk.Button(root,
                           text="Analyze Sentiment",
                           command=analyze_sentiment)
analyze_button.pack()

result_label = tk.Label(root)
result_label.pack()

root.mainloop()
