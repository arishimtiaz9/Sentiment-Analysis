import tkinter as tk
from textblob import TextBlob
from tkinter import messagebox


# Function to analyze sentiment
def analyze_sentiment():
    text = text_input.get("1.0", tk.END).strip()

    if text:
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity

        if sentiment > 0 and sentiment <= 0.5:
            result = "Slightly Positive Sentiment"
            root.config(bg="#90EE90")
        elif sentiment > 0.5 and sentiment<= 1:
            result= "Positive Sentiment 😊"
            root.config(bg="#90EE90")
        elif sentiment < 0 and sentiment >= -0.5:
            result = "Slightly Negative Sentiment"
            root.config(bg="#FF7F7F")
        elif sentiment < 0 and sentiment < -0.5:
            result = "Negative Sentiment 😔"
            root.config(bg="#FF7F7F")
        else:
            result = "Neutral Sentiment 😐"

        result_label.config(text=f"Polarity: {round(sentiment,2)}, Subjectivity: {round(blob.sentiment.subjectivity,2)}", fg="blue")
        result_label2.config(text=f"Sentiment: {result}", fg="blue",bg="yellow")
    else:
        messagebox.showwarning("Input Error", "Please enter some text to analyze.")


# Create the main window
root = tk.Tk()
root.title("Sentiment Analysis")
root.config(bg="#f0ae62")

# Set the window size
root.geometry("500x400")
root

# Input label
input_label = tk.Label(root, text="Enter the text to analyze sentiment: ", font=('Arial', 12,"bold","underline"))
input_label.pack(pady=10)

# Input text box
text_input = tk.Text(root, height=10, width=50, font=('Arial', 12))
text_input.pack(pady=10)

# Analyze button
analyze_button = tk.Button(root, text="Analyze Sentiment", command=analyze_sentiment, font=('Arial', 12),bg='lightblue')
analyze_button.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=('Times new roman',12))
result_label.pack(pady=5)

result_label2 = tk.Label(root, text="", font=('Times new roman',14,"bold"))
result_label2.pack(pady=10)

# Run the application
root.mainloop()
