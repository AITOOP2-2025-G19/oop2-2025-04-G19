import csv

def transcription_save (text) -> None:

    row_data = [text]

    try :
        with open('transcription','a') as f:
            writer = csv.writer(f)
            csv_writer.writerow(row_data)
    except Exception as e:
        print(f" 書き込み中にエラーが発生しました: {e}")