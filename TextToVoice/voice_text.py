import pyttsx3
from typing import Optional

# Initialize the text-to-speech engine
engine = pyttsx3.init()


def voice_text(text_filename: str, voiced_audio_filename: str, rate: Optional[int] = 150) -> None:
    """
    Converts text to speech and saves the spoken audio as a WAV file.

    Args:
        text_filename (str): The filename of the text file to convert to speech.
        voiced_audio_filename (str): The filename to save the resulting audio as a WAV file.
        rate (int, optional): The rate of speech, in words per minute. Defaults to 150.

    Returns:
        None
    """
    engine.setProperty('rate', rate)

    with open(text_filename) as f:
        text = "".join(f.readlines()).strip()

    engine.save_to_file(text, voiced_audio_filename)
    engine.runAndWait()


if __name__ == "__main__":
    # Replace the filenames with your own text and audio filenames.
    voice_text(text_filename="your_text_file.txt",
               voiced_audio_filename="your_audio_file.wav",
               rate=150)
