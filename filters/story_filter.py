MIN_CONTENT_LENGTH = 15
MAX_CONTENT_LENGTH = 800
MIN_HEADER_LENGTH = 8
MAX_HEADER_LENGTH = 200


def filter_stories(stories):
    new_stories = list(filter(is_story_valid, stories))
    return new_stories


def is_story_valid(story):
    if not (MIN_CONTENT_LENGTH <= len(story['content']) <= MAX_CONTENT_LENGTH):
        return False
    if not (MIN_HEADER_LENGTH <= len(story['header']) <= MAX_HEADER_LENGTH):
        return False
    return True
