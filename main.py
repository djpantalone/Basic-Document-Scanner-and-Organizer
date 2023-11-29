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
        'Financial Invoice': ['invoice', 'billing statement', 'total amount', 'amount due'],
        'Purchase Receipt': ['purchase receipt', 'grocery receipt', 'total amount', 'amount paid'],
        'Professional Resume': ['professional resume', 'qualifications', 'work experience', 'career summary'],
        'Legal Contract': ['legal contract', 'contractual terms', 'conditions of agreement'],
        'Cooking Recipe': ['cooking recipe', 'culinary instructions', 'delicious preparation'],
        'Current News Article': ['current news article', 'latest news', 'economic report'],
        'Fictional Novel': ['fictional novel', 'detective story', 'enthralling reading'],
        'Poetry Collection': ['poetry collection', 'love poems', 'nature verses'],
        'Scientific Research Paper': ['scientific research paper', 'academic research', 'experimental results'],
        'Product User Manual': ['product user manual', 'instruction booklet', 'product guide'],
        'Email Correspondence': ['email correspondence', 'colleague communication', 'meeting notification'],
        'Legal Documentation': ['legal documentation', 'contract details', 'legal agreement'],
        'Travel Guidebook': ['travel guidebook', 'tourist attractions', 'travel recommendations'],
        'Presentation Slides': ['presentation slides', 'conference presentation', 'visual aids'],
        'Blog Post Article': ['blog post article', 'health and wellness blog', 'informative article'],
        'Medical Report': ['medical report', 'health assessment', 'test results'],
        'Public Speech Transcript': ['public speech transcript', 'presidential speech', 'powerful address'],
        'Financial Statement': ['financial statement', 'company financials', 'profit and loss report'],
        'Academic Research Paper': ['academic research paper', 'study on climate change', 'research findings'],
        'Magazine Feature Article': ['magazine feature article', 'fashion trends feature', 'magazine publication'],
        'Meeting Minutes': ['meeting minutes', 'meeting notes', 'agenda items'],
        'Job Application': ['job application', 'cover letter', 'resume submission'],
        'Technical Manual': ['technical manual', 'technical instructions', 'troubleshooting guide'],
        'Customer Review': ['customer review', 'product review', 'feedback'],
        'Survey Questionnaire': ['survey questionnaire', 'survey form', 'response analysis'],
        'Legal Brief': ['legal brief', 'legal argument', 'case analysis'],
        'Business Proposal': ['business proposal', 'business plan', 'investment pitch'],
        'Academic Thesis': ['academic thesis', 'research thesis', 'dissertation'],
        'Health Report': ['health report', 'medical checkup', 'health diagnosis'],
        'Event Invitation': ['event invitation', 'event details', 'RSVP'],
        'Financial Report': ['financial report', 'financial analysis', 'quarterly earnings'],
        'Technical Specification': ['technical specification', 'specification document', 'product details'],
        'Marketing Brochure': ['marketing brochure', 'product brochure', 'marketing materials'],
        'Travel Itinerary': ['travel itinerary', 'trip details', 'travel plans'],
        'Other': []  # Add an "Other" category for unrecognized text
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
    try:
        # Ask the user for an image file path or provide an option for the default file
        image_path = input("Enter the path to an image file (or press Enter for default - invoice.png): ").strip()

        if not image_path:
            # If the user presses Enter without providing a path, use the default file
            image_path = "invoice.png"
        
        # Run OCR on the specified image
        text = run_ocr_on_image(image_path)

        # Categorize the text
        categorized_tokens = categorize_text(text)
        print("Category:", categorized_tokens)

    except FileNotFoundError:
        print("Error: The specified image file was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
