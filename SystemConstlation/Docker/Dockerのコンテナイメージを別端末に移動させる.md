---
tags:
  - Docker
---

Dockerのコンテナイメージを別端末に移動させる


`docker pull`できないオフライン環境等のコンテナをアップグレードする場合などに使用。

-  コンテナイメージをオンラインからダウンロード

```
$ sudo docker pull ubuntu:latest
```

-  コンテナイメージを圧縮

```
$ sudo docker save -o ./ubuntu.tar ubuntu:latest
```

-  コンテナイメージを別端末にコピー

-  コンテナイメージをロード

```
$ sudo docker load -i ubuntu.tar
```