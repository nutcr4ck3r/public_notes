---
tags:
  - Bash
  - 覚書
---

# Bash 例文集

## 1. 変数の取り扱い

### 1.1. 変数の宣言と代入

```bash
# = の周辺にスペースを入れてはならない。
val=5
val="6"
```

### 1.2. 変数の値の参照

```bash
valA="Hello"
valB="Bob"

echo "$valA"
# Hello

echo "$valA$valB"
# HelloBob

# 変数名が他の文字列とくっついてしまう場合は｛｝で囲む。
echo "${valA} ${valB}by"
# Hello Bobby
```

## 2. 文字列に対する操作

### 2.1. コマンド実行結果を変数に格納

```bash
res=$(git status)
```

### 2.2. コマンド実行の終了ステータスを確認

```bash
# 直前のコマンドの実行結果は $? に格納されている。
# 慣例として、正常終了は０、異常終了は１以上の数値となる。
res=$(git status)
echo $?

# 複数のコマンドの終了ステータスで条件判別する場合は && を使用する。
# 正常終了した場合のみ次のコマンドが実行されるため、
# ここのコマンドの結果判別を省略できる。
git status && git pull
if ....
```

### 2.3. 文字列入力を待ち受けて変数に格納

```bash
printf "Input strings: "
read -r res
printf "Your input strings is $res\n"
```

### 2.4. フォーマット文字列

```bash
printf "Hello %s\n" "Bob!"
# Hello Bob!
# printf は最後に改行が入らないので注意

printf "Hello %s and %s!" "Alice" "Bob"
# Hello Alice and Bob!
```

### 2.5. 文字列のフォント色と背景色の変更

`\e[ <CODE>`と`\e[m`でフォントカラーなどを変更したい文字列を囲む。

```bash
# 背景を緑表示
printf "\e[42m%s\033[m\n" "GREEN back"

# フォントを赤表示
printf "\e[0;31m%s\033[m\n" "AKA font"
```

複数の効果を付与したい場合は、セミコロンでコードを区切って記述（順不同）

```bash
# 青背景；太字；赤文字
\e[44;1;31
```

```text
# デコレーション
#  \e[0  全ての効果をオフ
#  \e[1  太字
#  \e[4  下線
#  \e[5  点滅
#  \e[7  色の反転


# フォントカラー
#  \e[0;30   Black          \e[1;30   Dark Gray
#  \e[0;34   Blue           \e[1;34   Light Blue
#  \e[0;32   Green          \e[1;32   Light Green
#  \e[0;36   Cyan           \e[1;36   Light Cyan
#  \e[0;31   Red            \e[1;31   Light Red
#  \e[0;35   Purple         \e[1;35   Light Purple
#  \e[0;33   Brown          \e[1;33   Yellow
#  \e[0;37   Light Gray     \e[1;37   White
#  \e[       Default color


# バックグラウンドカラー
#  \e[40   Black
#  \e[41   Red
#  \e[42   Green
#  \e[43   Yellow
#  \e[44   Blue
#  \e[45   Magenta
#  \e[46   Cyan
#  \e[47   White
```

以下をスクリプト内に記述することで、変数名で簡単に指定できる。

```bash
# Color values
# e.g) printf "$foRed%s$foDef" "Red font color"
atOff="\e[0m"
atBold="\e[1m"
atUnder="\e[4m"
atBlink="\e[5m"
atReverse="\e[7m"

foDef="\e[m"
foRed="\e[0;31m"
foLRed="\e[1;31m"
foBlue="\e[0;34m"
foLBlue="\e[1;34m"
foYellow="\e[1;33m"
foGreen="\e[0;32m"
foLGreen="\e[1;32m"
foWhite="\e[1;37m"
foBlack="\e[0;30m"
foCyan="\e[0;36m"
foLCyan="\e[1;36m"
foPurple="\e[0;35m"
foLPurple="\e[1;35m"
foLGray="\e[0;37m"
foDGray="\e[1;30m"
foBrown="\e[0;33m"

bgBlack="\e[40m"
bgRed="\e[41m"
bgGreen="\e[42m"
bgYellow="\e[43m"
bgBlue="\e[44m"
bgMagenta="\e[45m"
bgCyan="\e[46m"
bgWhite="\e[47m"
```

## 3. 判定による条件分岐

### 3.1. 条件式の記述

```bash
val=5

# 基本形
if [[ $val == 5 ]]; then
  echo "Match"
fi

# if/else
if [[ $val == 5 ]]; then
  echo "Match"
else
  echo "Not match"
fi

# if/elif
if [[ $val == 5 ]]; then
  echo "Match: 5"
elif [[ $val == 3 ]]; then
  echo "Match: 3"
else
  echo "Not match"
fi
```

### 3.2. 条件式の演算子

```bash
val=5

# 等しいかどうか
if [[ $val == 5 ]]; then
  echo "Match"
fi
if [[ $val -eq 5 ]]; then
  echo "Match"
fi

# 等しくないかどうか
if [[ $val != 5 ]]; then
  echo "Match"
fi
if [[ $val -ne 5 ]]; then
  echo "Match"
fi

# より大きい
if [[ $val > 0 ]]; then
  echo "Match"
fi
if [[ $val -gt 0 ]]; then
  echo "Match"
fi

# 以上
if [[ $val >= 0 ]]; then
  echo "Match"
fi
if [[ $val -ge 0 ]]; then
  echo "Match"
fi

# より小さい
if [[ $val < 6 ]]; then
  echo "Match"
fi
if [[ $val -lt 6 ]]; then
  echo "Match"
fi

# 以下
if [[ $val <= 6 ]]; then
  echo "Match"
fi
if [[ $val -le 6 ]]; then
  echo "Match"
fi
```

### 3.3. 特定のファイルやディレクトリが存在するかどうかを判定する場合

```bash
# test の有無を判定（ファイルやディレクトリの区別なし）
if [ -e ./test ]; then
  echo "[*] Path is Existed."
fi

# App.js ファイルの有無を判定
if [ -f ./App.js ]; then
  echo "[*] File is Existed."
fi

# .git ディレクトリの有無を判定
if [ -d ./.git ]; then
  echo "[*] Directory is Existed."
fi

# test リンクの有無を判定
if [ -L ./test ]; then
  echo "[*] Link is Existed."
fi
```

### 3.4. ファイルの属性を判定する場合

```bash
# ファイルが読み取り可能かどうかを判定
if [ -r ./test.txt ]; then
  echo "[*] File is writable."
fi

# ファイルが書き込み可能かどうかを判定
if [ -w ./test.txt ]; then
  echo "[*] File is writable."
fi

# ファイルが実行可能かどうかを判定
if [ -x ./test.txt ]; then
  echo "[*] File is executable."
fi
```

### 3.5. ファイルが空ファイルかどうかを判定する場合

```bash
if [ ! -s ./test.txt ]; then
  echo "[!] File is empty!"
else
  echo "[*] File is not empty."
fi
```

### 3.6. コマンド実行結果に特定文字列が含まれているかどうかを判定する場合

```bash
comStr="$(git status)"

if [[ "$comStr" == *behind* ]]; then
  printf "[!] New commits on remote.\n"
fi
```

## 4. その他の小技

### 4.1. 先頭に絶対あるアレ

```bash
#!/bin/bash
```

### 4.2. YES / NO 判定

```bash
printf "[?] Execute a command? [y/n:default (n)] : "
read -r res
if [ "$res" = "y" ] || [ "$res" = "Y" ] || \
[ "$res" = "yes" ] || [ "$res" = "YES" ]; then
    echo "[*] Command Execute!!!"
fi
```
