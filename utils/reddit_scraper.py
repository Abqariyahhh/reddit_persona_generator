import praw
import os
from dotenv import load_dotenv

load_dotenv()

def get_reddit_instance():
    return praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )

def scrape_user_data(username):
    reddit = get_reddit_instance()
    user = reddit.redditor(username)
    
    posts, comments = [], []
    
    for submission in user.submissions.new(limit=None):
        posts.append({
            'title': submission.title,
            'selftext': submission.selftext,
            'url': submission.url,
            'permalink': f"https://www.reddit.com{submission.permalink}"
        })
        
    for comment in user.comments.new(limit=None):
        comments.append({
            'body': comment.body,
            'permalink': f"https://www.reddit.com{comment.permalink}"
        })
    
    return posts, comments
