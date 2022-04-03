---
tags:
  - Javascript
  - 覚書
---

# Javascript 例文集

## 1. 関数の表現方法

### 1.1. 基本的な関数の表記方法

以下の３つは、どの表記法を用いても同じ結果を得ることができる。

```javascript
// 基本的な関数表記
function log_output(arg, val) {
  console.log(arg)
  console.log(val)
}

// 関数リテラル表記
const log_output = function(arg, val) {
  console.log(arg)
  console.log(val)
}

// アロー関数表記
const log_output = (arg, val) => {
  console.log(arg)
  console.log(val)
}
```

### 1.2. 一部を省略した表記方法

```javascript
// 引数が一つなら（）を省略可、引数が無い場合は省略不可
const log_output = arg => {console.log(arg)}

// 実行部分が式なら｛｝を省略可
const log_output = arg => console.log(arg)
const log_output = arg => return arg * 2  // これは文なので省略不可

// 式の場合は return 省略可
const log_output = (arg, val) => arg + val
```

## 2. 条件分岐（if）

### 2.1. 単一条件の判定（if...else）

```javascript
const a = 1

if (a > 0) {
  console.log('a is bigger than 0.')
}
else {
  console.log('else')
}
```

### 2.2. 複数条件の判定（else if）

```javascript
const a = 1

if (a == 0) {
  console.log('a = 0')
}
else if (a == 1) {
  console.log('a = 1')
}
```

### 2.3. AND / OR / NOT 条件式

```javascript
// AND 式
if (a > 0 && a < 5) {
  console.log('Matched!')
}

// OR 式
if (a == 0 || a == 5) {
  console.log('Matched!')
}

// NOT 式
if (!a == 0) {
  console.log('Matched!')
}
```

### 2.4. 単一処理の場合の省略形

```javascript
if (a == 0) console.log('Mathced!')
```

## 3. 条件分岐（switch）

### 3.1. Switch 式による条件分岐

```javascript
const value = 1

switch (value) {
  case 1:
    console.log('1')
    break
  case 2:
    console.log('2')
    break
  case 3:
    console.log('3')
    break
  default:  // いずれの条件にも合致しなかった場合
    console.log('No match.')
}
```

### 3.2. 複数のケースに同じ処理をさせる場合

```javascript
const value = 1

switch (value) {
  case 1:
  case 2:
  case 3:
    console.log('1, 2 or 3')
    break
  default:
    console.log('No match.')
}
```

## 4. 繰り返し処理（for）

### 4.1. 回数を指定した繰り返し

```javascript
for(let i = 0; i < 5; i++) {
  console.log(i)
}
// 実行結果
// 0
// 1
// 2
// 3
```

### 4.2. 配列・オブジェクトを利用した繰り返し

配列の繰り返し（`lengsth`又は`for~of`）

```javascript
const fruits = ['apple', 'banana', 'cherry'];

// 配列の長さを使用する場合
for(let i = 0; i < fruits.length; i++) {
  console.log(fruits[i])
}
// 実行結果
// apple
// banana
// cherry

// for ~ of 構文
for(let x of fruits) {
  console.log(x)
}
// 実行結果
// apple
// banana
// cherry
```

オブジェクトの繰り返し（`for~in`又は`forEach`）

```javascript
// for ~ in 構文
// この構文は配列に使用しない。オブジェクトに使用する。
const fruitsObj = [name: 'apple', number: 10, color: 'red'];

for(let x in fruitsObj) {
  console.log(x)
  console.log(fruitsObj[x])
};
// 実行結果
// name
// apple
// number
// 10
// color
// red

// forEach の場合は、Object.keys で全キーの配列を作成後、
// forEach でループ処理を実行する。
Object.keys(fruitsObj).forEach((key) => {
  console.log(`キー: ${key} , 値: ${fruitsObj[key]}`)
});
// 実行結果
// キー: name , 値: apple
// キー: number , 値: 10
// キー: color , 値: red
```

## 5. エラー処理

```javascript
try {
  await response = fetch('https://sample.com/')
}
catch (e) {
  console.log('Error!')
  console.log(e.message)
  // エラーオブジェクトの message プロパティにエラーメッセージが格納されている。
}
```

## 6. HTML 要素の操作

### 6.1. 要素の値を取得・設定

```javascript
<div id="idName">test</div>
<a id="linkA" href="google.com">link to Google</a>

// 値の取得
data = document.getElementById("idName")
// 結果＝ <div id="idName">test</div>

// HTML タグの中身だけ取得
data = document.getElementById("idName").innerHTML
// 結果＝ test

// a タグの href 要素の値を取得
data = document.getElementById("linkA")
hrefStr = data.a
// 結果＝ google.com

// 要素の値を変更
document.getElementById("idName").innerHTML = "Strings have changed."
// 結果＝ <div id="idName">Strings have cahnged.</div>
```

## 7. 時間を指定した実行処理

### 7.1. setInterval 関数（定期実行）

停止する必要が無い場合の使用方法

```javascript
let count = 0

function count_up() {
  console.log(count++)
}

// 第１引数：処理、第２引数：実行間隔（ミリ秒）
setInterval(count_up, 1000)
```

停止する必要がある場合の使用方法

```javascript
let count = 0

const count_up = () => {
  console.log(count++)
  if (count > 10) {
    clearInterval(intervalId)
  }
}

const intervalId = setInterval(count_up, 1000)
```

### 7.2. setTimeout 関数（ｘ秒後に実行）

```javascript
function logOutput() {
  console.log("test")
}

setTimeout(logOutput, 5000)
```

## 8. 日付処理

### 8.1. 現在日時の取得

```javascript
// Unix タイムスタンプ形式（int型）の取得
const date = Date.now()  // 1646801950226

// 可読性のある形式（str型）での取得
const date = Date()  // 'Wed Mar 09 2022 14:01:16 GMT+0900 (Japan Standard Time)'

// date オブジェクトの生成
const date = new Date()
```

### 8.2. UNIX タイムスタンプの変換

必要ライブラリ：`date-fns`

```bash
npm install date-fns
```

```javascript
import format from 'date-fns/format'

const createdDate = 1585574700000

function convert_date() => {
  return (
    format(createdDate, 'yyyy.MM.dd HH:mm')
  )
}
```

## 9. 数字の取り扱い

### 9.1. 文字列を数値に変換

```javascript
const numStr = '123'
let res = 0

res = Number(numStr)
// res : int => 123
```

## 10. 文字列の操作

### 10.1. 数字を文字列に変換

```javascript
const num = 123
let res = ''

res = num.toString()
// res : str => '123'
```

### 10.2. テンプレートリテラル

文字列をバッククォートで囲むことにより、
変数を展開したり、改行をそのまま反映したり、式を展開したりできる。

展開したい部分は`${name}`の形で記述する。

```javascript
const strings = 'JS'

console.log(`Hello, ${strings}`)
console.log(`How are you?
I'm fine!`)
console.log(`1 + 2 = ${1+2}`)
```

### 10.3. 数字をカンマで３桁区切り表示

```javascript
const number = 1234567

console.log(number.toLocaleString())
// 1,234,567

// React Native など、上記関数が正常に動作しない場合の力技
console.log(number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ","))
```

## 11. 配列の取り扱い

### 11.1. 配列の定義

```javascript
const arr = [1, 2, 3]
```

### 11.2. 配列のソート

- `sort()`関数は、デフォルト使用の場合、数字も文字列としてソートする。
- 文字と数字が混在する場合、『数位 > ローマ字 > 日本語』の順でソートする。
- 返り値は存在せず、適用した配列が直接ソートされる。

```javascript
const arr = [29, 100, 12]
arr.sort()  // arr => [100.12.29]
```

数値をソートしたい場合は`sort()`に関数の引数を与える。

```javascript
// 昇順
array.sort(
  function(a,b) {
    if (a > b) retrrn 1
    else if (a < b) return -1
    else return 0
  })

// 降順
array.sort(
  function(a,b) {
    if (a < b) return 1
    else if (a > b) return -1
    else return 0
  })
```

### 11.3. 配列の先頭を削除

```javascript
const arr = [1, 2, 3]
const res = arr.shift()
// arr = [2, 3]
// res = [1]
```

### 11.4. 配列の末尾を削除

```javascript
const arr = [1, 2, 3]
const res = arr.pop()
// arr = [1, 2]
// res = [3]
```

### 11.5. 指定した要素の削除

```javascript
const arr = [1, 2, 3]
const res = arr.splice(1,2)  // １番目から２個の要素を削除
// arr = [1]
// res = [2, 3]
```

### 11.6. 指定した要素の置換

```javascript
const arr = [1, 2, 3]
const res = arr.splice(1,2,0)  // １番目から２個の要素を０に置換
// arr = [1]
// res = [2, 3]

// 指定した条件のデータを削除
const arr = ['apple', 'banana', 'cherry', 'donky']
const filter = ['apple', 'cherry']
const res = arr.filter((val) => {
  return ! filter.includes(val)})
```

## 12. JSON の取り扱い

### 12.1. JSON 文字列の生成

キーと値を含む javascript オブジェクトを JSON 文字列に変換する。

```javascript
const dicObj = {
  a: 1,
  b: 'String'
  c: [1, 2, 3]
  d: {
    'A': 1,
    'B': 2,
  }
}

console.log(JSON.stringify(dicObj))
console.log(JSON.stringify(dicObj,undefined,1))  // 1 は
:width: ,
// 結果
{"a":1,"b":"String","c":[1,2,3,4],"d":{"A":1,"B":2}}

{
 "a": 1,
 "b": "String",
 "c": [
  1,
  2,
  3,
  4
 ],
 "d": {
  "A": 1,
  "B": 2
 }
}
```

### 12.2. JSON 文字列から javascript オブジェクト（JSON）の生成

- JSON 文字列を受取り、キーと値を含むオブジェクト（JSON）に変換する。
- 検索や値の取得をする為には、この行程を踏む必要がある。
- `fetch`などで取得した`Response`オブジェクトから javascript オブジェクトを得る場合は
別途他の方法がある事に注意

```javascript
const fromJson = JSON.parse(jsonString)
```

### 12.3. JSON のソート

昇順のソート

```javascript
let jsonData = JSON.parse(data)
jsonData.sort(function(a,b){
    if(a.property > b.property) return 1  // property には、ソートのキーにしたい
    if(a.property< b.property) return -1  // JSON 内のキー名を指定する。
    return 0
 })
```

降順のソート

```javascript
let jsonData = JSON.parse(data)
jsonData.sort(function(a,b){
    if(a.property > b.property) return -1
    if(a.property< b.property) return 1
    return 0
 })
```

### 12.4. 値の取得

```javascript
// ドット演算子記法
console.log(jsonData.name)

// ブラケット演算子記法
console.log(jsonData['name'])

// ブラケット演算子なら、キー名に変数を使用可能
const arg = 'name'
console.log(jsonData[arg])
```

## 13. API 問い合わせ

### 13.1. 基本的な HTTP リクエスト

- `fetch`により GET リクエストを送信、レスポンスオブジェクトを得る。
- レスポンスオブジェクトの持つ`json`メソッドを使用する。
- 最終的には javascript オブジェクトを得ることが出来る。

※`fetch`が返す物は`promise`である。
このため、正常にレスポンスオブジェクトを得るには、
`.then()`を使用するか、`await fetch()`のように実行する必要がある。

```javascript
// .then() を使用する場合
function get_api_response() {
  fetch('https://sample.com/api/test')
    .then((res) => {     // res => レスポンスオブジェクト
      return res.json()  // レスポンスを JSON として評価し、javascript オブジェクトに変換
    })
    .then((jsonData) => {
      console.log(jsonData)
      return jsonData
    })
}

// async/await を使用する場合
async function get_api_response() {
  const resObj = await fetch('https://sample.com/api/test')
  const jsonData = await resObj.json()

  console.log(jsonData)
  return jsonData
}
```

### 13.2. クエリパラメータを付与してリクエストを送信

```javascript
const url = 'https://sample.com/api/test'
const params = {a: xxxx, b: yyyy, c: zzzz}
const queryParams = new URLSearchParams(params)

const res = await fetch(url)
```

### 13.3. ヘッダを付与してリクエストを送信

```javascript
const url = 'https://sample.com/api/test'

// ベタ打ちする場合
await fetch(url, {
  headers: {
    Authorization: 'Basic' + btoa('username' + ':' + 'password'),
    Accept: 'application/json', 'Content-Type': 'application/json;charset=utf-8'
  }
})

// headers オブジェクトを渡す場合
let headers = new Headers()
headers.set({
    Authorization: 'Basic' + btoa('username' + ':' + 'password'),
    Accept: 'application/json', 'Content-Type': 'application/json;charset=utf-8'
  })

await fetch(url, { headers })
```

### 13.4. POST リクエストの送信

```javascript
const url = 'https://sample.com/api/test'

await fetch(url, {
  method: 'POST',
  body: data
})

// JSON 形式で送る場合
await fetch(url, {
  method: 'POST',
  body: JSON.stringify(data)
})

```

## 14. VSCode でデバッグする手順

1. 拡張機能`Live Server`をインストール
2. ステータスバーから`Go Live`をクリックし、ローカルサーバを起動
3. デバッグから`Launch Chrome against localhost`を選択して実行
