
# Document Scanner and Organizer Prototype

Turns your paper documents into PDF files. Upload an image of a document, and the app will enhance its readability. Text is extracted using OCR to categorize the document.

## Installation

1. Ensure you have Python installed on your system.
2. Install the required Python libraries by running the following command in your terminal:
3. Download tesseract exe from https://github.com/UB-Mannheim/tesseract/wiki and run.
4. Add a path variable "C:\Program Files\Tesseract-OCR".

```bash

python -m venv venv
.\venv\Scripts\activate  # On Windows
source venv/bin/activate # On Unix or MacOS

```

```bash
python -m spacy download en_core_web_sm
```

```bash
pip install -r requirements.txt
```

## Running the Prototype

```bash
python main.py
```



