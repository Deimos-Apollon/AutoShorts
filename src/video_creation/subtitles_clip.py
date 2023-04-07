from collections import namedtuple
from typing import Sequence, List, Tuple
import pvleopard
from moviepy.video.VideoClip import TextClip
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

    start_time, word_part = words[0].start_sec, []
    for i, word_info in enumerate(words[:-1]):
        if i % words_on_screen == 0:
            word_part = []
        start_time = word_info.start_sec
        end_time = words[i+1].start_sec
        word_part.append(word_info.word)
        words_slice_info = ((start_time, end_time), " ".join(word_part))
        subtitles_list.append(words_slice_info)

    # add last subtitles
    word_part.append(words[-1].word)
    words_slice_info = ((words[-1].start_sec, words[-1].end_sec), " ".join(word_part))
    subtitles_list.append(words_slice_info)
    return subtitles_list


def get_subtitles_clip(audio_path: str, size: Tuple[int, int]) -> SubtitlesClip:
    """
    Generates a SubtitlesClip object given an audio file path.

    Args:
        audio_path (str): The path to the audio file to generate subtitles for.
        size: Tuple[int, int]: Size of the subtitles on the video (height, width)
    Returns:
        SubtitlesClip: A SubtitlesClip object representing the subtitles of the audio file.
    """
    # Create a pvleopard client and process the audio file to obtain its transcript and word sequence
    leopard = pvleopard.create(access_key=PVLEOPARD_ACCESS_KEY)
    transcript, words = leopard.process_file(audio_path)

    # Generate the subtitle list from the word sequence
    subtitle_list = __generate_subtitles(words)

    def text_transformer(txt):
        return TextClip(txt.upper(), font='Impact', color='gold', method='caption',
                        stroke_color='black', size=size, fontsize=70, stroke_width=3)

    # Create a SubtitlesClip object from the subtitle list and center it on the screen
    subtitles = SubtitlesClip(subtitle_list, text_transformer)
    subtitles = subtitles.set_position(('center', 'center'))
    subtitles = subtitles

    return subtitles

