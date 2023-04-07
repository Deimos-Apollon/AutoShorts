

class FormatConverter:
    @staticmethod
    def get_story_dict(header, language, content, tags) -> dict[str, str]:
        """
        General method for getting story dictionary (corresponding to DB format

        :return: dict, representing Story document
        """
        return {"header": header, "language": language, "content": content, "tags": tags}

    def reddit_to_story_one(self, reddit_post):
        """
        Converts reddit to `Story` DB format
        """
        return self.get_story_dict(header=reddit_post.title, language="en", content=reddit_post.selftext,
                                   tags=str(reddit_post.subreddit))

    def reddit_to_story_many(self, reddit_posts):
        stories = [self.reddit_to_story_one(post) for post in reddit_posts]
        return stories
