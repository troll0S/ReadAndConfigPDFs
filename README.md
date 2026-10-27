# formatKRKfiles – Batch PDF Renamer

A small Python tool that automates a real office task: it renames batches of PDF certificates from the Polish National Criminal Register (KRK) based on data read directly from each document.

Instead of opening every file and typing its name by hand, you pick a folder and every PDF is renamed to a consistent format:

```
KRK_<Surname> <First names>_<date>.pdf
```

## How it works

1. A folder picker (Tkinter) asks for the folder with the PDF files.
2. For each PDF, PyMuPDF reads the text from fixed areas of the first page: surname, first names and the date.
3. Names are normalised (correct capitalisation, including Polish characters and double-barrelled names), and characters that are not allowed in file names are removed.
4. The file is renamed and the result is printed for each file; errors are reported without stopping the batch.

## Tech stack

Python · PyMuPDF (fitz) · Tkinter · regular expressions · PyInstaller (standalone Windows .exe)

## Getting started

**From source:**

```bash
git clone https://github.com/troll0S/ReadAndConfigPDFs.git
cd ReadAndConfigPDFs
pip install pymupdf
python main.py
```

**Windows executable:** download `formatKRKfiles.exe` from the Releases page and run it.

## Usage notes

- Put all PDF files attached to the KRK certificates in one folder, then run the app and select that folder.
- Do not include two identical files with different names – this case is not supported.
- The fields are read from fixed positions on the page, so the tool works only with documents in the standard KRK certificate layout.
- Files are processed locally; no data leaves your computer.

## License

This project uses PyMuPDF, which is licensed under AGPLv3, so the application is distributed under **AGPLv3** as well. Use and redistribution must comply with that license.

## Author

Wojciech Jurek – [GitHub](https://github.com/troll0S) · [LinkedIn](https://www.linkedin.com/in/wojciech-jurek-825027339)
