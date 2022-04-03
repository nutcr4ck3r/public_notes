---
tags:
  - Linux
  - サーバ構築
---

iptables設定例

- 番号付きで表示・確認

```
sudo iptabels -nL INPUT --line-numbers
```

- 挿入、IPアドレス指定、複数ポートを指定

```
sudo iptables -I INPUT 5 -s x.x.x.x -m multiport -p tcp --dports 22,80,443 -m state --state NEW -j ACCEPT
```

- 削除、61番目（途中の番号を削除すると以降の番号がずれるため、後ろから削除する方が安心）

```
sudo iptables -D INPUT 61
```