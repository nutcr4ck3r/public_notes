---
tags:
  - フォレンジック
  - Linux
---

imgファイルを直接マウントする方法

```
sudo mount -t ext4 -o loop,rw,offset=0 {イメージファイル.img} {マウント先PATH}
```