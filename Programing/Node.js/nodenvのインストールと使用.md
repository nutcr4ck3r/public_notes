---
tags:
  - Node.js
  - 覚書
---

# nodenv のインストールと使用

## 1. インストール

基本的には公式ページのコマンドを実行していくのみとなる。

### 1.1. macOS の場合

```bash
brew install nodenv
brew install node-build
echo 'eval "$(nodenv init -)"' >> ~/.zshrc
```

### 1.2. Linux の場合

```bash
git clone https://github.com/nodenv/nodenv.git ~/.nodenv
cd ~/.nodenv && src/configure && make -C src
echo 'export PATH="$HOME/.nodenv/bin:$PATH"' >> ~/.zshrc
# ターミナルを再起動
mkdir -p "$(nodenv root)"/plugins
git clone https://github.com/nodenv/node-build.git "$(nodenv root)"/plugins/node-build
~/.nodenv/bin/nodenv init
```

## 2. アップグレード

### 2.1. macOS でのアップグレード

```bash
brew upgrade nodenv node-build
```

### 2.2. Linux でのアップグレード

```bash
cd ~/.nodenv
git pull

cd ~/.nodenv/plugins/node-build
git pull
```

## 3. 指定バージョンの Node.js を利用する

### 3.1. バージョンを指定してインストール

```bash
# インストール可能バージョンのリスト表示
nodenv install --list

# 指定バージョンのインストール
nodenv install 16.12.0

# 指定バージョンのアンインストール
nodenv uninstall 14.8.0

# 新規にインストールした後は、rehash を実行して認識させる。
nodenv rehash
```

### 3.2. バージョンを指定して利用

```bash
# 指定バージョンをローカル／グローバルに適用
# local = カレントディレクトリに適用
nodenv local 16.12.0

# global = システム全体に適用
nodenv global 16.12.0

# 現在適用されているバージョンの確認
nodenv versions
  15.14.0
  16.3.0
```
