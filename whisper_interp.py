import mlx_whisper

class interp:
    def preprocess_audio() -> str:
        audio_file_path = "python-audio-output.wav"

        result = mlx_whisper.transcribe(
        audio_file_path, path_or_hf_repo="whisper-base-mlx"
        )
        print(result)
    '''
    :param none
    :return 音声ファイルを文字起こししたテキストを返す
        音声ファイルをmlx_whisperを使って文字起こしする処理
    '''
       