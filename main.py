from PIL import Image
import pytesseract
import cv2
import os
from collections import Counter
import re

def preprocess_image_for_ocr(input_image, method="threshold"):
    """
    Preprocess the image to enhance OCR performance.
    - input_image: Image to preprocess.
    - method: Preprocessing method, either 'threshold' or 'blur'.
    Returns the filename of the processed image.
    """
    # Convert image to grayscale
    grayscale_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    # Apply chosen preprocessing method
    if method == "threshold":
        processed_image = cv2.threshold(grayscale_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    elif method == "blur":
        processed_image = cv2.medianBlur(grayscale_image, 3)
    else:
        processed_image = grayscale_image

    # Save the processed image temporarily
    temp_filename = f"temp_{os.getpid()}.jpg"
    cv2.imwrite(temp_filename, processed_image)

    return temp_filename

def extract_text_from_image(image_filename):
    """
    Perform OCR on a given image and return the extracted text.
    - image_filename: Filename of the image to process.
    Returns the extracted text.
    """
    with Image.open(image_filename) as img:
        extracted_text = pytesseract.image_to_string(img)

    # Remove the temporary image file
    os.remove(image_filename)

    return extracted_text

def run_ocr_on_image(image_path, preprocess_method="threshold"):
    """
    Main function to run OCR on a specified image.
    - image_path: Path to the image file.
    - preprocess_method: Method for preprocessing the image.
    """
    # Load the image from the given path
    image = cv2.imread(image_path)

    # Preprocess the image
    preprocessed_image_file = preprocess_image_for_ocr(image, preprocess_method)

    # Extract text using OCR
    text = extract_text_from_image(preprocessed_image_file)
    print("Extracted Text:")
    print(text)
    return text

def categorize_text(text):
    # Define categories and their associated keywords
    categories = {
        'Invoice': ['invoice', 'total amount', 'due'],
        'Receipt': ['receipt', 'total amount', 'paid'],
        'Resume': ['resume', 'qualifications', 'work experience'],
        'Contract': ['contract', 'terms and conditions', 'agreement'],
        'Recipe': ['recipe', 'make', 'delicious'],
        'News Article': ['news', 'latest news', 'economy'],
        'Novel': ['novel', 'detective', 'reading'],
        'Poem': ['poem', 'love', 'nature'],
        'Scientific Paper': ['scientific paper', 'research', 'results'],
        'User Manual': ['user manual', 'instructions', 'product'],
        'Email': ['email', 'colleague', 'meeting'],
        'Legal Document': ['legal document', 'contract details'],
        'Travel Guide': ['travel guide', 'tourist attractions'],
        'Presentation': ['presentation', 'conference'],
        'Blog Post': ['blog post', 'healthy eating'],
        'Medical Report': ['medical report', 'test results'],
        'Speech': ['speech', 'president', 'powerful'],
        'Financial Statement': ['financial statement', 'company profits'],
        'Research Paper': ['research paper', 'climate change'],
        'Magazine Article': ['magazine article', 'fashion trends']
    }

    # Initialize category counts
    category_counts = {category: 0 for category in categories}

    # Tokenize the text and convert to lowercase
    tokens = re.findall(r'\b\w+\b', text.lower())

    # Iterate through tokens and categorize
    for token in tokens:
        for category, keywords in categories.items():
            if any(keyword in token for keyword in keywords):
                category_counts[category] += 1

    # Determine the category with the highest count
    max_category = max(category_counts, key=category_counts.get)

    return max_category




if __name__ == '__main__':
    
    image_path = input("Enter a img path: ")
    text = run_ocr_on_image(image_path)


    # Categorize the text
    categorized_tokens = categorize_text(text)
    print("Category:", categorized_tokens)


    

   
