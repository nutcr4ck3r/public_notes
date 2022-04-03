---
tags:
  - Linux
  - Kindle
---

# Linux で Kindle for PC を使用する方法

いつまでたっても Kindle for Linux が出ないので。

~~いい加減にしろ。~~

## 必要な環境のインストール

### Wine

```bash
# apt-add-repository を使うために必要
sudo apt install -y software-properties-common

# Wine 安定版のインストール
sudo dpkg --add-architecture i386
wget -qO - https://dl.winehq.org/wine-builds/winehq.key | sudo apt-key add -
sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ hirsute main'
sudo apt install --install-recommends winehq-stable

# インストール確認
wine --version
```

### Winetricks 及び日本語フォント

Wine の環境を整えるためのツール

```bash
sudo apt install --install-recommends winetricks
```

日本語が豆腐に文字化けしないようにフォントをインストール

```bash
winetricks -q fakejapanese_ipamona
```

## Kindle for PC のインストール

<https://amzn.to/3vhAURs> から EXE をダウンロード、Wine で実行

```bash
# 起動時のエラー発生を抑制するために必要なディレクトリを作成
mkdir -p ${WINEPREFIX:-$HOME/.wine}/drive_c/users/$USER/AppData/Local/Amazon/Kindle

# インストール
wine Kindle_for_PC_Windows_ダウンロード.exe
```

## Kindle for PC のセットアップ

### ログイン

サインイン先を`Default`から`amazon.co.jp`を選択し、ログイン

### 自動アップデートの無効化

自動アップデートが有効な場合、途中でソフトウェアが異常終了するため、無効化

`Tools => Options => General => 'Automatically install updates...' をオフ`

## ２回目以降の起動

いずれかの方法で起動できる。

- `~/.wine/drive_c/Program Files (x86)/Amazon/Kindle`にある`Kindle.exe`を実行
- スタートメニューに存在する Kindle のショートカットから実行

