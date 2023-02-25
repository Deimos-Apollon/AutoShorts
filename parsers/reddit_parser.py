import praw
import re
import csv
from datetime import datetime
from parsers.reddit_auth_tokens import REDDIT_TOKENS


def remove_links(text):
    """Removes links from text"""
    return re.sub(r'http\S+', '', text)


class RedditParser:
    reddit = praw.Reddit(**REDDIT_TOKENS)
    subreddits = ['dating', 'relationships', 'relationship_advice', 'marriage', 'breakups', 'advice', 'sex',
                  'sexover30',
                  'AskMen', 'AskWomen', 'AskReddit', 'Asexual', 'Demisexuality', 'DeadBedrooms', 'ForeverAlone',
                  'polyamory', 'LongDistance', 'NoFap', 'OneY', 'TwoXChromosomes', 'offmychest', 'TrueOffMyChest',
                  'confession', 'AmItheAsshole', 'Tinder', 'Bumble', 'OkCupid', 'POF', 'Match', 'R4R']

    def get_top_posts(self, subreddit_name, limit):
        """Returns list of top posts from given subreddit"""
        subreddit = self.reddit.subreddit(subreddit_name)
        return list(subreddit.top(time_filter='week', limit=limit))

    def get_hot_posts(self, subreddit_name, limit):
        """Returns list of hot posts from given subreddit"""
        subreddit = self.reddit.subreddit(subreddit_name)
        return list(subreddit.hot(limit=limit))

    def get_new_posts(self, subreddit_name, limit):
        """Returns list of new posts from given subreddit"""
        subreddit = self.reddit.subreddit(subreddit_name)
        return list(subreddit.new(limit=limit))

    def get_all_posts(self, limit_for_each_category=10, categories_to_pick=('top', 'hot', 'new')):
        all_posts = []
        for subreddit_name in self.subreddits:
            if 'top' in categories_to_pick:
                top_posts = self.get_top_posts(subreddit_name, limit_for_each_category)
                all_posts.extend(top_posts)
            if 'hot' in categories_to_pick:
                hot_posts = self.get_hot_posts(subreddit_name, limit_for_each_category)
                all_posts.extend(hot_posts)
            if 'new' in categories_to_pick:
                new_posts = self.get_new_posts(subreddit_name, limit_for_each_category)
                all_posts.extend(new_posts)

        # remove duplicates
        all_posts = list(set(all_posts))
        for post in all_posts:
            post.selftext = remove_links(post.selftext)

        return all_posts

    @staticmethod
    def save_to_csv(posts, filename, min_rating=500):
        count = 0
        with open(filename, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Subreddit', 'Title', 'Text', 'Rating', 'URL', 'Num Comments', 'ID', 'Created', 'Symbols'])
            for post in posts:
                if post.score >= min_rating:
                    text = remove_links(post.selftext)
                    symbols = len(text)
                    if 1000 <= symbols <= 7000:
                        writer.writerow(
                            [post.subreddit_name_prefixed, post.title, text, post.score, post.url, post.num_comments,
                             post.id, datetime.fromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S'), symbols])
                        count += 1
        print(f"Saved {count} posts to {filename}")
