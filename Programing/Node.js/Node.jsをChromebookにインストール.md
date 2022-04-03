---
tags:
  - Node.js
  - ChromeOS
---

# Node.js を Chromebook にインストールする

ChromeOS の Linux は、`sudo apt install nodejs`すると、かなり古いバージョンが降ってくる。

これを解消する。

## How to install

### n パッケージで Node.js をアップグレード

```bash
sudo npm install -g n
sudo n lts  # lts=推奨版のインストール latest=最新版
```

### コマンドで使用できるかを確認

```bash
node -v
npm -v

node

> 1 + 1
(Ctrl + D)
```
