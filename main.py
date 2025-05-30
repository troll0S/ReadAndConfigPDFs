import fitz  # PyMuPDF
import os
import tkinter as tk
from tkinter import filedialog
import re

# Definiujemy prostokąty (Rect) z podanych współrzędnych
RECT_NAZWISKO = fitz.Rect(194.65, 173.80, 300.00, 181.36)
RECT_IMIONA = fitz.Rect(194.65, 188.91, 400.00, 196.47)
RECT_DATA = fitz.Rect(464.26, 337.40, 600.00, 343.79)

def capitalize_complex(text):
    # Rozbij na segmenty oddzielone spacją, myślnikiem, apostrofem, itp.
    return re.sub(r"([\wąćęłńóśżź]+)", lambda m: m.group(1).capitalize(), text.lower())

def sanitize_filename(name):
    # Usuwa niedozwolone znaki w nazwach plików (np. :, /, \, ?, *, itd.)
    return re.sub(r'[<>:"/\\|?*]', '', name)

def extract_fields(filepath):
    doc = fitz.open(filepath)
    page = doc[0]

    nazwisko = page.get_textbox(RECT_NAZWISKO).strip()
    imiona = page.get_textbox(RECT_IMIONA).strip()
    data_info = page.get_textbox(RECT_DATA).strip()

    return nazwisko, imiona, data_info

def main():
    # Wybieranie folderu z PDF-ami
    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory(title="Wybierz folder z plikami PDF")

    if not folder:
        print("Nie wybrano folderu.")
        return

    for filename in os.listdir(folder):
        if filename.lower().endswith(".pdf"):
            path = os.path.join(folder, filename)
            nazwisko, imiona, data_info = extract_fields(path)

            nowaNazwa = (
                    "KRK_" +
                    capitalize_complex(nazwisko) + " " +
                    capitalize_complex(imiona) + "_" +
                    data_info[-10:]
            )

            nowaNazwa = sanitize_filename(nowaNazwa) + ".pdf"

            new_path = os.path.join(folder, nowaNazwa)

            try:
                os.rename(path, new_path)
                print(f"Zmieniono nazwę: {filename} → {nowaNazwa}")
            except Exception as e:
                print(f"Błąd przy zmianie nazwy {filename}: {e}")

if __name__ == "__main__":
    main()
