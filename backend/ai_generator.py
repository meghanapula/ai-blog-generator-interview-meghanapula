import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_blog_post(keyword, metrics):
    prompt = f"""
    Write a 600-word SEO-optimized blog post about "{keyword}".
    
    Include:
    - An introduction
    - 2–3 sections with H2 headings
    - A bullet list
    - A conclusion
    - Use {{AFF_LINK_1}} and {{AFF_LINK_2}} as affiliate placeholders

    Format it in Markdown.

    SEO Context:
    - Search Volume: {metrics['search_volume']}
    - Keyword Difficulty: {metrics['keyword_difficulty']}
    - CPC: ${metrics['avg_cpc']}
    """

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        content = response.text
        return content.replace("{{AFF_LINK_1}}", "https://example.com/product1")\
                      .replace("{{AFF_LINK_2}}", "https://example.com/product2")
    except Exception as e:
        print("❌ Gemini Error:", e)
        return "Error generating blog post"
