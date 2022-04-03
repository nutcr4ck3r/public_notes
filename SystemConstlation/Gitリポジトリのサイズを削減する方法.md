---
tags:
  - Git
---

# Gitリポジトリのサイズを削減する方法

- 誤って node_modules などをコミットしてしまった場合などに。

## 1. 参考サイト

- https://qiita.com/kaneshin/items/0d19fc1cd86f931dc855

## 2. 必要ソフトのダウンロード

- `git_find_big.sh` は、.git ディレクトリの中からファイルサイズの大きい履歴データをリストアップしてくれるスクリプト。

```bash
wget https://confluence.atlassian.com/bitbucket/files/321848291/321979854/1/1360604134990/git_find_big.sh
```

## 3. Gitリポジトリの調査

- Gitリポジトリのルートディレクトリで、`git_find_big.sh` を実行
- サイズの大きい不要ファイルを確認

## 4. 不要データの削除

- `git filter-branch` コマンドで不要な履歴データを削除する。
- 削除する前にバックアップを取りたい場合は、参考サイトを参照

```bash
  * node_modules/ を削除したい場合のコマンド
  * ファイル単位だけでなく、ディレクトリ単位でも削除できる。

$ git filter-branch --index-filter 'git rm -r --cached --ignore-unmatch node_modules/' -- --all
```

## 5. 削除後のデータのコミット・プッシュ

```bash
git add .
git commit -m "Delete needless history file in .git/object."
git push origin --all --force
```

## 6. サイズが削減されたリポジトリの再クローン

- 消すのは履歴データであってファイル自身ではないため、作業していたローカルリポジトリのサイズは変化しない。
- ローカルリポジトリのサイズも削減したい場合は、一旦すべて削除してから、再度クローンすること。