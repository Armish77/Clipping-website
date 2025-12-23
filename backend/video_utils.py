import subprocess

def crop_vertical(input_video, output_video, start, duration):
    """
    Crops a 16:9 video into a 9:16 vertical clip
    """
    subprocess.run(
        [
            "ffmpeg", "-y",
            "-ss", str(start),
            "-i", input_video,
            "-t", str(duration),
            "-vf", "crop=607:1080:656:0",
            "-c:a", "copy",
            output_video
        ],
        check=True
    )
