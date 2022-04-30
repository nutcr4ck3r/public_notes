---
tags:
  - MySQL
  - DB
  - 覚書
---

# MySQL 覚書

## 1. 主キー・外部キーの関係性の整理

### 1.1. 主キー

1. 当該テーブルにおいて一意の値でなければならない。（UNIQUE）
2. 主キーとして指定されていなければならない。（PRIMARY KEY）
3. 主キーのフィールドには NULL を含んではならない。（NOT NULL）
4. 複数の列を組み合わせて、複合キーとして使用することができる。
5. 別のテーブルから参照される際は、主キーが使用される。（REFERENCES）

### 1.2. 外部キー

1. 当該テーブル（A）の任意フィールドの値を別のテーブル（B）の値に紐づける事ができる。
2. テーブルＡに外部キーとして設定する値は、テーブルＢの主キーである必要がある。
3. テーブルＢに存在しない主キー値をテーブルＡで扱う事はできない。

## 2. データベースで扱うデータタイプ

### 2.1. 文字列型のデータタイプ一覧

| データ型   | タイプ               | 最大サイズ              |
| ---------- | -------------------- | ----------------------- |
| CHAR       | 固定長文字列         | 255 バイト              |
| VARCHAR    | 可変長文字列         | 255 バイト              |
| TYNYTEXT   | 可変長バイナリデータ | 255 バイト              |
| TINYBLOB   | 可変長バイナリデータ | 255 バイト              |
| TEXT       | 可変長バイナリデータ | 65535 バイト (65KB)     |
| BLOB       | 可変長バイナリデータ | 65535 バイト (65KB)     |
| MEDIUMTEXT | 可変長バイナリデータ | 16777215 バイト (16MB)  |
| MEDIUMBLOB | 可変長バイナリデータ | 16777215 バイト (16MB)  |
| LONGTEXT   | 可変長バイナリデータ | 4294967295 バイト (4GB) |
| LONGBLOB   | 可変長バイナリデータ | 4294967295 バイト (4GB) |
| ENUM       | リスト               | 65535 個                |
| SET        | リスト               | 64 個                   |

### 2.2. 数値型のデータタイプ一覧

| データ型  | SIGEND 指定時サイズ                       | UNSIGNED 指定時サイズ                          |
| --------- | ----------------------------------------- | ---------------------------------------------- |
| TYNYINT   | -128〜127                                 | 0〜255                                         |
| BIT       | TYNYINT(1) の別名                         | TYNYINT(1) の別名                              |
| BOOL      | TYNYINT(1) の別名                         | TYNYINT(1) の別名                              |
| BOOLEAN   | TYNYINT(1) の別名                         | TYNYINT(1) の別名                              |
| SMALLINT  | -32768〜32767                             | 0〜65535                                       |
| MEDIUMINT | -8388608〜8388607                         | 0〜16777215                                    |
| INT       | -2147483648〜2147483647                   | 0〜4294967295                                  |
| INTEGER   | INT の別名                                | INT の別名                                     |
| BIGINT    | -9223372036854775808〜9223372036854775807 | 0〜18446744073709551615                        |
| FLOAT     | 単精度浮動小数点                          | 単精度浮動小数点（負数を除く）                 |
| DOUBLE    | 倍精度浮動小数点                          | 倍精度浮動小数点（負数を除く）                 |
| REAL      | DOUBLE の別名                             | DOUBLE の別名                                  |
| DECIMAL   | 桁数と小数桁数を指定できる数値型          | 桁数と小数桁数を指定できる数値型（負数を除く） |
| DEC       | DECIMAL の別名                            | DECIMAL の別名                                 |
| NUMERIC   | DECIMAL の別名                            | DECIMAL の別名                                 |
| FIXED     | DECIMAL の別名                            | DECIMAL の別名                                 |

### 2.3. 日付型のデータタイプ一覧

| データ型  | タイプ | 形式                | 範囲                                     |
| --------- | ------ | ------------------- | ---------------------------------------- |
| DATE      | 日付型 | YYYY-MM-DD          | 10000-01-01〜9999-12-31                  |
| DATETIME  | 日付型 | YYYY-MM-DD HH:MM:SS | 1000-01-01 00:00:00〜9999-12-31 23:59:59 |
| TIMESTAMP | 日付型 | YYYY-MM-DD HH:MM:SS | 1970-01-01 00:00:00〜2037                |
| TIME      | 時刻型 | HH:MM:SS            | -838:59:59〜838:59:59                    |
| YEAR      | 年     | YYYY 又は YY        | YYYY=1901〜2155、YY=70〜69（1970〜2069） |

## 3. コメントの形式

```sql
# 行コメント

-- 行コメント

/* ブロックコメント
   （改行も含む） */
```

## 4. 練習用サーバの起動・接続

### 4.1. mysql-client のインストール

ターミナルから MySQL サーバに接続するために必要

```bash
# for macOS
brew install mysql-client

# for Linux (ex.Ubuntu)
sudo apt install mysql-client

mysql --version
echo "export PATH=${PATH}:/usr/local/opt/mysql-client/bin" >> ~/.zshrc
source ~/.zshrc
```

### 4.2. 練習用サーバの起動

GitHub に公開されているデータを利用して、サンプルデータ入りのサーバを作成

```bash
git clone git@github.com:not13/mysql_with_phpmyadmin.git
cd mysql_with_phpmyadmin.git
docker-compose up -d
```

### 4.3. 練習用サーバへの接続

```bash
mysql -uroot -p -h127.0.0.1
password: root
```

## 5. データベース操作

### 5.1. データベース一覧の確認

```sql
SHOW DATABASES;

+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sakila             |
| sys                |
+--------------------+
5 rows in set (0.01 sec)
```

### 5.2. データベースの作成・削除

```sql
-- 作成
CREATE DATABASE databaseName;

-- 削除
DROP DATABASE databaseName;
```

### 5.3. 操作するデータベースの選択

```sql
USE databaseName
```

## 6. テーブル作成時の操作

### 6.1. テーブル一覧の確認

```sql
-- 現在操作中のデータベースで確認する場合
SHOW TABLES;

-- データベースを指定して確認する場合
SHOW TABLES FROM databaseName;

+----------------------------+
| Tables_in_sakila           |
+----------------------------+
| actor                      |
| actor_info                 |
| store                      |
+----------------------------+
3 rows in set (0.00 sec)
```

### 6.2. テーブルのフィールド一覧の確認

```sql
SHOW FIELDS FROM tableName;
+------------------+-------------------+------+-----+-------------------+-----------------------------------------------+
| Field            | Type              | Null | Key | Default           | Extra                                         |
+------------------+-------------------+------+-----+-------------------+-----------------------------------------------+
| store_id         | tinyint unsigned  | NO   | PRI | NULL              | auto_increment                                |
| manager_staff_id | tinyint unsigned  | NO   | UNI | NULL              |                                               |
| address_id       | smallint unsigned | NO   | MUL | NULL              |                                               |
| last_update      | timestamp         | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |
+------------------+-------------------+------+-----+-------------------+-----------------------------------------------+
4 rows in set (0.01 sec)
```

### 6.3. テーブルの作成・削除

```sql
-- 作成
CREATE TABLE tableName (
  fieldNmae1 dataType1,
  fieldNmae2 dataType2,
  fieldNmae3 dataType3,
);

-- 削除
DROP TABLE tableName;
```

### 6.4. テーブル作成時に設定できる定義

```sql
-- NULL の入力を不許可にする。
CREATE TABLE tableName (
  fieldNmae1 dataType1 NOT NULL,
);

-- フィールドの値を一意にし、重複を不許可にする。
CREATE TABLE tableName (
  fieldNmae1 dataType1 UNIQUE,
);

-- デフォルト値を設定する。
CREATE TABLE tableName (
  fieldNmae1 dataType1 DEFAULT value1,
);

-- インクリメントを設定する。
-- 値は整数値、
CREATE TABLE tableName (
  fieldNmae1 dataType1 PRIMARY KEY AUTO_INCREMENT,
);

-- インデックスを作成する。
CREATE TABLE tableName (
  fieldNmae1 dataType1,
  INDEX indexName(fieldName1, fieldName2)
);

-- 主キーを設定する。
-- 直接指定
CREATE TABLE tableName (
  fieldNmae1 dataType1 NOT NULL PRMARY KEY,
);
-- PRIMARY KEY オプション
CREATE TABLE tableName (
  fieldNmae1 dataType1 NOT NULL,
  PRIMARY KEY(fieldName1, fieldName2)
);

-- 外部キーを設定する。
-- 直接指定
CREATE TABLE tableName1 (
  fieldNmae1 dataType1 NOT NULL REFERENCES
    tableaName2(fieldName2),
);
-- FOREIGN KEY オプション
CREATE TABLE tableName1 (
  fieldNmae1 dataType1 NOT NULL,
  FOREIGN KEY(fieldName1) REFERENCES
    tableaName2(fieldName2)
);
```

### 6.5. テンポラリテーブルの作成・削除

- テンポラリテーブルは、データベースとの接続が切れると同時に削除される。
- テンポラリテーブルは、作成したユーザしか参照することができない。

```sql
-- 作成
CREATE TEMPORARY TABLE tableName (
  fieldNmae1 dataType1,
  fieldNmae2 dataType2,
  fieldNmae3 dataType3,
);

-- 削除
DROP EMPORARY TABLE tableName;
```

## 7. 既存テーブルの操作

### 7.1. 主キー・外部キーの設定・削除

```sql
-- 主キーの設定
-- CONSTRAINT keyName は省略可能。省略した場合は PRIMARY となる。
ALTER TABLE tableName ADD CONSTRAINT keyName
  PRIMARY KEY(fieldName1, fieldName2);

-- 外部キーの設定
-- CONSTRAINT keyName は省略可能。省略した場合は fieldName1 と同じになる。
ALTER TABLE tableName ADD CONSTRAINT keyName
  FOREIGN KEY(fieldName1) REFERENCES
    tableName2(fieldName2);

-- キーの削除
-- 主キー又は外部キーを削除
ALTER TABLE tableName DROP CONSTRAINT keyName
-- テーブルから主キーを削除
ALTER TABLE tableName DROP PRIMARY KEY
```

### 7.2. インデックスの設定

```sql
-- CREATE INDEX による方法
CREATE INDEX indexName
  ON tableName(fieldName1, fieldName2);

-- ALTER TABLE による方法
ALTER TABLE tableName
  ADD INDEX indexName(fieldName1, fieldName2);
```

### 7.3. フィールドの追加・削除

```sql
-- 追加
ALTER TABLE tableName
  ADD fieldName dataType;

-- 削除
ALTER TABLE tableName
  DROP COLUMN fieldName;
```

## 8. データの取得

### 8.1. 使用できる演算子等の一覧

算術演算子

| 記号 | 意味               | 使用例 | 結果       |
| ---- | ------------------ | ------ | ---------- |
| +    | 加算               | 1+2    | 3          |
| -    | 減算               | 3-2    | 1          |
| \*   | 乗算               | 2\*3   | 6          |
| /    | 除算               | 10/3   | 3.33333... |
| DIV  | 除算（整数部のみ） | 10/3   | 3          |
| %    | 剰余               | 10/3   | 1          |

比較演算子

| 演算子 | 意味                | 使用例      | 使用例の表す条件                   |
| ------ | ------------------- | ----------- | ---------------------------------- |
| =      | 等しい              | code = 10   | code が 10 と等しい                |
| <=>    | 等しい（NULL 対応） | code <=> 10 | code が 10 と等しい（NULL を含む） |
| !=     | 等しくない          | code != 10  | code が 10 と等しくない            |
| <>     | 等しくない          | code <> 10  | code が 10 と等しくない            |
| >      | より大きい          | code > 10   | code は 10 より大きい              |
| >=     | 以上                | code >= 10  | code は 10 以上                    |
| <      | 未満                | code < 10   | code は 10 未満                    |
| <=     | 以下                | code <= 10  | code は 10 以下                    |

論理演算子

| 記号 | 意味         | 使用例   |
| ---- | ------------ | -------- |
| NOT  | 否定         | NOT 条件 |
| !    | 否定         | ! 条件   |
| AND  | 論理積       | X AND Y  |
| &&   | 論理積       | X && Y   |
| OR   | 論理和       | X OR Y   |
| \|\| | 論理和       | X \|\| Y |
| XOR  | 排他的論理和 | X XOR Y  |

### 8.2. 基本的なデータ取得

```sql
-- 全てのフィールドのデータを取得
SELECT
  *
FROM tableName;

-- 特定のフィールドのデータを取得
SELECT
  first_name,
  last_name,
  birthday
FROM tableName;

-- フィールド名を別名で表示
SELECT
  first_name AS 姓,
  last_name AS 名,
  birthday AS 誕生日
FROM tableName;
```

### 8.3. 完全一致による絞り込み

```sql
SELECT *
FROM tableName
WHERE full_name = '鈴木一郎';
```

### 8.4. 曖昧検索による絞り込み

ワイルドカードとして扱う部分を`%`で指定する。

```sql
SELECT *
FROM tableName
WHERE full_name LIKE '鈴木%';
```

### 8.5. 重複するデータを除いた絞り込み

```sql
SELECT DISTINCT(dpt_code)
FROM tbl_employee
```

### 8.6. 複数条件による絞り込み

```sql
-- AND 条件
-- 全ての条件に合致するエントリーを絞り込み
SELECT *
FROM tableName
WHERE (dpt_code = 10) AND (post_code = 4);

-- OR 条件
-- いずれかの条件に合致するエントリーを絞り込み
SELECT *
FROM tableName
WHERE (dpt_code = 10) OR (post_code = 4);

-- IN 条件
-- 指定フィールドの値がいずれかのエントリーを絞り込み
SELECT *
FROM tableName
WHERE dpt_code IN (10, 20, 50);

-- NOT IN 条件
-- 指定フィールドの値がいずれでもないエントリーを絞り込み
SELECT *
FROM tableName
WHERE dpt_code NOT IN (40, 60);
```

### 8.7. NULL の判定

```sql
-- NULL のエントリーを絞り込み
SELECT *
FROM tableName
WHERE full_name IS NULL;

-- NULL のエントリーを除外
SELECT *
FROM tableName
WHERE full_name IS NOT NULL;
```

### 8.8. 値の範囲指定

```sql
-- ADN 演算子で指定する場合
SELECT *
FROM tableName
WHERE (post_code >= 10) ADN (post_code <= 90);

-- BETWEEN 演算子で指定する場合
SELECT *
FROM tableName
WHERE post_code BETWEEN 10 AND 90;
```

### 8.9. 絞り込み結果の並び替え

NULL は、MySQL において最小の値として扱われるため、
昇順で並び替えると最上段に並ぶ。

```sql
-- 昇順（ASC は省略可能）
SELECT *
FROM tableName
WHERE post_code BETWEEN 10 AND 90
ORDER BY code ASC;

-- 高順
SELECT *
FROM tableName
WHERE post_code BETWEEN 10 AND 90
ORDER BY code DESC;

-- ２つ以上のフィールドで並び替える場合
-- 先に指定したフィールドほど並び替えが優先される。
SELECT *
FROM tableName
WHERE post_code BETWEEN 10 AND 90
ORDER BY
  dpt_code ASC,
  code DESC;
```

### 8.10. 抽出された値を別名で表示

`CASE`句を使用し、指定フィールドの特定値を別名で表示する。

```sql
-- WHEN ~ THEN は複数を指定可能
SELECT
  code AS 社員コード,
  name AS 社員名,
  CASE dpt_code
    WHEN 10 THEN 'Yes'
    ELSE 'No'
  END AS 総務部
FROM tableName;

-- 演算子を使用する場合
SELECT
  code AS 社員コード,
  name AS 社員名,
  CASE
    WHEN dpt_code = 10 THEN 'Yes'
    ELSE 'No'
  END AS 総務部
FROM tableName;
```

結果

```text
社員コード  社員名    総務部
--------------------------
101         鈴木一郎  Yes
102         山田次郎  No
103         佐藤三郎  No
```

＝以外の演算子を使用する場合

### 8.11. 複数のテーブルを結合してデータを取得

- ポイント
  - FROM 句のテーブルは複数指定できる。
  - `テーブル名．フィールド名`の形式でテーブル・フィールド名を一括指定
  - WHERE 句でテーブルを等結合

```sql
-- tbl_employee
code  name      dpt_code
--------------------------
101   鈴木一郎  10
102   山田次郎  20
103   佐藤三郎  30

-- tbl_department
code  name
--------------------------
10    総務部
20    営業部
30    開発部
```

```sql
SELECT
  tbl_department.code AS dpt_code,
  dtl_department.name AS dpt_name,
  tbl_employee.code AS emp_code,
  tbl_employee.name AS emp_name
FROM
  tbl_employee,
  tbl_department
WHERE
  tbl_employee.dpt_code = tbl_department.code;

-- 結果
-- ＝の左で指定した値をキーとして、右に指定したフィールドの値を参照する。
dpt_code  dpt_name  emp_code  emp_name
----------------------------------------
10        総務部    101       鈴木一郎
20        営業部    102       山田次郎
30        開発部    103       佐藤三郎
```

### 8.12. 複数のクエリ結果を参照して表示

UNION: 複数のクエリ結果を結合表示

```sql
SELECT * FROM BLUE
UNION
SELECT * FROM RED;
```

UNION ALL: 複数のクエリ結果を結合表示（重複表示を許可）

```sql
SELECT * FROM BLUE
UNION ALL
SELECT * FROM RED;
```

INTERSECT: 複数のクエリ結果から、重複するものだけを表示

```sql
SELECT * FROM BLUE
INTERSECT
SELECT * FROM RED;
```

EXCEPT: 複数のクエリ結果から、後に指定された結果を除く

```sql
-- BLUEにのみ存在する結果を表示
SELECT * FROM BLUE
EXCEPT
SELECT * FROM RED;
```

## 9. データの追加・編集

### 9.1. 値を直接指定してテーブルへデータを追加

```sql
INSERT INTO tablename (
  code,
  name,
  dpt_code
)
VALUES (
  101,
  '山田太郎',
  20
);

-- テーブル内の全てのフィールドを埋めるようにデータを追加する場合、
-- フィールド名は省略できる。
INSERT INTO tablename
VALUES (
  101,
  '山田太郎',
  20
);
```

### 9.2. 別のテーブルからデータを追加

```sql
-- フィールドを直接指定して追加する場合
INSERT INTO tbl_dpt_emp (
  dpt_code,
  dpt_name,
  emp_code,
  emp_name
)
  SELECT
    dpt.code,
    dpt.name,
    emp.code,
    emp.name
  FROM
    tbl_employee AS emp,
    tbl_department AS dpt
  WHERE
    emp.dpt_code = dpt.code;

-- フィールド指定しない場合、追加先テーブル列の並び順の通りにデータが追加される。
INSERT INTO tbl_dpt_emp
  SELECT
    dpt.code,
    dpt.name,
    emp.code,
    emp.name
  FROM
    tbl_employee AS emp,
    tbl_department AS dpt
  WHERE
    emp.dpt_code = dpt.code;
```

### 9.3. 既存データを更新

```sql
UPDATE
  tbl_employee
SET
  dpt_code = 30,
  birthday = '1983-03-03'
WHERE
  code = 103;
```

### 9.4. 既存データの削除

```sql
DELETE
FROM
  tbl_employee
WHERE
  code = 103;
```

## 10. 代表的な関数

### 10.1. 文字列を左／右から指定数分だけ取得

```sql
LEFT(stringValue, number)  -- 左から
RIGHT(stringValue, number)  -- 右から
```

```sql
-- name フィールドの左から２文字文を取得
SELECT
  LEFT(name, 2)
FROM
  tbl_employee
WHERE
  code = 101;
```

### 10.2. 大文字／小文字に変換

```sql
SELECT LOWER(stringValue)
SELECT UPPER(stringValue)
```

### 10.3. 値の左右に含まれる空白を削除

```sql
TRIM(stringValue)
LTRIM(stringValue)
RTRIM(stringValue)
```

```sql
-- 名前の左右に含まれてしまった空白を削除する場合
SELECT
  TRIM(name)
FROM
  tbl_employee;

-- 名前の左に含まれてしまった空白を削除する場合
SELECT
  LTRIM(name)
FROM
  tbl_employee;
```

### 10.4. 文字列の長さを計る

```sql
LENGTH(stringValue)
```

```sql
SELECT
  LENGTH(name)
FROM
  tbl_employee
WHERE
  code = 102;  -- '山田太郎'

-- 結果 4
```

### 10.5. 文字列を補填する

```sql
-- 補填対象文字列、何文字まで補填するか、補填に使用する文字は
-- 補填に使用する文字を省略した場合は、半角空白が適用される。
LPAD(stringValue, number, character)
```

```sql
SELECT
  code,
  LPAD(name, 10, '*')
FROM
  tbl_employee;

-- 結果
code  name
--------------
101   ******鈴木一郎
102   ******山田次郎
103   ******佐藤三郎
```

### 10.6. 文字列を置換して抽出

```sql
-- 操作対象文字列、置換前の文字列、置換後の文字列
REPLACE(stringValue, character1, character2)
```

```sql
SELECT
  code,
  REPLACE(name, '太郎', '次郎')
FROM
  tbl_employee;
```

### 10.7. 文字列の部分抽出

```sql
-- 操作対象文字列、抽出開始位置、抽出文字数
SUBSTRING(stringValue, startPosition, length)
```

```sql
SELECT
  code,
  SUBSTRING(name, 2, 3)
FROM
  tbl_employee
WHERE
  code = 101;  -- name = 山田太郎

-- 結果 = '田太郎'
```

### 10.8. 計算（剰余、切り捨て、切り上げ）

```sql
-- 剰余
MOD(value1, value2)

-- 数値の四捨五入：四捨五入される数、四捨五入する桁
ROUND(value, digit)

-- 切り捨て：切り捨てされる数、切り捨てする桁
TRUNCATE(value, digit)
```

```sql
-- 剰余（結果：1）
SELECT MOD(5, 2)

-- 下２桁を基準に四捨五入（結果：123.46）
SELECT ROUND(123.456, 2);
-- 上２桁を基準に四捨五入（結果：100）
SELECT ROUND(123.456, -2);

-- 下２桁を基準に切り捨て（結果：123.45）
SELECT TRUNCATE(123.456, 2);
-- 上２桁を基準に切り上げ（結果：100）
SELECT TRUNCATE(123.456, -2);

-- 切り上げは、四捨五入と 0.05 を加える計算を組み合わせる。
SELECT ROUND( (1.32 + 0.05), 1)
```

### 10.9. 現在の日付・時刻を得る

```sql
-- 現在の日付：2020-12-04
CURRENT_DATE()

-- 現在の時刻：11:33:54
CURRENT_TIME()

-- 現在の日時：2020-12-04 11:33:54
CURRENT_TIMESTAMP()
```

### 10.10. レコードの件数を取得

```sql
COUNT(fieldName)
```

```sql
-- tbl_employee テーブルの全レコード件数を取得
SELECT
  COUNT(*)
FROM
  tbl_employee;

-- dpt_code の数（重複を除く）を取得：結果＝3
SELECT
  COUNT(DISTINCT(dpt_code))
FROM
  tbl_employee;
```

### 10.11. 平均値を取得する

```sql
AVG(fieldName)
```

```sql
-- 年齢の平均値を取得
SELECT
  AVG(age)
FROM
  tbl_employee;
```

### 10.12. 最大値・最小値・合計値を取得

```sql
MAX(fieldName)
MIN(fieldName)
SUM(fieldName)
```

```sql
-- 年齢の最大値
SELECT
  MAX(age)
FROM
  tbl_employee;

-- 年齢の最小値
SELECT
  MIN(age)
FROM
  tbl_employee;

-- 年齢の合計値
SELECT
  SUM(age)
FROM
  tbl_employee;
```

### 10.13. 値のデータタイプを変換

```sql
-- 変換対象の値、変換後のデータタイプ
CAST(value AS dataType)
```

```sql
-- 文字列型を日付型へ
CAST('2020-12-01' AS DATE)

-- 数値型を文字列型へ
CAST(12.345 AS CHAR)
```

## 11. ビューの作成

ビューを作成することで、何度も SELECT 文でフィールドを並べ替える必要がなくなる。

```sql
CREATE VIEW viewName (
  fieldName1,
  fieldName2
) AS
  selectStatement;
```

```sql
-- tbl_post テーブルから code, name フィールド、
-- tbl_employee テーブルから code, name フィールド を選択し、
-- post_code, post_name, emp_code, emp_name として表示。
CREATE VIEW v_post_list (
  post_code,
  post_name,
  emp_code,
  emp_name
) AS
  SELECT
    post.code,
    post.nmae,
    emp.code,
    emp.name
  FROM
    tbl_post AS post,
    tbl_employee AS emp
  WHERE
    post.code = emp.post_code;
```
