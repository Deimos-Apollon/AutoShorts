from moviepy.video.io.VideoFileClip import VideoFileClip


def get_video_clip(video_path: str) -> VideoFileClip:
    """
    Loads a video clip given a file path.

    Args:
        video_path (str): The file path of the video file.

    Returns:
        VideoFileClip: A VideoFileClip object representing the loaded video clip.
    """
    # Load the video clip
    video = VideoFileClip(video_path)
    return video
