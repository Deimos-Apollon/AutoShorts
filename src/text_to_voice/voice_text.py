import pyttsx3
from typing import Optional
import json

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')


def voice_text(text_filename: str, voiced_audio_filename: str, rate: Optional[int] = 150,
               voice_index: Optional[int] = 1) -> None:
    """
    Converts text to speech and saves the spoken audio as a WAV file.

    Args:
        text_filename (str): The filename of the text file to convert to speech.
        voiced_audio_filename (str): The filename to save the resulting audio as a WAV file.
        rate (int, optional): The rate of speech, in words per minute. Defaults to 150.
        voice_index (int, optional): Voice id to be used, 0 for female, 1 for male. Defaults to 1 (male).
    Returns:
        None
    """
    engine.setProperty('rate', rate)
    engine.setProperty('voice', voices[voice_index].id)

    with open(text_filename) as f:
        text = "".join(f.readlines()).strip()

    engine.save_to_file(text, voiced_audio_filename)
    engine.runAndWait()


if __name__ == "__main__":
    # Replace the filenames with your own text and audio filenames.
    text_filename = "sample.txt"
    out_audio_filename = "voiced.wav"
    voice_text(text_filename=f"../../input/story_text/{text_filename}",
               voiced_audio_filename=f"../../input/voiced/{out_audio_filename}",
               rate=180)
