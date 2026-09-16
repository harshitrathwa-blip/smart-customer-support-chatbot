import re

def preprocess_text(text: str) -> str:
    """
    Performs lightweight NLP preprocessing:
    - Lowercase normalization
    - Whitespace cleanup
    - Basic punctuation handling
    """
    if not text:
        return ""
    # Lowercase
    processed = text.lower()
    # Remove extra whitespaces
    processed = re.sub(r'\s+', ' ', processed).strip()
    # Remove basic punctuation for keyword matching while keeping words intact
    processed = re.sub(r'[^\w\s]', '', processed)
    return processed

def detect_intent(text: str) -> tuple[str, list[str]]:
    """
    Simple intent detection layer using keyword and rule matching.
    Returns a tuple of (detected_intent, extracted_keywords).
    """
    if not text:
        return "unknown", []

    cleaned_text = preprocess_text(text)
    words = cleaned_text.split()

    # Define keyword mapping rules
    intents = {
        "greeting": ["hi", "hello", "hey", "greetings", "good", "morning", "evening"],
        "business_hours": ["hours", "timing", "timings", "open", "close", "time", "working"],
        "order_status": ["status", "where", "placed", "order"],
        "order_tracking": ["track", "tracking", "shipped", "dispatch", "delivery"],
        "return_request": ["return", "replace", "exchange", "send back"],
        "refund_request": ["refund", "money back", "repay", "cashback"],
        "payment_issue": ["payment", "failed", "card", "upi", "netbanking", "transaction", "deducted"],
        "cancel_order": ["cancel", "cancellation", "stop order"],
        "delivery_information": ["delivery", "shipping", "days", "take", "arrive", "home delivery"],
        "product_information": ["product", "item", "stock", "available", "catalog"],
        "complaint": ["damage", "damaged", "broken", "worst", "bad", "complaint", "issue", "poor"],
        "contact_support": ["support", "agent", "human", "contact", "call", "helpdesk"],
        "goodbye": ["bye", "goodbye", "thanks", "thank you", "exit"]
    }

    matched_intent = "unknown"
    matched_keywords = []

    for intent, keywords in intents.items():
        found = [kw for kw in keywords if kw in cleaned_text or any(kw in word for word in words)]
        if found:
            matched_intent = intent
            matched_keywords = list(set(found))
            break # Return the first strong intent match

    return matched_intent, matched_keywords