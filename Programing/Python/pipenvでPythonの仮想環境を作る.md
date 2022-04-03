---
tags:
  - Python
---

# pipenvでPythonの仮想環境を作る

venvに比べてキッチリ整理するのに向く。（気がする）

## インストール

- 必要なツールのインストール

```bash
sudo apt install pipenv
sudo apt install virtualenv # 無いと言われた場合
```

## 仮想環境の作成

- 最終的な仮想環境関連ファイルは以下の通り。

```text
/test-project  " 仮想環境のルートディレクトリ
┣ /.venv  " 仮想環境のインストールパッケージ等
┃    ┣ /bin
┃    ┣ /include
┃    ┗ /lib
┣ Pipfile  " インストールパッケージリスト、スクリプト等が記載
┣ Pipfile.lock  " インストールパッケージのバージョン管理
┗ python.py  " 作成したPythonコード
```

- プロジェクトディレクトリを作成

```bash
mkdir test-project
cd test-project
```

- 仮想環境を作成

```bash
mkdir .venv          "仮想環境保存ディレクトリ。デフォルト位置でいいならスキップ。
pipenv --python 3    "python3.xの現バージョンで作成される。
pipenv --python 3.6  "指定したバージョンで作成される。
pipenv --venv        "仮想環境のパス。.venvを作成していない場合に。
```

## 仮想環境のカスタマイズ

- 使用するパッケージのインストール
  - リストファイルを配布・再利用することで同一環境を構築できる。

```bash
pipenv install numpy  "numpyをインストールする場合の例。Pipfileに記述される。
```

- 開発用パッケージを別枠でインストール
  - 開発用パッケージは別リストで管理・配布したい場合に。

```bash
pipenv install --dev flake8  "Pipfileのdev-packagesに記述される。
```

- 別環境にインストールパッケージを再現
  - 開発用に同一環境を配布する場合などに。

```bash
pipenv install        "プロジェクトディレクトリのPipfileを基に再現
pipenv install --dev  "開発用パッケージもインストールする場合
pipenv sync           "Pipfile.lockを基に、バージョンも完全に同じ状態で再現
pipenv sync --dev     "Pipfile.lockを基に、開発用パッケージも完全再現
```

### 仮想環境の実行

- インストールパッケージの確認

```bash
pipenv graph
```

- 仮想環境でpythonファイルを実行
  - 単一のファイルをテストする場合。実行・終了に時間がかかる。

```bash
pipenv run python test.py
```

- 仮想環境のシェルに入る。
  - 連続でインタラクティブに環境を使用する場合。

```bash
pipenv shell  "プロンプトの頭に仮想環境名が付く。
exit  "仮想環境を抜ける。
```

## その他のTips

- スクリプトの登録と実行
  - `Pipfile`に記述することでエイリアス機能に似たスクリプトを実行可能

```bash
 [scripts]
 start = "python main.py runserver"
 test = "python -m unittest discover -v"

pipenv run start
```

- プログラム実行時の自動読み込みファイル（.env）
  - `.env`に記述された内容は自動的に読み込まれる。
  - ローカルテスト環境ゆえの設定やハードコーディングできない内容などに。

```url
www.unclessxz.com
```
