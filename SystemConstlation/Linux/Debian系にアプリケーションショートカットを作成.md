---
tags:
  - Linux
  - 環境構築
---

# ショートカット作成（例：Android Studio の場合）

- ターミナルを開く
- gedit ~/.local/share/applications/android-studio.desktop でファイルを開く
- Desktopファイルの記述方法に従って、android-studio.desktop を記述し、保存する
- chmod 773 ~/.local/share/applications/android-studio.desktop でファイルに実行権限を与える
  - ＊無くても動作した。
- ログアウトし、ログインする

## Desktopファイルの記述例

```bash
[Desktop Entry]
Type=Application
Encoding=UTF-8
Name=Android Studio
Comment=Android Studio
Exec=/opt/android-studio/bin/studio.sh
Icon=/opt/android-studio/bin/studio.png
```
