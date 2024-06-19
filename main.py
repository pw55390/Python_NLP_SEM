import tkinter as tk
from tkinter import scrolledtext, messagebox
from transformers import pipeline
from googletrans import Translator
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, classification_report
from slowa_kluczowe import data  # Importowanie danych z pliku slowa_kluczowe.py
TF_ENABLE_ONEDNN_OPTS=0



# Użycie pipeline do generowania podsumowań z modelem slauw87/bart_summarisation
pipe = pipeline("summarization", model="slauw87/bart_summarisation", framework="pt")
translator = Translator()

def summarize_text(text, max_length=150, min_length=40):
    # Generowanie podsumowania za pomocą pipeline
    summary = pipe(text, max_length=max_length, min_length=min_length, length_penalty=2.0, num_beams=4, early_stopping=True)
    return summary[0]['summary_text']

def translate_text(text, dest_language="pl"):
    translation = translator.translate(text, dest=dest_language)
    return translation.text

# Funkcja do wczytania tekstu z pliku pattern.txt i wyświetlenia podsumowania
def load_and_process_file():
    try:
        with open("pattern.txt", "r") as file:
            text = file.read()
        text_input.delete("1.0", tk.END)
        text_input.insert(tk.END, text)
        summary = summarize_text(text)
        text_summary.delete("1.0", tk.END)
        text_summary.insert(tk.END, summary)
        translated_text = translate_text(text)
        category = classify_text(translated_text)
        text_category.delete("1.0", tk.END)
        text_category.insert(tk.END, f"Recognized Category: {category}")
    except FileNotFoundError:
        text_output.insert(tk.END, "Error: The file pattern.txt was not found in the project root directory.")
    except Exception as e:
        text_output.insert(tk.END, f"Error during processing: {e}")

# Funkcja do obsługi przycisku "PROCESS"
def on_process_click():
    input_text = text_input.get("1.0", tk.END).strip()
    if input_text:
        try:
            summary = summarize_text(input_text)
            text_summary.delete("1.0", tk.END)
            text_summary.insert(tk.END, summary)
            translated_text = translate_text(input_text)
            category = classify_text(translated_text)
            text_category.delete("1.0", tk.END)
            text_category.insert(tk.END, f"Recognized Category: {category}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during processing:\n{str(e)}")
    else:
        messagebox.showwarning("No Text", "Please enter some text to process.")


# Przygotowanie danych
texts = []
labels = []

for category, sentences in data.items():
    for sentence in sentences:
        texts.append(sentence)
        labels.append(category)

# Podział na dane treningowe i testowe
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

# Tworzenie modelu
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Trenowanie modelu
model.fit(X_train, y_train)

# Przewidywanie na danych testowych
y_pred = model.predict(X_test)

# Wyniki
#print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
#print(classification_report(y_test, y_pred, target_names=list(data.keys())))

# Funkcja do klasyfikacji tekstu
def classify_text(text):
    return model.predict([text])[0]


# Konfiguracja GUI
root = tk.Tk()
root.title("Text Summarizer and Classifier")

# Pole do wprowadzania tekstu
tk.Label(root, text="Enter text to process:").pack()
text_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10)
text_input.pack(padx=10, pady=10)

# Przycisk PROCESS
process_button = tk.Button(root, text="PROCESS", command=on_process_click)
process_button.pack(pady=10)

# Pole do wyświetlania podsumowania
tk.Label(root, text="Summary:").pack()
text_summary = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10)
text_summary.pack(padx=10, pady=10)

# Pole do wyświetlania kategorii
tk.Label(root, text="Recognized Category:").pack()
text_category = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=2)
text_category.pack(padx=10, pady=10)

# Wczytanie i przetworzenie tekstu z pliku po uruchomieniu programu
load_and_process_file()

# Uruchomienie aplikacji
root.mainloop()
