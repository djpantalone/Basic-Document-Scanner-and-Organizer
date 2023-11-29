
# Document Scanner and Organizer Prototype

Turns your paper documents into PDF files. Upload an image of a document, and the app will enhance its readability. Text is extracted using OCR to categorize the document.

## Installation

1. Ensure you have Python installed on your system.
2. Install the required Python libraries by running the following command in your terminal:
3. Download tesseract exe from https://github.com/UB-Mannheim/tesseract/wiki and run.
4. Add a path variable "C:\Program Files\Tesseract-OCR".

# Create a virtual environment
```bash
python -m venv venv
```

# Activate a virtual environment

## Windows
```bash
.\venv\Scripts\activate  
```

## Unix or MacOS
```
source venv/bin/activate 
```


# Download a specific spaCy language model.
```bash
python -m spacy download en_core_web_sm
```

# Install the required Python libraries
```bash
pip install -r requirements.txt
```

# Running the Prototype
```bash
python main.py
```



