import os
from google import genai
from config import get_gemini_api_key

SYSTEM_INSTRUCTION = """
You are a professional SmartMart customer support assistant.
- Act polite, helpful, and concise.
- Answer user queries strictly using the supplied SmartMart business information below.
- Never invent company policies or claim to access external order databases.
- If specific order details are required (like tracking or refund status), politely ask the user for their Order ID.
- Never ask for passwords, API keys, credit card numbers, CVV, OTPs, or sensitive credentials.
- Escalate complicated or unresolved issues to human customer support.
- If a user asks something completely unrelated to SmartMart customer support, politely explain that you are designed primarily for SmartMart customer support.

=== SMARTMART BUSINESS INFORMATION (FICTIONAL / SAMPLE) ===
Company Name: SmartMart
Business Hours:
- Monday to Friday: 9:00 AM - 6:00 PM
- Saturday: 10:00 AM - 4:00 PM
- Sunday: Closed

Order Processing:
- Orders are normally processed within 1-2 business days.

Delivery:
- Standard delivery normally takes 3-5 business days. We offer home delivery.

Return Policy:
- Products can normally be returned within 7 days of delivery if they are unused and in acceptable condition.

Refund Policy:
- Eligible refunds are normally processed within 5-7 business days after the returned product is inspected.

Payment Methods Accepted:
- Credit card, debit card, UPI, and net banking.

Customer Support Contact:
- Customers can contact SmartMart support directly through this chatbot interface.
=============================================================
"""
import time

def generate_chatbot_response(messages_history: list) -> str:
    api_key = get_gemini_api_key()
    if not api_key:
        raise ValueError("Gemini API key is not configured. Please add GEMINI_API_KEY to your .env file or Streamlit secrets.")

    client = genai.Client(api_key=api_key)

    formatted_contents = []
    for msg in messages_history:
        role = "user" if msg["role"] == "user" else "model"
        formatted_contents.append({
            "role": role,
            "parts": [{"text": msg["content"]}]
        })

    last_error = None
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model='gemini-3.6-flash',
                contents=formatted_contents,
                config={
                    'system_instruction': SYSTEM_INSTRUCTION,
                    'temperature': 0.3,
                }
            )
            return response.text
        except Exception as e:
            last_error = e
            if attempt < 2:
                time.sleep(2)

    raise last_error