import requests
import json
import os


# ファイルに結果を書き込み
def output_2_file(jsons):
    i = 1
    for x in jsons['results']:
        with open('result.txt', mode='a') as f:
            print('No. %s' % i, file=f)
            print('Zip code: %s' % x['zipcode'], file=f)
            print('Address: %s%s%s' %
                 (x['address1'], x['address2'], x['address3']), file=f)
            print('Ruby: %s%s%s' %
                 (x['kana1'], x['kana2'], x['kana3']), file=f)
            print('')
            i += 1


# メイン処理部分
results = 'result.txt'  # 結果を書き込むファイル
zipCode = input('Please input ZIP code for search: ')

baseUrl = 'https://zipcloud.ibsnet.co.jp/api/search'
limitNo = 20  # 取得する最大件数
parData = {'zipcode': zipCode, 'limit': limitNo}

# API 問い合わせの実行
response = requests.get(baseUrl, parData)

# 結果を辞書型に変換
jsons = json.loads(response.text)

# 結果ファイルが存在する場合は削除
if os.path.isfile(results):
    os.remove(results)

try:
    output_2_file(jsons)  # 結果をファイルに書き込み
except:  # エラー処理
    print('Error!')

    if jsons['message'] != None:  # エラーメッセージがある場合
        print(jsons['message'])
    else:  # エラーメッセージがない場合
        print('指定の郵便番号は存在しません。.')
