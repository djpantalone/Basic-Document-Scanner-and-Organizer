def categorize_text(text, categories):
    category_results = {}
    if text is None:
        return {category: False for category in categories}

    # Convert the text to lowercase
    text = text.lower()

    for category, keywords in categories.items():
        # Convert each keyword to lowercase and check if it's in the lowercase text
        matching_keywords = [keyword for keyword in keywords if keyword.lower() in text]
        category_results[category] = bool(matching_keywords)
        print(f"Category: {category}, Matching Keywords: {matching_keywords}")

    return category_results




categories = {
    'Invoice': ['invoice', 'total amount', 'due date'],
    'Receipt': ['receipt', 'purchase', 'subtotal'],
    'Personal/Business Letter': ['dear', 'sincerely', 'regards'],
    'Bank Statement': ['balance', 'transaction', 'statement'],
    'Contract': ['agreement', 'contract', 'terms and conditions'],
    'Report': ['report', 'summary', 'findings'],
    'Article': ['author', 'article', 'published'],
    'Menu': ['menu', 'dish', 'cuisine'],
    'Email': ['subject', 'to', 'cc'],
    'Event Flyer': ['event', 'date', 'location'],
    'Brochure': ['brochure', 'features', 'services'],
    'Academic Paper': ['abstract', 'introduction', 'conclusion'],
    'News Bulletin': ['news', 'headline', 'report'],
    'Medical Prescription': ['prescription', 'dosage', 'medicine'],
    'User Manual': ['manual', 'instructions', 'guide'],
    'Warranty Document': ['warranty', 'guarantee', 'valid until'],
    'Shipping Label': ['ship to', 'tracking number', 'carrier'],
    'Travel Itinerary': ['itinerary', 'flight', 'accommodation'],
    'Job Offer Letter': ['offer', 'position', 'salary']
}



