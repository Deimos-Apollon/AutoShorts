from moviepy.audio.io.AudioFileClip import AudioFileClip


def get_audio_clip(audio_path: str) -> AudioFileClip:
    """
    Loads an audio clip given a file path.

    Args:
        audio_path (str): The file path of the audio file.

    Returns:
        AudioFileClip: An AudioFileClip object representing the loaded audio clip.
    """
    # Load the audio clip
    audio = AudioFileClip(audio_path)
    return audio
