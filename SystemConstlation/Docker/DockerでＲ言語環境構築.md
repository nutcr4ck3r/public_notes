---
tags:
  - Docker
  - R言語
---

DockerでＲ言語環境構築

Dockerでコンテナ作成して繋ぐだけ。

- Dockerイメージをダウンロード

```
$ sudo docker pull rocker/rstudio
* rocker/verse でも良いが、リッチな分、最終的なサイズは大きい。
```

- Dockerコンテナを作成

```
$ sudo docker run -e PASSWOR=user -p 8787:8787 --rm --name rocker
* -e で初期パスワードを設定しないと、コンテナが正常に起動しない。
```

- ブラウザから接続

```
http://localhost:8787
* username=rstudio , password=user (起動コマンドで設定したもの)
```

- Rパッケージで不足がある場合は`/bin/bash`でコンテナを起動し、インストールしてからコミットする。

- パッケージはCのコードでダウンロードしてくるので、非常に時間がかかることに注意

参考サイト：The rocker project  
https://www.rocker-project.org/