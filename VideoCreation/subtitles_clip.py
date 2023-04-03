from collections import namedtuple
from typing import Sequence, List, Tuple
import pvleopard
from moviepy.video.tools.subtitles import SubtitlesClip
from TOKENS import PVLEOPARD_ACCESS_KEY

# Define a named tuple to represent a word and its corresponding start and end times and confidence score
Word = namedtuple('Word', ['word', 'start_sec', 'end_sec', 'confidence'])


def __generate_subtitles(words: Sequence[Word]) -> List[Tuple[Tuple[float, float], str]]:
    """
    Generates a list of subtitles given a sequence of words and their corresponding start and end times.

    Args:
        words (Sequence[Word]): A sequence of named tuples representing words and their corresponding start and end times.

    Returns:
        List[Tuple[Tuple[float, float], str]]: A list of tuples representing subtitles, where each tuple contains a
        tuple of start and end times and the subtitle text.
    """
    subtitles_list = []
    words_on_screen = 5
    for i in range(0, len(words), words_on_screen):
        words_slice = words[i:i+words_on_screen]
        start_time = words_slice[0].end_sec
        end_time = words_slice[-1].end_sec
        words_slice_info = ((start_time, end_time), " ".join([word_info.word for word_info in words_slice]))
        subtitles_list.append(words_slice_info)

    # for word_item in words:
    #     start_time = word_item.start_sec
    #     end_time = word_item.end_sec
    #     # there was a case when end = start with word 'I'
    #     if end_time - start_time < 1e-10:
    #         end_time += 0.2
    #     word = word_item.word
    #     word_info = ((start_time, end_time), word)
    #     subtitles_list.append(word_info)
    return subtitles_list


def get_subtitles_clip(audio_path: str) -> SubtitlesClip:
    """
    Generates a SubtitlesClip object given an audio file path.

    Args:
        audio_path (str): The path to the audio file to generate subtitles for.

    Returns:
        SubtitlesClip: A SubtitlesClip object representing the subtitles of the audio file.
    """
    # Create a pvleopard client and process the audio file to obtain its transcript and word sequence
    leopard = pvleopard.create(access_key=PVLEOPARD_ACCESS_KEY)
    transcript, words = leopard.process_file(audio_path)

    # Generate the subtitle list from the word sequence
    subtitle_list = __generate_subtitles(words)

    # Create a SubtitlesClip object from the subtitle list and center it on the screen
    subtitles = SubtitlesClip(subtitle_list)
    subtitles = subtitles.set_position(('center', 'center'))

    return subtitles

