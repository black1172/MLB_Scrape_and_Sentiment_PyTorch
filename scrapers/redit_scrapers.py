import praw
from datetime import datetime
from typing import List
from data_model import ContentItem
from config import REDDIT_CONFIG

class RedditScraper:
    def __init__(self):
        # TODO: Initialize Reddit connection
        pass
    
    # NOTE: '->' denotes the function return type
    def get_posts(self, subreddit_names: List[str], limit: int) -> List[ContentItem]:
        # TODO: Scrape posts from subreddits
        pass
    
    def get_comments(self, post_id: str, limit: int) -> List[ContentItem]:
        # TODO: Get comments from a specific post
        pass