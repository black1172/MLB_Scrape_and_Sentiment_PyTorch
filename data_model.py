@dataclass
class ContentItem:
    # Basic metadata
    id: str
    source: str = "reddit"
    content: str
    author: str
    timestamp: datetime
    url: str
    item_type: str  # "post" or "comment"
    parent_id: Optional[str] = None  # for comments linking to posts
    
    # Engagement metrics
    engagement: Dict  # {upvotes, comments, upvote_ratio}
    
    # NLP analysis results
    sentiment: float  # -1 to 1
    content_type: str  # "news", "opinion", "analysis", "sarcasm", "meme"
    team_mentions: List[str]
    player_mentions: List[str]