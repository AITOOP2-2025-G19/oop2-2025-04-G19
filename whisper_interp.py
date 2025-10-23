import mlx_whisper
from pydub import AudioSegment
import numpy as np

class interp:
    def preprocess_audio() -> str:
        audio_file_path = "python-audio-output.wav"

        result = mlx_whisper.transcribe(
        audio_file_path, path_or_hf_repo="whisper-base-mlx"
        )
        print(result)

       