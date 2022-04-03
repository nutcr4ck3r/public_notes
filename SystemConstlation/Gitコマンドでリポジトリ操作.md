---
tags:
  - Git
---

# Gitコマンドでリポジトリ操作

## 1. 初期設定

### 1.1. ローカルリポジトリを作成する場合

```bash
git init
```

## 2. リモートリポジトリからクローンする場合

```bash
git clone https://{username}@github.com/username/repository.git
# 要パスワード入力
```

## 3. git lfs導入

- サイズの大きいファイルの履歴データを無駄に増加させないためのソフトウェア
- <https://git-lfs.github.com/> からバイナリダウンロード、インストール

```bash
git lfs install
git lfs track "*.pdf"
git lfs track "*.exe"
git lfs track "*.zip"
git lfs track "*.tar"
git lfs track "*.gz"
```

## 4. SSHキーの作成・登録

### 4.1. キーの作成

```bash
ssh-keygen -t rsa -b 4096 -C "comment"
  # -C以下のコメントは任意
  # 作成場所は任意。但し、デフォルト以外だと.ssh/configの作成が必要
  # パスフレーズは空白でも作成可能
chmod 400 ssh_key.pub  # 秘密鍵のパーミッションを変更
```

### 4.2. GitHub 上での操作

1. GitHub のアバターアイコン => `settings`
2. `SSH & GPGkeys` => `NewSSHkey` に"公開鍵"（xxx.pub）の内容を貼り付け。
3. `vi ~/.ssh/config（デフォルトパス以外で作成した場合）`

```bash
 Host github
   HostName github.com
   User git
   IdentityFile ~/.ssh/id_rsa_github # 作成した"秘密鍵"のパス
```

パブリックキーのパーミッションエラーが出る場合やパスワードを何回も聞かれる場合は次を実行

```bash
# GitHub の CloneOrDownload から UseSSH => 文字列コピー
git remote set-url origin {コピー文字列}
git remote set-url origin git@github.com:user/repo.git
# sshキーをデフォルトパス（~/.ssh/id_rsa）に変更
(ssh周りは https://qiita.com/rorensu2236/items/df7d4c2cf621eeddd468 を参照)
```

## 5. ユーザ設定

リポジトリにコミットするユーザ名・メールアドレス、
コミットメッセージ編集に使用するエディターの指定

```bash
git config --global user.name "username"
git config --global user.email "mailaddress"
git config --global core.editor "/bin/vim"
```

## 6. リポジトリ操作

### 6.1. ステージング（add）

```bash
git add .  # 全てのファイル
git add {filename}  # 指定ファイル
```

### 6.2. コミット

```bash
git commit -a -m "message"
# -mオプション除外でエディター起動
```

### 6.3. ローカルをリモートリポジトリに反映

```bash
git remote add reponame {リモートリポジトリのSSHのcopy}
git push --set-upstream reponame master
```

### 6.4. リモートリポジトリへプッシュ

```bash
git push storage master
* storageリポジトリのmasterブランチへプッシュ
```

### 6.5. 差分の確認

```bash
git diff  # 最後のgit addからの差分
git diff --stat  # 最新のgit addから変更された割合の表示
git diff --name-only  # 変更されたファイルの名前のみ表示
git diff --cached  # 最後のgit addと最新コミットの差分
git diff HEAD^  # 最新コミットと最新コミット−１の差分
```

### 6.6. addの取り消し

```bash
git reset HEAD .  # 全てのgit addをリセット
git reset HEAD {filename}  # 指定ファイルのgit addをリセット
```

### 6.7. コミットの取り消し

```bash
git commit --amend  # 直前のコミットを取り消し
git commit --soft HEAD~2  # 過去２件分のコミットを取り消し（変更は保持）
git commit --hard HEAD~2  # 過去２件分のコミットを変更を含めて取り消し
```

### 6.8. ブランチの作成・編集

```bash
git branch {branch_name}  # ブランチの作成
git checkout {branch_name}  # ブランチの移動
git branch -d {branch_name}  # ブランチの削除
git branch -m {branch_name}  # 現在のブランチ名の変更
git branch  # ローカルブランチの一覧
git branch -a  # リモートとローカルのブランチの一覧
git branch -r  # リモートブランチの一覧
git checkout -b branch_name origin/branch_name  # リモートブランチへチェックアウト
```

### 6.9. 編集をマージ

master以外のブランチで編集した箇所をmasterに反映させる

```bash
git checkout {branch_name}  # ブランチに移動
git commit -a -m "コメント"  # 変更ファイルをコミット
git checkout master  # masterに移動
git merge {branch_name}  # 差分をマージ
git push origin master  # ファイルの更新
```

### 6.10. マージの取り消し

コンフリクトが発生して一旦戻したい場合に使用

```bash
git merge --abort
```

