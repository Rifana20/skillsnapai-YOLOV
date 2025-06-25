
import os
from dotenv import load_dotenv
import cohere

load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def rewrite_text(text, task="headline"):
    prompt = ""
    if task == "headline":
        prompt = f"Rewrite this LinkedIn headline to be ATS-optimized:\n{text}"
    else:
        prompt = f"Improve this LinkedIn About section for clarity and professional tone:\n{text}"
    
    response = co.generate(
        model='command',
        prompt=prompt,
        max_tokens=500,
        temperature=0.7
    )
    return response.generations[0].text.strip()
