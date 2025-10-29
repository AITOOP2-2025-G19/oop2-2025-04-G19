import mlx_whisper

def preprocess_audio() -> str:
    """
    指定されたWAVファイルをmlx-whisperを使用して文字起こしする。

    処理の結果を標準出力に出力する。

    Returns:
        str: 文字起こしされたテキスト。
    """

    audio_file_path = "python-audio-output.wav"

    result = mlx_whisper.transcribe(
    audio_file_path, path_or_hf_repo="whisper-base-mlx"
    )

    return(result)

    

if __name__ == "__main__":
    text = preprocess_audio()
    print(text)

