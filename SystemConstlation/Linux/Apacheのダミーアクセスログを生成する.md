---
tags:
  - Docker
  - Ruby
  - ログ解析
---

Apacheのダミーアクセスログを生成する

Apache-loggen という Ruby 製ソフトウェアを使用する。
- Docker イメージをダウンロードし、コンテナを起動

```
sudo docker pull ruby
sudo docker run -it -v /home/user/share:/home/user/share --rm --name ruby ruby /bin/bash
```

- Apache-loggen をインストール

```
gem install apache-loggen -N -V
```

-  ログを生成

```
apache-loggen --rate=10 --limit=10
 * ログを10個/秒の速度で、10個までを制限として生成
 * ファイルに出力する際はパイプを使用する。
 * json 形式で出力する場合は、最後に --json オプションを付与する。
```

参考サイト：apache-loggen を使って Apache アクセスログのダミーログを生成する  
https://inokara.hateblo.jp/entry/2015/06/21/225143
