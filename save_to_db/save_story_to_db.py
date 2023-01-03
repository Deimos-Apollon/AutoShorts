import pymongo
from pymongo.results import InsertOneResult
from server_variables import HOST, PORT


def save_story_to_db(story_obj: dict) -> InsertOneResult:
    """
    Saves story_obj to "Story" collection in db. Make sure to check if story_obj is valid via "is_story_valid" call.

    :param story_obj: dictionary representing "Story" collection's document, must be structured according
    to "Story" schema
    :return: Query result
    """
    with pymongo.MongoClient(HOST, PORT) as client:
        db = client['Autoshorts']
        db_story = db['Story']
        result = db_story.insert_one(story_obj)
        return result


def is_story_valid(story_obj: dict) -> bool:
    """
    Checks if "story_obj" corresponds with schema for "Story" collection in db.
    Must contain fields "header", "language", "content", "tags".

    :param story_obj: dictionary that should be representing "Story" collection's document
    :return: True if story_obj accords "Story"
    """
    must_have_keys = ["header", "language", "content", "tags"]

    # check if story_obj is None or empty, or is not a dict, or not contains must-have keys
    if (not story_obj) or (type(story_obj) != dict) or (not all(key in story_obj for key in must_have_keys)):
        return False

    # if any of values is None or empty
    if any(not story_obj[key] for key in must_have_keys):
        return False
    return True
