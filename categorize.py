def categorize_text(text, categories):
    category_results = {}
    for category, keywords in categories.items():
        if any(keyword in text for keyword in keywords):
            category_results[category] = True
        else:
            category_results[category] = False
    return category_results

# Example usage
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



