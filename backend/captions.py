import whisper
import subprocess
import os

def add_captions(input_video, output_video):
    """
    Generates captions using Whisper (lazy-loaded)
    """

    # 🔹 Load model ONLY when function is called
    model = whisper.load_model("tiny")

    audio_file = "temp_audio.wav"

    subprocess.run(
        [
            "ffmpeg", "-y",
            "-i", input_video,
            "-ar", "16000",
            "-ac", "1",
            audio_file
        ],
        check=True
    )

    result = model.transcribe(audio_file)
    text = result["text"].replace("'", "").replace('"', "")

    os.remove(audio_file)

    subprocess.run(
        [
            "ffmpeg", "-y",
            "-i", input_video,
            "-vf",
            f"drawtext=text='{text}':"
            "fontcolor=white:fontsize=36:"
            "box=1:boxcolor=black@0.6:"
            "x=(w-text_w)/2:y=h-120",
            output_video
        ],
        check=True
    )
