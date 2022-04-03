---
tags:
  - VMware
---

VMware上のLinuxで共有フォルダを使用する場合の設定

- VM Tools をインストールする。

```
sudo apt install open-vm-tools open-vm-tools-desktop
```

- VMの設定から共有フォルダを有効にする。

- `/mnt/hgfs`に共有フォルダが作成されている。
- 作成されていない場合、コマンドでマウントする。

```
sudo vmhgfs-fuse .host:/ /mnt/hgfs  " /mnt/hgfsにマウント
sudo vmhgfs-fuse .host:/ /home/user/Public -o nonempty  " /home/user/Publicにマウント
  * -o nonempty : マウント先ディレクトリが空でなくても強制的にマウントするオプション
```