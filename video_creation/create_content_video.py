from moviepy.audio.AudioClip import CompositeAudioClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip

from video_creation.audio_clip import get_audio_clip
from video_creation.subtitles_clip import get_subtitles_clip
from video_creation.video_clip import get_video_clip


def create_content_video(video_path: str,
                         voiced_audio_path: str,
                         music_audio_path: str,
                         content_video_filename: str) -> None:
    """
    Creates a content video by combining a video clip, a voiced audio clip with subtitles, and a background music
    audio clip.

    Args:
        video_path (str): The file path of the video clip.
        voiced_audio_path (str): The file path of the voiced audio clip with subtitles.
        music_audio_path (str): The file path of the background music audio clip.
        content_video_filename (str): The file path of the content video to be written.
    Returns:
        CompositeVideoClip: A CompositeVideoClip object representing the combined content video.
    """
    subtitles_clip = get_subtitles_clip(voiced_audio_path)
    voiced_clip = get_audio_clip(voiced_audio_path)
    music_clip = get_audio_clip(music_audio_path)
    video_clip = get_video_clip(video_path)

    # Combine the audio clips
    combined_audio = CompositeAudioClip([voiced_clip, music_clip])

    # Combine the video clip and the subtitles
    video_clip = CompositeVideoClip([video_clip, subtitles_clip.set_duration(video_clip.duration)])

    # Set the combined audio clip to the video clip
    video_clip = video_clip.set_audio(combined_audio)
    video_clip.write_videofile(content_video_filename)


if __name__ == "__main__":
    create_content_video(video_path=r"C:\Users\Deimos\Desktop\AutoShorts\playing\input\wheelchair.mp4",
                         voiced_audio_path=r"C:\Users\Deimos\Desktop\AutoShorts\playing\output\voiced.wav",
                         music_audio_path=r"C:\Users\Deimos\Desktop\AutoShorts\playing\input\Fluffing-a-Duck.mp3",
                         content_video_filename="output_after_refactor.mp4")

