---
tags:
  - Python
  - 覚書
---

# Python で使える例文集

## 1. if 文

### 1.1. in と not in

ある変数等に指定の値が含まれているかどうかを判定する、汎用性の高い構文

```python
line = 'Hello, I am Bob!'

if 'Hello' in line:
    print('"Hello" is included!')
```

逆に、含まれていない場合を判定したい場合は`not in`を使用する。

```python
line = 'Hello, I am Bob!'

if 'Bob' not in line:
    print('"Bob" is NOT included!')
else:
    print('"Bob" is included!')
```

### 1.2. AND/OR 演算子

```python
number = 5

if number > 0 and number < 10:
    print('Number has been into from 1 to 9')

if number == 0 or number == 5:
    print('Number is equal 0 or 5')
```

## 2. API への問い合わせ

### 2.1. API に問い合わせ、結果の JSON を dict 型として読み込む場合

返ってくる値は`レスポンスオブジェクト`。格納される主な属性は以下の通り。

- `status_code`: レスポンスのステータス（２００など）。str 型
- `headers`: レスポンスヘッダ。dic 型
- `text`: レスポンス文字列本体。str 型
- `content`: ファイルなどのバイナリデータを受信する場合に使用。byte 型

```python
import requests
import json

# API クエリをそのまま渡す場合
def get_api_response(arg):
    apiUrl = 'https://example.com/api/get/detail'
    res = requests.get(apiUrl)
    data = json.loads(res.text)  # text 属性のデータを dict 型に変換

    return data

# API クエリのパラメータ（?param1=value1 など）を辞書型で渡す場合
def get_malApi_response():
    urlrl = 'https://example.com/api/'
    param = {'param1':'value1', 'param2':'value2'}
    res = requests.get(urlrl, params=param)
    data = json.loads(res.text)

    return data

# ヘッダー情報を渡す場合
def get_malApi_response():
    urlrl = 'https://example.com/api/'
    hInfo = {'haeder1':'value1', 'header2':'value2'}
    res = requests.get(urlrl, headerss=hInfo)
    data = json.loads(res.text)

    return data

# POST でデータを渡す場合
def get_malApi_response():
    urlrl = 'https://example.com/api/'
    hInfo = {'param1':'value1', 'param2':'value2'}
    pData = {'key1': 'value1', 'key2': 'value2'}
    res = requests.post(urlrl, headers=info , data=pData)
    data = json.loads(res.text)

    return data

# ヘッダ情報を渡す場合
def get_api_response():
    apiUrl = 'https://example.com/api/'
    hedInf = {'param1':'value1', 'param2':'value2'}
    res = requests.get(apiUrl, headers=hedInf)
    data = json.loads(res.text)   # text 属性のデータを dict 型に変換

    return data
```

### 2.2. 返ってきた JSON のシングルクォーテーションをダブルクォーテーションにする場合

- `json.load`や`json.loads`だと、キー名や値の囲みがシングルクォーテーションになる。
- 都合が悪い場合、`json.dumps`を通せばダブルクォーテーションに変換できる。
  - （Pandas で読み込んだり、JSON ファイルとして書き出したい場合など）
- 但し、`json.dumps`した後のデータは dict 型では無い為、キーや値の取得はできない。

```python
import requests
import json

def get_malApi_response(arg):
    url = 'https://example.com/api/'
    param = arg  # arg = get/detail
    res = requests.get(urlrl + param)
    data = json.loads(res.text)
    resData = json.dumps(data)

    return data

```

## 3. ファイルのダウンロード

```py
import requests

dstUrl = 'https://www.meiji.ac.jp/isys/doc/seminar/Python_text.pdf'
fileName = 'test.pdf'
outName = 'output.pdf'

urlData = requests.get(dstUrl)
binData = urlData.content

with open(outName, mode='wb') as f:  # mode='wb'でバイト型書き込みに対応
    f.write(binData)
```

## 4. JSON ファイルの取扱

### 4.1. JSON 読み込み用モジュールの比較

- json.load():
  - json ファイルを読み込み、dict 型にする（引数は、ファイルオブジェクト）
  - `open`したファイルオブジェクトを渡す場合に使用
- json.loads():
  - json テキスト（str 型）を dict 型にする（引数は、str 型）
  - `response`オブジェクトの`text`属性を渡す場合に使用
- json.dump():
  - dict 型を json ファイルに保存する（引数は、ファイルオブジェクトと dict 型）
- json.dumps():
  - dict 型を str 型の json に整形する（引数は、dict 型）
  - `json.load`や`json.loads`で取得した dict 型に変換する場合などに使用

### 4.2. JSON ファイルからのデータ読み込み

```python
import json

with open('file.json', mode='r') as f:
    jsonData = json.load(f)  # JSON ファイルを読み込み、dict 型にする。
```

## 5. JSON データ （dict データ）の取扱

キーや値は dict 型でなければ取得できない為、dict 型として取り扱う。

### 5.1. キーの存在確認

```python
# 'meta'キーの存在確認
if 'meta' in jsonData and 'country' in jsonData['meta_data']:
    print(jsonData['meta_data'])

# 深い階層にあるキーの存在確認
if 'meta_data' in jsonData and 'country' in jsonData['meta_data']:
    print(jsonData['meta_data']['country'])
```

### 5.2. キー名から値を取得して特定文字列を検索

```python
if 'meta_data' in jsonData and 'country' in jsonData['meta_data']:
    if 'Japan' in jsonData['meta_data']['country']
        data = jsonData['meta_data']['country']
```

### 5.3. 値を取得する便利関数

- 辞書のキー指定が面倒な場合に使用
- 引数の数に応じてキーの数が自動で変化。キーが存在しない場合は空白を返す。

```python
def get_element(jsons, *eleVal):
    if len(eleVal) == 1:
        try:
            ret = jsons[eleVal[0]]
        except:
            ret = ''
        return ret
    elif len(eleVal) == 2:
        try:
            ret = jsons[eleVal[0]][eleVal[1]]
        except:
            ret = ''
        return ret
    elif len(eleVal) == 3:
        try:
            ret = jsons[eleVal[0]][eleVal[1]][eleVal[2]]
        except:
            ret = ''
        return ret
    elif len(eleVal) == 4:
        try:
            ret = jsons[eleVal[0]][eleVal[1]][eleVal[2]][eleVal[3]]
        except:
            ret = ''
        return ret

keyVal = get_element(jsons, 'meta_data', 'hash_value')
```

### 5.4. JSON データを整形して出力

```python
import pprint

# dict 型の JSON データを整形して出力する。
# 改行コードが値に含まれているとおかしなことになるため注意
pprint.pprint(dictJsonData)
```

## 6. Pandas データフレームの取扱

### 6.1. JSON 文字列ファイルをデータフレームに変換

- 読み込む JSON 文字列は、ダブルクォーテーションでキー名・値が囲まれているもの。

```python
import pandas

with open('file.json', mode='r') as r:
    data = pandas.read_json(r)
```

### 6.2. dict 型データをデータフレームに変換

- `pandas.DataFrame()`: キーをカラム名（最上行）に使用
- `pandas.DataFrame.from_dict()`: キーをインデックス名（最左列）に使用

```python
import pandas

dictA = { 'apple': 3,
 'banana': 5,
 'mango': 7,
 }

data = pandas.DataFrame(dictA, index='Index0')
#        apple  banana  mango
#Index0      3       5      7

data = pandas.DataFrame.from_dict(dictA, orient='index')
#          Quantity
# apple    3
# banana   5
# mango    7
```

## 7. BeautifulSoup によるスクレイピング

### 7.1. 基本的なデータ取得とパース

```python
import requests
from bs4 import BeautifulSoup as bs

pageData = request.get('https://google.com')
soupData = bs(pageData.text, 'html.parser')
```

### 7.2. ローカルの HTML ファイルを読み込む場合

```python
from bs4 import BeautifulSoup as bs

f = open('file.html', mode='r')
pageData = f.read()
f.close()
soupData = bs(pageData, 'html.parser')
```

### 7.3. 各要素の取得

```html
[sample.html]

<html>
  <title>Sample HTML</title>
  <body>
    <h1>H1 tag</h1>
    <h1 class="h1class">H1 tag with class</h1>
    <h2>
      <a href="https://google.com">URL link 1</a><br />
      <a href="https://microsoft.com">URL link 2</a><br />
    </h2>
  </body>
</html>
```

```python
result = soupData.select('h1')  # H1 タグのデータを取得。結果はリストデータ
# <h1>H1 tag</h1>
# <h1 class="h1class">H1 tag with class</h1>

result = soupData.select('h1')[0].text  # H1 タグのテキスト部分のみ抽出
# H1 tag

result = soupData.select('h1.h1class') # h1class というクラス名の H1 タグを抽出
# <h1>H1 tag</h1>

result = soupData.select('h2 > a') # H2 タグの子要素から a タグを抽出
# <a href="https://google.com">URL link 1</a>
# <a href="https://microsoft.com">URL link 2</a>

result = soupData.select('h2 > a')[0].get('href') # a タグの href 要素を抽出
# https:/google.com
```

## 8. 文字列データの取り扱い

### 8.1. 文字列への変換

```python
# 強制的に文字列へ変換
word = str(arg)

# Byte型の変換（b'文字列'と表示されるヤツ）
word = strings.decode()

# Unicode エスケープされたバイト列の変換
b = b'\\u3042\\u3044\\u3046\\u3048\\u304a'
print(b.decode('unicode-escape'))
# あいうえお

# \x00 を含むバイト列の変換
print(byteString.decode('utf-8').replace('\x00', ''))
```

### 8.2. フォーマット文字列

複数の形式（str と int 等）が混在する文字列を生成したい場合などに使用

```python
word = 'files'
numb = 6

# ％構文による場合
print('There are %s %s in the directory.' % (numb, name))
# There are 6 files in the directory.

# ｆ文字列による場合
print(f'There are {numbs} {word} in the directory.')
# There are 6 files in the directory.
```

### 8.3. 文字列入力

```python
import getpass

str = input('Please input strings: ')  # 文字列を普通に入力する場合
pass = getpass.getpass('Please input password: '  # 入力文字を画面に表示したくない場合
```

### 8.4. 文字列の分割

```python
line = 'abc,def,ghi'

varStr = line.split(',')
# セパレータを引数として指定
# 指定しない場合は空白文字を使用。
# 空白文字にはスペースや改行\n, タブ\t が適用される。
```

### 8.5. 文字列の置換

```python
# replace 関数による場合
strings = 'abcdif'
res = (strings.replace('i', 'e')
print(res)
# abcdef


# 正規表現による場合
strings = '[text] 報告について.txt'
res = re.sub('\[.*] ', '', strings)
print(res)
# 報告について.txt
```

### 8.6. 文字列の先頭／末尾の削除

```python
strings = 'abcdefg'

# 先頭１文字を除いて表示
print(strings[1:]) # 'bcdefg'

# 末尾２文字を除いて表示
print(strings[:-2]) # 'abcdef'

# 先頭２文字と末尾１文字を除いて表示
print(strings[2:-1]) # 'cdef'
```

## 9. 数値データの取り扱い

### 9.1. 割り算の商と余り

```python
nums = 13

syo = nums // 2
ama = nums % 2
print('%s, $S' % (syo, ama))
# 6, 1
```

### 9.2. 文字列を使って計算

- `eval`関数は、与えられた文字列を Python コードとして評価・実行する。
- **脆弱性の原因となる為、ユーザからの任意文字列は絶対に渡さない事**

```python
strings = '12 + 5'
result = eval(strings)
# result == 17
```

## 10. 正規表現モジュールによるパターンマッチング検索

`match()`や`search()`を使用し、
正規表現によって文字列をパターンマッチングさせた場合、
マッチングオブジェクトが返されるため、通常とは異なる処理が必要となる。

### 10.1. 文字列を検索して含まれるかどうかを判定

```python
string = 'Hello world!'
matObj = re.search(r'Hello (.*)')

if matObj is None:
    print('Not match')
else:
    print('Matched')
```

### 10.2. マッチした文字列を取得

```python
string = 'Hello world/!'
matObj = re.search(r'Hello (.*)(!/?)')
# Hello の後に『何かが０以上続き』その後に『！又は？が来る』場合の検索

if matObj is None:
    print('Not match')
else:
    print(matObj.group(0))  # マッチした文字列全て：Hello World!
    print(matObj.group(1))  # 正規表現部分でマッチした文字列１：World
    print(matObj.group(2))  # 正規表現部分でマッチした文字列２：!
```

### 10.3. 文字列が完全一致するかどうかを判定

例えば、メールアドレスの判定などに使用できる。

```python
address = 'testmail@example.com'

matObj = re.fullmatch(r'/^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/')
```

### 10.4. メールアドレスの正規表現

```python
matObj = re.search(r'/^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/')
```

### 10.5. URL の正規表現

```python
matchObj = re.search(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+')
```

### 10.6. ドメイン名の正規表現

```python
matchObj = re.search(r'/^([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*\.)+[a-zA-Z]{2,}$/')
```

### 10.7. IP アドレスの正規表現

```python
matchObj = re.search(r'/^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$/')
```

### 10.8. 各ハッシュ値の正規表現

```python
# MD5
matchObj = re.search(r'/^[a-f0-9]{32}$/')

# SHA-1
matchObj = re.search(r'/b[0-9a-f]{5,40}/')

# SHA-256
matchObj = re.search(r'/\b[A-Fa-f0-9]{64}\b/')
```

### 10.9. SSH フィンガープリントの正規表現

```python
matchObj = re.search(r'/[a-f0-9]*\:[a-f0-9]*\:[a-f0-9]*\:[a-f0-9]*\:[a-f0-9]*\:[a-f0-9]*\:[a-f0-9]*\:[a-f0-9]*\:[a-f0-9]*\:[a-f0-9]*\:[a-f0-9]*\:[a-f0-9]*\:[a-f0-9]*\:[a-f0-9]*\:[a-f0-9]*\:[a-f0-9]*/')
```

## 11. リストデータの取扱

### 11.1. 要素を末尾に追加

```python
listA = ['apple', 'banana']

listA.append('cherry')
```

### 11.2. リストやタプルを末尾に結合

str 型を結合すると、すべての文字が一文字ずつリストで追加されるので注意

```python
listA = ['apple', 'banana']
listB = ['cherry', 'Diamond']

listA.extend(listB)
```

### 11.3. リストの要素を削除

全削除する場合：`clear()`

```python
listA = ['apple', 'banana', 'cherry']

listA.clear()
```

指定した位置の要素を削除する場合：`pop()`

```python
listA = ['apple', 'banana', 'cherry']

# 整数の場合、先頭からの要素数
# 負数の場合、末尾からの要素数（末尾は -1）
# 引数を与えない場合は末尾の要素を削除

res = listA.pop(1)
print(res)
# res => banana
# listA => ['apple', 'cherry']

res = listA.pop(-1)
# res => cherry
```

指定した値と同じ要素を検索し、最初の要素を削除する場合：`remove()`

```python
listA = ['apple', 'banana', 'cherry']

listA.remove('cherry')
# listA => ['apple', 'banana']
```

指定した値と同じ要素を全て削除する場合：リスト内包表記

```python
listA = ['apple', 'apple', 'banana', 'banana', 'cherry', 'cherry']

res = [i for i in listA if i != 'cherry']
# res => ['banana', 'banana', 'cherry', 'cherry']
```

### 11.4. リストの重複を削除

`set`で重複の削除された set オブジェクトを取得、リスト化する。

```python
listA = ['apple', 'apple', 'banana', 'banana']

listB = list(set(listA))
```

### 11.5. リストの中身をソート

- `sorted`: ソートした値を返す。
- `sort`: 元のリストをソートしてしまう。返り値は none 。

```python
listA = ['Cherry', 'apple', 'Diamond', 'banana']

listB = sorted(listA)
listB = sorted(listA, reverse=True)  # 逆順ソート

listA.sort()
listA.sort(reverse=True)  # 逆順ソート
```

### 11.6. リストの任意の回数で処理を変える

```python
listA = ['Cherry', 'apple', 'Diamond', 'banana']

i = len(listA)  # i = 4

# ４番目の `banana` だけ表示
for fruit in listA:
    if i == 1:
        print(fruit)
    i -= 1
```

## 12. ファイル等の操作全般

### 12.1. ファイルの存在確認

```python
import os

# ファイルの存在を確認し、存在すれば削除
if os.path.isfile('file.txt'):
    os.remove('file.txt')
```

### 12.2. フォルダ内のファイル・フォルダ一覧を取得

```python
import glob

fileList = glob.glob('./image/*')
print(fileList)
# ["img/01.jpg", "img/02.jpg", "img/Old"]

# サブフォルダ内も再起的に取得する場合
fileList = glob.glob('./img/*', recursive=True)
print(fileList)
# ["img/01.jpg", "img/02.jpg", "img/Old", "img/Old/03.jpg]
```

### 12.3. ファイルの作成、削除、リネーム

```python
# 空ファイルの作成
with open("test.txt","w"):pass

# ファイルの削除
import os
os.remove('file.txt')

# ファイルのリネーム
import os
os.rename('fileA.txt', 'fileB.txt')
```

### 12.4. フォルダの作成・削除

```python
import os

os.makedirs('directory/path')
os.makedirs('directory/path', exist_ok=True)  # 既存でもエラーを返さない。

import shutil

shutil.rmtree('directory/path', )
```

### 12.5. ファイルの読み込み

```python
# システムの文字環境とファイルのエンコードが異なる場合は、エンコードを指定
with open('filename.txt', mode='r', encoding='UTF-8') as f:
    data = f.read()  # ファイルデータ全体を文字列として格納
    data = f.read(20)  # 読み込む最大文字数を指定可能

    # ファイルを行ごとに最終行まで読み込み
    for line in f:
        print(line)
```

### 12.6. ファイルへのデータ書き込み

```python
# データを単純に書き込み（追記モード）。最後は改行する。
def add_2_file(arg, fileName):
    with open(fileName, mode='a') as f:
        print(arg, file=f)

# データを書き込み、最後に改行させない。
def add_2_file_no_nl(arg, fileName):
    with open(fileName, mode='a') as f:
        print(arg, file=f, end='')  # 最後の改行文字を空白にする。

# pprint を使って dict 型 JSON を書き出し。
# 改行コード入りデータの場合、おかしな事になるため注意
# なお、シングルクォーテーションで書き出される為、書き出したファイルは
# そのままでは JSON ファイルとして読み込めない。
import pprint

def output_2_file(arg, fileName):
    with open(fileName, mode='a') as f:
        pprint.pprint(arg, stream=f)
```

## 13. Zip ファイルの取り扱い

### 13.1. フォルダの Zip 圧縮

```python
# shutil ライブラリの場合
import shutil

shutil.make_archive('path/to/new_zip_name', 'zip', 'target_directory')
```

### 13.2. パスワード付き Zip 圧縮

```python
import subprocess

subprocess.run(['zip', '-e', f'--password=P@sswordd', '-r', 'path/to/zipfile.zip', 'target_directory'])
```

### 13.3. ファイル名を Shift-JIS 文字コードに変換してから圧縮

- Windows10 標準の Zip 解答や Lhaca 等を使用した場合の文字化けに対応する。
- 『Shift-JIS に変換 => 圧縮 => UTF-8 に戻す』を行う。
- UTF-8 に戻さない場合、ファイルの取り扱いが困難になるため注意

必要なパッケージ：'convmv'

```bash
sudo apt install convmv
```

```python
import subprocess

# ./tmp_dir の中にある全てのファイルのファイル名を変換、圧縮、再変換
subprocess.run(f'convmv -r -f utf8 -t sjis --notest tmp_dir/*', shell=True, stdout=subprocess.DEVNULL)
subprocess.run(f'zip -r tmp.zip tmp_dir')
subprocess.run(f'convmv -r -f sjis -t utf8 --notest tmp_dir/*', shell=True, stdout=subprocess.DEVNULL)
```

## 14. OS コマンドの実行（Linux）

### 14.1. OS コマンドを実行

```python
import subprocess

subprocess.run('ls')
subprocess.run(['ls', '-l'])  # 引数を与える場合
subprocess.run(['echo', 'morning coffee'])  # 引数が "morning coffee" の場合
subprocess.run('sudo apt update && sudo apt upgrade -y', shell=True)  # 文字列をそのままコマンドにしたい場合
```

### 14.2. 出力の受取り

```python
import subprocess

# コマンド実行結果を標準出力しつつ、その後で結果を利用する場合
result = subprocess.run(['which', 'bash'])
print(result.stdout)  # コマンド実行結果の標準出力（string）
print(result.returncode)  # コマンド実行の終了コード（正常終了：０、異常終了：１など）

# コマンド実行結果を表示させない場合
stdOut = subprocess.run(['which', 'bash'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

# コマンド実行の標準出力を devnull に捨てて、結果のみを得たい場合
retCode = subprocess.run(['which', 'bash'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
print(retCode.returncode)  # リターンコードは残される。
```

### 14.3. コマンド実行結果を変数に格納

```python
import subprocess

subprocess.check_output(['ls', '-l'])
```

## 15. エラー処理

```python
try:
  print('Try!')
  print(varA)
except:
  print('...and Error!')
```

## 16. 日付データの取り扱い

### 16.1. 日付形式のデータ生成

```python
from datetime import date

varDate = date(2020, 2, 3)
print(varDate)
# 2020-02-03
```

### 16.2. 日時形式のデータ生成

```python
from datetime import datetime

varDate = datetime(2020, 2, 3, 15, 45)
print(varDate)
# 2020-02-03 15:45:00
```

### 16.3. 現在の日、時間を取得

```python
import datetime

varDate = datetime.date.today()
# 2020-02-03
varDate = datatime.datetime.now()
# 2020-02-03 15:45:00
dayOnly = datetime.datetime.now().strftime(%d)
# 03
```

### 16.4. 日付の差分計算

```python
from datetime import date

date1 = date(2022, 1, 31)
date2 = date(2022, 5, 12)
print(date2 - date1)
# 101 days, 0:00:00
```

### 16.5. 年、月、日単位の日付計算

```bash
pip install python-dateutil
```

```python
from datetime import date
from dateutil.relativedelta import relativedelta

varDate = date(2020, 1, 2)
result = varDate + relativedelta(years=1, months=2, days=3)
print(result)
# 2021-3-5
result = varDate + relativedelta(year=1, month=2, day=3)
print(result)
# 0001-2-3  複数形にしない場合、その数値が直接指定される。
```

### 16.6. UNIX タイムスタンプを日付形式で変換

```python
from datetime import datetime
from datetime import timezone

uniTime = 1636437881
varDate = datetime.datetime.fromtimestamp(uniTime)
varDate = datetime.datetime.fromtimestamp(uniTime, timezone.utc)  # タイムゾーン指定
varDate = datetime.datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d-%H-%M-%S')  # 形式指定
# 2021-10-20-11-10-53
```

## 17. その他の小技

### 17.1. おまじない

```python
if __name__ == '__main__':
```

### 17.2. 引数処理（引数の数確認と値の受領）

```python
import sys

args = sys.argv

# 引数が２つ必要な場合のエラー処理
if len(args) <= 2 or len(args) >= 4:
    print('** 引数エラー **')
    print("JSONファイル名とアクターのIDリストファイルに2つの引数が必要です。")
    print('ex) python create_summary_by_file.py result.json idList.text')
else:
    jsonFileName = args[1]
    idList = args[2]
    print('Start script.')
```

### 17.3. if 文を一行で記述

```python
exit('[!] Eixt.') if var == 0 else None
result = 'Success!' if var > 1 else 'Failed...'
result = 'Success!' if var > 10 else  var < 10 'Failed...'
```

### 17.4. for 文の連番をスマートに記述

```python
listA = ['a', 'b', 'c']

for i, x in enumerate(listA, start=1)
    print(f'No.{i}  {x})
# No.1  a
# No.2  b
# No.3  c
```

### 17.5. 英文字列の検索

検索文字列を比較する際は、大文字又は小文字に揃えると比較が容易

- `lower()`: すべての文字を小文字に変換する。
- `upper()`: すべての文字を大文字に変換する。(upper メソッド)
- `capitalize()`: 最初の文字を大文字にして他は小文字に変換する。(capitalize メソッド)
- `title()`: 文字列に含まれる単語毎に最初の文字を大文字に他は小文字に変換する。(title メソッド)
- `swapcase()`: 大文字を小文字に、小文字を大文字に変換する。(swapcase メソッド)

```python
wordA = 'Diamond'
wordB = 'DIAMOND'

if wordA.lower() == wordB.lower():
    print('It matched!')
else:
    print('No matched!')
```

### 17.6. 型判定

型によって処理を変えたい場合に使用

- 型一覧
  - `str`,`int`, `float`, `dict`, `tuple`, `list`, `bool`

```python
varA = {'key': 'value'}
if isinstance(varA, dict):  # varA が辞書型かどうかを判定
    for x in varA:
        print('%s: %s' % (x, varA[x]))
```

### 17.7. YES / NO 実行確認

```python
message = "Start script. OK? ('yes' or 'no' [y/n]): "

def yes_no_input(message):
    while True:
        choice = input(message).lower()
        if choice in ['y', 'ye', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
```

### 17.8. 入力のループ

```python
message = 'Input number (1 ~ 3)'

def input_loop(message):
    while True:
        nums = input(message)
        if nums == 1:
            return 1
        elif nums == 2:
            return 2
        elif nums == 3:
            return 3
```

### 17.9. プログラムの中途終了

```python
import sys

res = input('Start? (yes or no)')

if res == no:
  sys.exit(1)  # 引数１は、終了時のリターンコード。未指定の場合は０

sys.exit('Script has shutdown.')  # メッセージを表示させて終了させる場合
```

### 17.10. ログファイルに書き出しつつ標準出力に表示

```python
def write_logs(arg, logFileName):
    with open(logFileName, mode='a') as f:
        print(arg, file=f)
        print(arg)
```

### 17.11. ファイルの先頭行に挿入

```python
# ファイル全体を読み込み後、先頭行を加えてから残りの行を書き出し。
def insert_first_line(fileName, firstLine):
    with open(fileName) as f:
        lines = f.readlines()

    with open(fileName, mode='w') as f:
        print(firstLine + '\n', file=f)
        f.writelines([item for item in lines])
```

### 17.12. ファイルの最終行を削除

```python
# ファイル全体を読み込んで、最終行を除く行を書き出し。
def delete_last_line(fileName):
    with open(fileName) as f:
        lines = f.readlines()

    with open(fileName, mode='w') as f:
        f.writelines([item for item in lines[:-1]])
```
