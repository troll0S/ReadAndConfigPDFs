import fitz  # PyMuPDF
import os
import tkinter as tk
from tkinter import filedialog

def analyze_pdf(filepath):
    print(f"Plik: {os.path.basename(filepath)}")
    doc = fitz.open(filepath)
    page = doc[0]  # analizujemy pierwszą stronę

    # Pobieramy tekst w postaci strukturalnej
    blocks = page.get_text("dict")["blocks"]
    for block in blocks:
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                text = span["text"]
                bbox = span["bbox"]  # [x0, y0, x1, y1]
                print(f"Tekst: '{text}' | Pozycja: {bbox}")
    print("=" * 60)

def main():
    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory(title="Wybierz folder z plikami PDF")

    if not folder:
        print("Nie wybrano folderu.")
        return

    for filename in os.listdir(folder):
        if filename.lower().endswith(".pdf"):
            path = os.path.join(folder, filename)
            analyze_pdf(path)

if __name__ == "__main__":
    main()
