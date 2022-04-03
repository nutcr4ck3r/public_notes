---
tags:
  - Python
---

# pyenv のインストールと使用

## インストール

### macOS の場合

```bash
brew update
brew install pyenv
echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

### Linux の場合

Zsh の場合を記述

ファイルが存在しない場合は、`.zshrc`に読み替えても問題ないハズ

```bash
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
cd ~/.pyenv && src/configure && make -C src

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zprofile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zprofile
echo 'eval "$(pyenv init --path)"' >> ~/.zprofile

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
echo 'eval "$(pyenv init --path)"' >> ~/.profile

echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

## アップグレード

### macOS でのアップグレード

```bash
brew upgrade pyenv
```

### Linux でのアップグレード

```bash
cd ~/.pyenv
git pull
```

## 指定バージョンのインストール

```bash
# インストール可能なバージョンのリストを表示
pyenv install --list

# 指定バージョンのインストール
pyenv install 3.8.0
```

## 指定バージョンの利用

```bash
# local = カレントディレクトリに適用
pyenv local 3.8.0

# global = システム全体に適用
pyenv global 3.8.0

# 現在適用されているバージョンをチェック
pyenv versions
```
