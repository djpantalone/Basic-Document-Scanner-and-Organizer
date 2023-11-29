import pytest
from categorize import categorize_text, categories  
from main import run_ocr_on_image  # Import from main.py

test_data = [
    ("invoice.png", 'invoice'),
]

@pytest.mark.parametrize("image_path, expected_category", test_data)
def test_document_categorization(image_path, expected_category):
    extracted_text = run_ocr_on_image(image_path)
    categorized_result = categorize_text(extracted_text, categories)
    assert categorized_result.get(expected_category, False) == True
