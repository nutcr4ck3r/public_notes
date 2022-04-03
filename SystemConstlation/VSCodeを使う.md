---
tags:
  - VSCode
---

# VSCode の設定覚書

## 1. 設定のエクスポート・インポート

### 1.1. settings.json / keybindings.json

- macOS
  - `~/Library/Application\ Support/Code/User/settings.json`
- Linux(Ubuntu 18.04)
  - `~/.config/Code/User/settings.json`
- Windows10
  - `%APPDATA%/Code/User/settings.json`
  - `%APPDATA%/Roaming/Code/User/settings.json`

### 1.2. 拡張機能

インポート用のコマンドラインを以下のコマンドで出力

```bash
code --list-extensions | xargs -L 1 echo code --install-extension
```

## 2. code-server を使用する場合

### 2.1. インストール（Linux の場合）

参考：<https://qiita.com/shin1kt/items/acf44cb7e8112e2b6a18>

ターミナルから以下を実行

```bash
curl -fsSL https://code-server.dev/install.sh | sh -s -- --dry-run
curl -fsSL https://code-server.dev/install.sh | sh
```

起動

```bash
code-server
```

起動により設定ファイルが作成されるので、パスワードを確認

```bash
[~/.config/code-server/config.yaml]

bind-addr: 127.0.0.1:8080
auth: password
password: *******************
cert: false
```

自動起動用スクリプト作成

```bash
[/opt/code-server.sh]

#!/bin/bash

/usr/bin/code-server /home/[ユーザー名] --config="/home/[ユーザー名]/.config/code-server/config.yaml"

# 作成後に "sudo chmod +x code-server.sh" で実行権限付与
```

自動起動用スクリプトをキックするためのサービスの作成

```bash
[/etc/systemd/system/code-server.service]

[Unit]
Description = code-server service

[Service]
ExecStart = /opt/code-server.sh
Restart = always
Type = simple
User = [ユーザー名]
Group = [ユーザーグループ名（ユーザ名と同じで大丈夫なはず）]

[Install]
WantedBy = multi-user.target
```

サービス起動及び自動起動設定

```bash
systemctl start code-server
systemctl enable code-server
```

### 2.2. code-server の使用方法

- ブラウザで `localhost:8080` にアクセス
- パスワードを入力してアクセス
  - パスワードはサービス停止の後、`code-server --auth none` で不要になる（かもしれない）。
- Chrome のキーバインドと競合するため、アドレスバー右端のアイコンからアプリとしてインストール

### 2.3. 細かい設定

- キーバインドは File -> Preferences -> Keyboard Shortcuts から変更。変更後はウィンドウ再起動
- 最低限変えるべきショートカット : `Trigger Suggest` : IME オンオフと重複しているため致命的
- タイトルバーに Linux のウィンドウテーマを適用する場合は以下参照
  - File -> Preferences -> Settings
  - Window -> Title Bar Style を custom に変更

## 3. VSCode (code-server) で白源フォントを適用する方法

参照：<https://www.randynetwork.com/blog/hackgen-introduce/>

### 3.1. for macOS

```bash
brew tap homebrew/cask-fonts
brew install font-hackgen
brew install font-hackgen-nerd
```

### 3.2. for Linux

1. GitHub リポジトリから公式リリースをダウンロード：<https://github.com/yuru7/HackGen>
2. zip 解凍、`/usr/share/fonts/`に移動
3. `fc-cache -fv`でフォント更新
