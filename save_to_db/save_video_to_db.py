import pymongo
from pymongo.results import InsertOneResult
from server_variables import HOST, PORT


def save_video_to_db(video_obj: dict) -> InsertOneResult:
    """
    Saves video_obj to "Story" collection in db. Make sure to check if video_obj is valid via "is_video_valid" call.

    :param video_obj: dictionary representing "Story" collection's document, must be structured according
    to "Video" schema
    :return: Query result
    """
    with pymongo.MongoClient(HOST, PORT) as client:
        db = client['Autoshorts']
        db_story = db['Video']
        result = db_story.insert_one(video_obj)
        return result


def is_video_valid(video_obj: dict) -> bool:
    """
    Checks if "video_obj" corresponds with schema for "Video" collection in db.
    Must contain fields ["title", "length", "tags"].

    :param video_obj: dictionary that should be representing "Video" collection's document
    :return: True if story_obj accords "Video"
    """
    must_have_keys = ["title", "length", "tags"]

    # check if story_obj is None or empty, or is not a dict, or not contains must-have keys
    if (not video_obj) or (type(video_obj) != dict) or (not all(key in video_obj for key in must_have_keys)):
        return False

    if any(not video_obj[key] for key in must_have_keys):
        return False
    return True


