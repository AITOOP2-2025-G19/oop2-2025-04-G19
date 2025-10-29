# 学籍番号と名前を書くと作業番号を書く
#リーダー k24128 古澤天翔
#業者1 K24091 高宮千聖
#作業者2 x24006 井手和海
#作業者3 k24062 輿水遥人
# 変数名関数名はsampleから

# 1 ファイル名:record_audio.py 関数名:record_audio
# 2 ファイル名:whisper_interp.py 関数名:preprocess_audio
# 3 ファイル名:transcription_save.py 関数名:transcription_save

# 2の返り値を3で使用する関数名 text
import record_audio 
import whisper_interp 
import transcription_save


record_audio.record_audio()

text = whisper_interp.preprocess_audio()

transcription_save.transcription_save(text)