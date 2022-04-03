---
tags:
  - Windows
  - キーボード
---
# Windows 設定覚書

Windows 10 クリーンインストールをやらかした場合の備忘録

## Windows アップデートを適用

Windows 公式ページから最新版へアップデート

<https://www.microsoft.com/ja-jp/software-download/windows10>

※ WSL の利用に必要

## セーフモードに F8 連打で入れるように設定

1. コマンドプロンプトを管理者権限で有効化
2. `bcdedit /set {default} bootmenupolicy legacy`

## Chrome ウェブブラウザをインストール

<https://www.google.co.jp/chrome/>

## Chocolatey と ツール類のインストール

1. chocolatey のインストール
    - PowerShell を Admin 起動して以下を実行
    - `Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))`
2. Hackgen フォントインストール
    - `cinst -y font-hackgen-nerd`
3. 7zip インストール
    - `cinst -y 7zip`
4. Chrome インストール
    - `cinst -y googlechrome`
6. PowerToys インストール
    - `cinst -y powertoys`

## Windowsの Capslock を完全に Ctrl にする

### 必要なソフトウェア

- Change Key
  - <https://forest.watch.impress.co.jp/library/software/changekey/>
- PowerToys
  - Chocolatey でインストール済

### 1. Change Key で Capslock を F13 にする

素のまま Capslock を Ctrl に入れ替えると、何故か Ctrl が押されっぱなしになる現象が発生しがち。

これを解消するために、Capslock の機能をまず F13 という機能が存在しないキーコードに変更する。

1. Change Key をダウンロードし、管理者権限で起動
2. CapsLock をクリックし、キー割り当て画面右上の "Scan Code" から "0x0064" を設定

### 2. PowerToys で F13 を Ctrl に入れ替え

1. PowerToys 起動
2. Keyboard Manager からキー割り当てを変更

## WSL 有効化と Ubuntu インストール

### 有効化

1. コントロールパネル => プログラムと機能 =>『Windows の機能の有効化または無効化』から以下を有効化
    - Hyper-V
    - Linux 用 Windows サブシステム 叉は Windows Sussystem for Linux
    - 仮想マシンプラットフォーム
2. 管理者権限で起動した PowerShell から以下を実行

```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
wsl --set-default-version 2
```

### Ubuntu インストール

```powershell
wsl -l --online  # 利用可能なディストリビューションの一覧
wsl --install    # 基本的な Ubuntu のインストール
wsl -l -v        # インストールされている Linux システムの一覧
```

## VSCode インストール

<https://code.visualstudio.com/download>
