---
tags:
  - Docker
---
Dockerに外部へ通信させる為のTips

基本的に閉じられた環境であるDockerから通信する際、基本的なテクニックを覚えておく必要がある。

前提として、Dockerコンテナ内から通信ができるのは、ホストが宛先を解決できる範囲と同じ。

## 直接IPアドレスを指定する場合
- ホストが持つIPアドレスを直接指定する。（host=192.168.0.1の場合、http://192.168.0.1:80でアクセス）
- ただし、指定したポートがコンテナなどにフォワーディングされていないか確認が必要

## --add host を使う場合

```
$ docker run --add-host=local_dev:192.168.0.1
* http://local_dev:80 でアクセスできる。
```

## docker-compose.yml で指定する場合

```
[docker-compose.yml]
extra_hosts:
  - "local_dev:$192.168.0.1"
  *やっていることは、/etc/hosts に追記しているのと同じ。
```

参考サイト：Dockerのコンテナの中からホストOS上のプロセスと通信する方法  
https://qiita.com/Iju/items/badde64d530e6bade382
