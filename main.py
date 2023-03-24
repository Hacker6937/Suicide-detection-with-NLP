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

root=tk.Tk()
root.title("Sentiment Analyzer")
root.geometry("400x300")

main_frame=tk.Frame(root)
main_frame.pack(fill=tk.BOTH,expand=1)

canvas=tk.Canvas(main_frame)
canvas.pack(side=tk.LEFT,fill=tk.BOTH,expand=1)

xscrollbar=tk.Scrollbar(main_frame,orient=tk.HORIZONTAL,command=canvas.xview)
xscrollbar.pack(side=tk.BOTTOM,fill=tk.X)

yscrollbar=tk.Scrollbar(main_frame,orient=tk.VERTICAL,command=canvas.yview)
yscrollbar.pack(side=tk.RIGHT,fill=tk.Y)

canvas.configure(xscrollcommand=xscrollbar.set,
                 yscrollcommand=yscrollbar.set)

canvas.bind('<Configure>',lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

second_frame=tk.Frame(canvas)

canvas.create_window((0,0),window=second_frame,
                     anchor='nw')

disclaimer_label = tk.Label(second_frame,text="Disclaimer: This program is not fully refined. If you feel uncertain about the safety of a loved one, please contact the authorities to ensure their well-being. The purpose of this program is for users to input comments from their family members that they find suspicious. The program will then analyze the statement and determine if it indicates suicidal tendencies. By using this program, you agree that any harm caused by it is not the fault of its creator, contributors or Replit.com.",wraplength=380)
disclaimer_label.pack()

text_entry_label = tk.Label(second_frame,text="Please enter the statement or note from your loved one that you find concerning:")
text_entry_label.pack()

text_entry = tk.Text(second_frame,height=5,width=40)
text_entry.pack()

analyze_button = tk.Button(second_frame,text="Analyze Sentiment",command=analyze_sentiment,width=20,height=2,bg='lightblue')
analyze_button.pack(pady=(10))

result_label=tk.Label(second_frame,width=40,height=10,bg='white',wraplength=380,borderwidth=2,
relief="solid")
result_label.pack(pady=(10))

root.mainloop()