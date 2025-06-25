import os
from dotenv import load_dotenv
import cohere

load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def generate_message(role):
    role = role.lower().strip()

    if "web" in role:
        return (
            "Hi [Name], I came across your profile and was really impressed by your work in web development. "
            "As a fellow web developer passionate about intuitive digital experiences, I'd love to connect and learn more about your journey."
        )
    elif "data" in role or "ml" in role or "ai" in role:
        return (
            "Hi [Name], I’m exploring Data Science and AI and noticed your expertise in the field. "
            "I'd love to connect and exchange insights and learn from your experience!"
        )
    elif "design" in role:
        return (
            "Hi [Name], your design work looks inspiring! I’m learning UI/UX and would love to connect and grow together creatively."
        )
    elif "marketing" in role or "digital" in role:
        return (
            "Hi [Name], I came across your profile while exploring digital marketing strategies. "
            "Your experience stood out, and I’d love to connect and learn more about your campaigns and growth tactics."
        )
    else:
        return (
            f"Hi [Name], I’m currently building my career in {role.title()} and came across your profile. "
            "It would be great to connect and learn from your journey in this field!"
        )
