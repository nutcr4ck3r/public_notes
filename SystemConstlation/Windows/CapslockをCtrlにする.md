---
tags:
  - Windows
  - キーボード
---

# Windowsの Capslock を完全に Ctrl にする

## 必要なソフトウェア

- Change Key
  - <https://forest.watch.impress.co.jp/library/software/changekey/>
- PowerToys
  - <https://docs.microsoft.com/ja-jp/windows/powertoys/install>

## 1. Change Key で Capslock を F13 にする

素のまま Capslock を Ctrl に入れ替えると、何故か Ctrl が押されっぱなしになる現象が発生しがち。

これを解消するために、Capslock の機能をまず F13 という機能が存在しないキーコードに変更する。

1. Change Key をダウンロードし、管理者権限で起動
2. CapsLock をクリックし、キー割り当て画面右上の "Scan Code" から "0x0064" を設定

## 2. PowerToys で F13 を Ctrl に入れ替え

1. PowerToys 起動
2. Keyboard Manager からキー割り当てを変更
