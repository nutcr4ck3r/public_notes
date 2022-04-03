---
tags:
  - VMware
---

VMware上のOSを高速化する

仮想マシンの動作を高速化するための設定

# VMXファイルの編集

## 仮想マシン起動中の.vmemファイルの作成抑止

```
mainMem.useNamedFile = "FALSE"
```

## ページ共有機能の無効化

```
sched.mem.pshare.enable = "FALSE"
```

## メモリ使用量が変化してもメモリサイズを固定する

```
prefvmx.useRecommendedLockedMemSize = "TRUE"
MemAllowAutoScaleDown = "FALSE"
```

## 全部入り

```
mainMem.useNamedFile = "FALSE"
sched.mem.pshare.enable = "FALSE"
prefvmx.useRecommendedLockedMemSize = "TRUE"
MemAllowAutoScaleDown = "FALSE"
```