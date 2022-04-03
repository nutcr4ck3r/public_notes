---
tags:
  - Python
---

PythonのWindows実行体をデコンパイルする方法

# EXE => .pyc

`.pyc`ファイルは、実行体から生成されるC-Pythonのバイナリファイル。  
生のバイナリではなく、　`marshal`モジュールでシリアライズされている。  
内部にはPythonの命令がバイナリ形式で含まれている。

## .pyc 生成

`python-exe-unpacker`を使用し、アンパックする。  
実行する環境は、実行体がコンパイルされたPythonバージョンに合わせることが望ましい。

https://github.com/countercept/python-exe-unpacker

アンパックされたファイルは、コマンド実行パスに作成されたフォルダに全て出力される。

## .pyc 特定

アンパックされたファイルの中には`XXXXX.exe.manifest`が存在する。  
（`XXXXX`はコンパイルする前のPythonファイル名となっている）  
``XXXXX`をアンパックされたファイルの中から探し出し、`XXXXX.pyc`に拡張子を変更する。

# .pyc => .py

`python-exe-unpacker`で生成された`.pyc`ファイルは、Pythonバージョンを含むヘッダ情報16バイトが欠落している。  
デコンパイルするためには、コンパイルされたPythonバージョンのヘッダ情報が必須となるため、修正する。

## ヘッダ情報生成

最も簡単な方法は、目的とするバージョンのPython環境で適当な`.py`ファイルを作成し、そこから`.pyc`ファイルを生成すること。  
`.py`ファイルの中身は何でもよい。`print('hello')`のみでもOK

```
$ python -m py_compile .\tekitou.py
```

## ヘッダ情報編集

生成した`.pyc`ファイルなどから得られたヘッダ情報を、`XXXXX.pyc`に移植する。  
この際、欠落した16バイトを追加する必要があるため、Linuxのバイナリエディタ "hexeditor" を`-b`オプションで使用するなどして先頭に16バイト分を追加できるようにする。

```
例：Python 3.7.2 の場合

0x00～0x01	バージョンのマジックナンバー  "0x42 0x0D"
0x02～0x03	固定値 "0x0D 0x0A"
0x04～0x0F	ゼロで埋める
```

## デコンパイル

`uncompyle6`を使用してデコンパイルする。  
デコンパイル結果は標準出力される。

https://github.com/rocky/python-uncompyle6/

# もしもデコンパイルが上手くいかない場合は

現状（2020.09.24時点）、Python 3.8^ のバージョンでコンパイルされたデータは`.pyc`からのデコンパイルが失敗する。  
よって、低レベル命令語にディスアセンブルし、そこから手動でデコンパイルする必要がある。

## ディスアセンブル

以下のスクリプトを`dis.py`として保存した後、`python disassemble.py XXXXX.pyc`で実行する。  
これは、Python標準モジュールの`marshal`モジュールでデシリアライズしたデータを、同じく標準モジュールである`dis`を使用してディスアセンブルするもの。  
低レベル命令語ではあるものの、丁寧に読めばコードを把握することができる。  
＊何故かFlareVM環境だと正常に動作しなかった。Kali環境だと正常動作する。

```
import sys
import dis
import marshal

# Useful header constant from https://stackoverflow.com/questions/32562163/how-can-i-understand-a-pyc-file-content
header_sizes = [
    # (size, first version this applies to)
    # pyc files were introduced in 0.9.2 way, way back in June 1991.
    (8,  (0, 9, 2)),  # 2 bytes magic number, \r\n, 4 bytes UNIX timestamp
    (12, (3, 6)),     # added 4 bytes file size
    # bytes 4-8 are flags, meaning of 9-16 depends on what flags are set
    # bit 0 not set: 9-12 timestamp, 13-16 file size
    # bit 0 set: 9-16 file hash (SipHash-2-4, k0 = 4 bytes of the file, k1 = 0)
    (16, (3, 7)),     # inserted 4 bytes bit flag field at 4-8 
    # future version may add more bytes still, at which point we can extend
    # this table. It is correct for Python versions up to 3.9
]
header_size = next(s for s, v in reversed(header_sizes) if sys.version_info >= v)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(f'Usage: python {sys.argv[0]} pycfile')
        sys.exit(1)

    pycfile = sys.argv[1]
    with open(pycfile, "rb") as f:
        metadata = f.read(header_size)
        code = marshal.load(f)

    dis.dis(code)
```

## ディスアセンブルされたコードの読み方一例

python インタプリタは内部にシンプルな stack マシン(VM) を持っている。  
python インタプリタがスクリプトを実行する際、内部では以下の工程がスクリプトが停止するまで繰り返し続けられている。

1. bytecode を一命令読み込む
2. 読み込んだ bytecode に基づいて stack 上の値の読み書きや計算を行い、 stack を更新する

### （例）以下のスクリプトをコンパイルした際の bytecode

使用した python のバージョンは 3.8.2

```python
[add.py]
a = 1
b = a + 3
print(b)
```

disassemble 結果

```
  1           0 LOAD_CONST               0 (1)
              2 STORE_NAME               0 (a)

  2           4 LOAD_NAME                0 (a)
              6 LOAD_CONST               1 (3)
              8 BINARY_ADD
             10 STORE_NAME               1 (b)

  3          12 LOAD_NAME                2 (print)
             14 LOAD_NAME                1 (b)
             16 CALL_FUNCTION            1
             18 POP_TOP
             20 LOAD_CONST               2 (None)
             22 RETURN_VALUE
```

- disassemble 結果の一番左に書かれている数字は元のスクリプトファイルの行数
- 中央あたりに書かれている `LOAD_CONST` などの文字列は bytecode の命令
- 各命令の左隣に書かれている数字は bytecode のオフセット（配列の番号のようなもの）
- 右側に書かれている数字は命令に渡すオペランド(引数)

### １行目：a=1

```
  1           0 LOAD_CONST               0 (1)
              2 STORE_NAME               0 (a)
```

まずはスクリプトの一行目にある `a = 1` に対応する命令を確認  
一番左に書かれている数値がスクリプトの行番号に対応するので、 `a = 1` は `LOAD_CONST` と `STORE_NAME` という二つの命令で構成されていることがわかる。

`LOAD_CONST` は stack にオペランドとなっている定数値を push する命令。 オペランドには 0 が渡されているが、これは pyc ファイル内に定義された定数一つ一つに付けられた通し番号を表している。 この定数一覧は上記の disassemble.py 内で `code.co_consts` にアクセスすることで以下のように確認できる。

```python
>>> code.co_consts
(1, 3, None)    #配列のような形で値が格納されている。
```

ここから、定数リストの 0 番目に格納されている値は 1 であることがわかる。  
これは disassemble 結果のオペランドの右に括弧つきで書かれている値と一致する。  
この括弧つきの値は、定数が通し番号で表示されているとわかりづらいため、 `dis` パッケージが定数の実際の値を書き込んでくれていたもの。

よって、この `LOAD_CONST` 命令では 1 を stack 上に push することになる。  
＊`LOAD`＝stack に値を push

```
[co_const]
[0] 1    <= この値を、
[1] 3

[stack]
[0] 1    <= stack に push（LOAD_CONST）
```

次の `STORE_NAME` 命令は stack から値を pop してオペランドにある *名前* に格納する命令。  
名前とは、 python のオブジェクトを参照するために利用する識別子で、定数と同じように通し番号が付けられている。  
名前一覧は `code.co_names` で参照が可能。

```python
>>> code.co_names
('a', 'b', 'print')
```

また、括弧内に書かれている `a` は、名前番号の 0 番に割り当てられているのが `a` であることを示している。  

つまり、この `STORE_NAME` 命令では `a` という名前に pop した値を格納する (紐づける) という操作をしている。  
＊`STORE`＝stack の値を pop して格納

```
[stack]
[0] 1    <= この stack の値を、

[co_name]
[0] a = 1    <= この名前（a）に格納（STORE_NAME）
[1] b
[2] print
```

### 2 行目：b=a+3

```
  2           4 LOAD_NAME                0 (a)
              6 LOAD_CONST               1 (3)
              8 BINARY_ADD
             10 STORE_NAME               1 (b)
```
ここでは、始めに `LOAD_NAME`, `LOAD_CONST` によって `a` (に紐づいた値である `1` ) と `3` を stack に push している。

```
[co_name]
[0] a = 1    <= この名前（a）に格納された値（1）を push（LOAD_NAME）

[co_const]
[0] 1
[1] 3    <= この値を push（LOAD_CONST）

[stack]
[0] (a=)1    <= push された値
[1] 3    <= push された値
```

次の `BINARY_ADD` は stack から値を 2 つ pop して加算をした後、その結果を push する命令。  
これで、 stack には `a + 3` の結果が積まれることになる。  
それを次の `STORE_NAME` で `b` に格納、つまり `b = a + 3` という操作となる。

```
[stack]
[0] (a=)1    <= これと、
[1] 3    <= これを、pop して加算、結果を push（BINARY_ADD）

[stack]
[0] 4    <= push された値、これを pop して、

[co_name]
[0] a = 1
[1] b = 4    <= ここに格納（STORE_NAME）
```

### ３行目：print(b)

```
  3          12 LOAD_NAME                2 (print)
             14 LOAD_NAME                1 (b)
             16 CALL_FUNCTION            1
             18 POP_TOP
             20 LOAD_CONST               2 (None)
             22 RETURN_VALUE
```

`LOAD_xxx` で `print` と `b` の順で値を push。 その後、 `CALL_FUNCTION 1` という命令が出てくる。  
この命令は、まず stack の一番上 (TOS: Top Of Stack) からオペランドで指定された数だけ値を pop した後に stack 上の一番上に残った関数オブジェクトを pop する。  
そして、 pop した関数オブジェクトをその前に pop した値を引数として呼び出し、その結果を push する。

今回は `CALL_FUNCTION` のオペランドに 1 が指定されているので、 TOS から値を一つ、つまり `b` を pop する。  
次に stack 上に残っている `print` を関数オブジェクトとみなし、 `print(b)` を実行し、その返り値である None を stack に push する。  
しかし、今回は返り値を使用していないため、直後の `POP_TOP` で返り値を捨てている。

```
[co_name]
[0] a=1
[1] b=4    <= LOAD_NAME
[2] print    <= LOAD_NAME

[stack]
[0] print    <= 関数名として pop（CALL_FUNCTION）
[1] 4    <= TOS. 引数として pop（CALL_FUNCTION 1）
```

ここまででスクリプトに対応する処理はすべて完了したため、最後にこのスクリプト自体の返り値 (None) を push し、 `RETURN_VALUE` でスクリプトの実行が終了する。

## Python VM 命令一覧

公式ドキュメント：https://docs.python.org/ja/3/library/dis.html#python-bytecode-instructions