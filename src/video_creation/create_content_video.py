from moviepy.audio.AudioClip import CompositeAudioClip
from moviepy.audio.fx.volumex import volumex
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip

from src.video_creation.audio_clip import get_audio_clip
from src.video_creation.subtitles_clip import get_subtitles_clip
from src.video_creation.video_clip import get_video_clip


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
    voiced_clip = get_audio_clip(voiced_audio_path)
    music_clip = get_audio_clip(music_audio_path).fx(volumex, 0.7) if music_audio_path else None

    video_clip = get_video_clip(video_path)
    subtitles_clip = get_subtitles_clip(voiced_audio_path, size=(video_clip.h * 0.2, video_clip.w * 0.9))

    # Combine the audio clips
    combined_audio = CompositeAudioClip([voiced_clip, music_clip]) if music_clip else voiced_clip

    # Combine the video clip and the subtitles
    video_clip = CompositeVideoClip([video_clip, subtitles_clip.set_duration(video_clip.duration)])

    video_clip = video_clip.set_duration(voiced_clip.duration + 1)

    # Set the combined audio clip to the video clip
    video_clip = video_clip.set_audio(combined_audio)
    video_clip.write_videofile(content_video_filename)


if __name__ == "__main__":
    video_filename = "input.mp4"
    voiced_story_filename = "voiced.wav"
    music_filename = "audio.mp3"
    out_video_filename = "first_video.mp4"
    create_content_video(video_path=f"../../input/video/{video_filename}",
                         voiced_audio_path=f"../../input/voiced/{voiced_story_filename}",
                         music_audio_path=f"../../input/music/{music_filename}",
                         content_video_filename=f"../../output/{out_video_filename}")

