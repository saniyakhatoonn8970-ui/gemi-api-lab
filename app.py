print("Sending request to Gemini...")
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key="AQ.Ab8RN6Ixn4DkCrqO8OuLW4w8qGnyI6a7BHDaarqqqHMgO0V0Lg")

print("Sending request to Gemini...")

response = client.models.generate_content(
    model='gemini-3.5-flash-lite',
    contents='Explain artificial intelligence in simple terms.'
)

print("\nGemini Response:")
print(response.text)