---
tags:
  - Linux
  - XFCE
---

# Linux (XFCE) のメニューにアプリケーションを追加

`~/.local/share/applications`に、以下の定形で`~~.desktop`ファイルを作成する。

```text
[Desktop Entry]
Type=Application
Encoding=UTF-8
Name=Rhyme
Comment=Modern design music player
Exec=/snap/bin/rhyme
Icon=/snap/rhyme/current/meta/gui/icon.png
Categories=X-XFCE;X-Xfce-Toplevel;Utility;
```

`Categories`は、アプリケーションを表示させるカテゴリ。複数指定可能

カテゴリの一覧は次の通り。

```text
Categories=X-XFCE;X-Xfce-Toplevel;Utility;

X-Xfce-Toplevel
Settings
Accessibility
Core
Legacy
Utility
Development
Education
Game
Graphics
Audio
Video
AudioVideo
Network
Office
System
```
