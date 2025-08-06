import praw
from datetime import datetime
from typing import List
from data_model import ContentItem
from config import REDDIT_CONFIG

class RedditScraper:
    def __init__(self):
        # Create Reddit connection using PRAW
        self.reddit = praw.Reddit(
        client_id=REDDIT_CONFIG[0],        
        client_secret=REDDIT_CONFIG[1],    
        user_agent=REDDIT_CONFIG[2]        
    )
    
    # NOTE: '->' denotes the function return type
    def get_posts(self, subreddit_names: List[str], limit: int) -> List[ContentItem]:
        for subreddit_name, i in enumerate(subreddit_names):

    
    def get_comments(self, post_id: str, limit: int) -> List[ContentItem]:
        # TODO: Get comments from a specific post
        pass