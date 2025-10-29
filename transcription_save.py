import csv
# import re # 👈 reモジュールはもう不要です！

def transcription_save (data_dict) -> None:
    # 📝 修正点: 引数名を data_dict に変更し、辞書を受け取ることを明確にします。

    FILE_NAME = 'transcription.csv'
    
    # 1. 渡されたものが辞書であることを確認し、'text' の値を取得する
    if not isinstance(data_dict, dict):
        print("エラー: 渡されたデータはPythonの辞書（dict）オブジェクトである必要があります。")
        return

    if 'text' in data_dict:
        text_to_save = data_dict['text']
    else:
        print("エラー: 辞書にキー 'text' が見つかりませんでした。")
        return
        
    row_data = [text_to_save] # 抽出した文字列をリストとして保存します

    try:
        # 2. 抽出したデータをCSVに保存
        with open(FILE_NAME, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(row_data)
        print(f"抽出したテキストを {FILE_NAME} に書き出しました。 ")
        
    except Exception as e:
        print(f" 書き込み中にエラーが発生しました: {e}")