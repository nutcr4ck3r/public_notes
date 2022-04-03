---
tags:
  - Linux
  - サーバ構築
  - 環境構築
---

Sambaを設定してLinux-Windows間でファイルを共有

## ネットワーク設定

- SAMBA端末とWindows端末の両方に同じ仮想ネットワークアダプタ（ホストオンリー）を追加
- ネットワークのサブネットを合わせて通信可能にする。

## コンフィグファイルの編集

### `/etc/samba/smb.conf`を編集

以下を追記

```
[public]
    path = /home/kali/Public
    writable = yes
    security = user
```

### 文法誤りなどが無いかチェック

`testparm`コマンドでチェック

```
$ testparm

Load smb config files from /etc/samba/smb.conf
Loaded services file OK.
```

### Sambaユーザを登録

```
$ sudo useradd user    # ホームディレクトリを持たないユーザの作成
$ sudo pdbedit -a smbuser    # Samba用ユーザデータベースへ登録
```

## サービスの開始

 `smbd`、`nmbd`サービスを起動

```
$ sudo systemctl start smbd
$ sudo systemctl start nmbd
$ sudo systemctl enable smbd    # 次回以降もサービスを自動起動させる場合
$ sudo systemctl enable nmbd    # 次回以降もサービスを自動起動させる場合
```

## Windowsからの接続

`¥¥Linux's IP-address¥`をエクスプローラに入力して接続

## トラブルシューティング：WindowsのSamba認証情報をリセットする場合

接続が不安定になった場合に実行。

1. `ファイル名を指定して実行` -> `rundll32 keymgr.dll KRShowKeyMgr`
2. 表示された編集画面で、対象のサーバーを選択して編集なり消去する。
3. コントロールパネル→ユーザーアカウント→資格情報の管理からも同様の編集が可能
