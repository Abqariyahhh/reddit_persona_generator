import os
import argparse
from utils.reddit_scraper import scrape_user_data
from openai import OpenAI
from dotenv import load_dotenv
from tqdm import tqdm


load_dotenv()

# Initialize OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")  # Set this in your .env
)

def summarize_persona(posts, comments):
    combined_texts = []

    # Collect post content
    for p in posts:
        combined_texts.append(f"POST: {p['title']}\n{p['selftext']}\nURL: {p['permalink']}")

    # Collect comment content
    for c in comments:
        combined_texts.append(f"COMMENT: {c['body']}\nURL: {c['permalink']}")

    # Join texts safely outside the f-string
    joined_text = "\n\n".join(combined_texts[:20])  

    prompt = f"""
You are a language model helping generate user personas.
Using the following Reddit posts and comments, build a detailed user persona.

Include the following in the persona:
- Likely age range
- Interests
- Political/social opinions (if any)
- Personality traits
- Writing style
- Subreddits they frequent
- Anything else noticeable

After each trait, cite the comment/post (with its URL) that supports it.

Reddit Data:
{joined_text}
"""

    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",  
        messages=[
            {"role": "system", "content": "You analyze Reddit data to generate user personas."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1500
    )

    return response.choices[0].message.content


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("username", help="Reddit username (e.g., kojied or Hungry-Move-6603)")
    args = parser.parse_args()

    posts, comments = scrape_user_data(args.username)
    print(f"Collected {len(posts)} posts and {len(comments)} comments from u/{args.username}")

    persona = summarize_persona(posts, comments)

    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)
    out_file = f"{output_dir}/{args.username.lower()}_persona.txt"

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(persona)

    print(f"Persona saved to {out_file}")


if __name__ == "__main__":
    main()
