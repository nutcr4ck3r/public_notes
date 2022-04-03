---
tags:
  - Linux
---

# Linuxでユーザを作成してsudo権限をつける

- `useradd`によるユーザ作成は、ホームディレクトリが作成されない。
- `adduser`により作成することでホームディレクトリが作成される。

```bash
adduser {user_name}

 Adding user `user_name' ...
 Adding new group `user_name' (1002) ...
 Adding new user `user_name' (1002) with group `user_name' ...
 Creating home directory `/home/user_name' ...
 Copying files from `/etc/skel' ...
 Enter new UNIX password:  # パスワード入力
 Retype new UNIX password: # パスワード入力（確認）
 passwd: password updated successfully
 Changing the user information for user_name
 Enter the new value, or press ENTER for the default
         Full Name []:    # Enter連打
         Room Number []: 
         Work Phone []: 
         Home Phone []: 
         Other []: 
 Is the information correct? [Y/n] Y  # Yes
```

- 追加ユーザをsudoグループに追加

```bash
gpasswd -a {user_name} sudo
```
