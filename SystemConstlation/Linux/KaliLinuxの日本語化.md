---
tags:
  - Linux
  - KaliLinux
---

# KaliLinuxの日本語化

- Kali LinuxのVMイメージは大変便利
- だけど英語設定なので日本語表示が文字化けするし入力できない。
- 日本語でいい感じに使用できるようにする。
- Debian系のディストリも同様の手順で設定可能

## アップデート

```bash
sudo apt update && sudo apt upgrade -y
```

## 日本語入力設定

- Fcitx-Mozcインストール

```bash
sudo apt install fcitx-mozc
```

- 入力メソッド設定

```bash
$ im-config &
  * GUIが起動するので fcitx を入力メソッドに設定
  * 設定後、ログアウト＆再ログイン
```

- 再ログイン後、`Fcitx Configuration` から入力方式を追加し、以下の並びにする。
- 必ず、直接入力（Keyboard - English/Japanese）が上に来るように設定すること。


```bash
Keyboard - English (us or jp)
Mozc
```

## 日本語表示

```bash
sudo dpkg-reconfigure locales
  * この後のLocales設定で "ja_JP.UTF-8 UTF-8" を選択
  * 選択はスペースキー、フォーカス移動はTABキーを使用
sudo apt install fonts-ipafont
  * 中華風フォントが適用される場合の対処
```

## タイムゾーンを変更

```bash
$ sudo dpkg-reconfigure tzdata
  * この後のタイムゾーン設定で "Asia - Tokyo" を選択

又は

$ sudo rm -f /etc/localtime
$ sudo ln -s /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
```

## 再起動

- 全ての作業完了後、再起動
- 場合によっては完全な日本語化まで複数回再起動の必要あり。
  - 完全に日本語化されたかどうかは、メインメニューを開けば判断できる。
  - メニューのプログラム名や設定ソフトの項目名が日本語化されていればOK
