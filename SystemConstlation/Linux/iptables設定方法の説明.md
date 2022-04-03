---
tags:
  - Linux
  - サーバ構築
---

iptables設定方法の説明

## 設定上、特に気をつけるべき内容
- 適用するルールは「ACCEPT, LOG, DROP」の順番で記載する。
  - iptables は、上から順番に評価する仕組みであるため。
  - DROP:anywhereの下にACCEPTを記載しても、許可ルールは適用されない。

## ルールの書式

```
sudo iptables {command} {chain} {rule-specification} {target}
```

- command（チェインに何をするか）
  - `-A` : 追加　`sudo iptables -A INPUT {rule}`
  - `-D` : 削除　`sudo iptables -D INPUT {rule number}`
  - `-R` : 置換　`sudo iptables -R INPUT {rule number}`
  - `-I` : 挿入　`sudo iptables -I INPUT 1 {rule}`
  - `-L` : 表示　`sudo iptables -nL INPUT --line-numbers`

- options : `-n` ホスト情報のアドレスを数値表示
  - `-F` : チェインの全ルールを削除　`sudo iptables -F INPUT`
  - `-P` : チェインのデフォルトポリシーを設定　`sudo iptabels -P INPUT DROP`

- chain（チェイン名の指定）
  - PREROUTING（`-t nat` を併記）
  - INPUT
  - OUTPUT
  - POSTROUTING（`-t nat` を併記）
  - FORWARD

- rule-specification（フィルタリングするパケットの特徴指定）
  - `-s` : パケットの送信元。ipアドレス、ネットワークアドレスを指定可能
      - `-s 192.168.0.3`  `-s ! 10.0.0.0/21（否定設定）`
  - `-d` : パケットの送信先。書式は -s に同じ。否定設定可
  - `-p` : パケットのプロトコル。tcp, udp, icmp, all など。否定設定可
      -  `-p tcp`
      - TCP/UDP拡張（`-p tcp`又は`-p udp`の際に指定可能）
         - `--sport` : (tcp/udp) 送信元ポート指定。ポート番号又はポート名を使用可能。否定設定可
           - `-p tcp --sport 22:80（２２〜８０を指定）`
        - `--dport` : (tcp/udp) 宛先ポート指定。書式は`--sport`に同じ。否定設定可
     - ICMP拡張（`-p icmp`の際に指定可能）
       - `--icmp-type` : icmpタイプを指定。否定設定可
  - `-i `: パケットの入ってくるインターフェース名。OUTPUTチェインには指定不可能。否定設定可
      - `-i eth0`
  - `-o` : パケットの出ていくインターフェース名。INPUTチェインには指定不可能。書式は -i に同じ。否定設定可
  - `-m` : マッチ条件指定、limit 拡張、state 拡張又は multiport 拡張を使用するためのモジュール追加オプション。
      - `-m {protocol} --{option}` : 指定したプロトコルの詳細マッチ条件を指定
          - ex) `-p tcp -m tcp --dport 22`　tcp の２２番ポート宛通信を指定。`-p tcp --dport`と同じ。
      - `-m --limit {rate}` : 単位時間 (second, minute, hour, day) あたりに許容されるマッチ回数。
          - `-m --limit 3/hour（１時間あたり３回まで）`
      - `-m state --state` : パケットの状態を指定
          - NEW（新規）, ESTABLISHED（継続）, RELATED（関連）, INVALID（それら以外）
          - `-m state --state ESTABLISHED,RELATED`
      - `-m multiport` : 複数ポートを指定する。
          - `-m multiport -p tcp --dports 22,80,443`
  - `-j` : ターゲットの指定
      - `-j ACCEPT` : パケットを通貨させる。
      - `-j DROP` : パケットを破棄する。
      - `-j REJECT` : パケットを破棄した上で、その旨をICMPで送信元に通知する。
      - `-j LOG` : マッチしたパケットのログを記録する。

参考サイト：iptablesのコマンド書式
https://www.turbolinux.co.jp/products/server/11s/user_guide/iptablescmd.html
