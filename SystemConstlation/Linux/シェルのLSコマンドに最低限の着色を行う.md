---
tags:
  - Linux
---

シェルのLSコマンドに最低限の着色を行う

次のコードを`.bashrc`や`.zshrc`に入力

```
autoload -U compinit
compinit
 
export LSCOLORS=exfxcxdxbxegedabagacad
export LS_COLORS='di=34:ln=35:so=32:pi=33:ex=31:bd=46;34:cd=43;34:su=41;30:sg=46;30:tw=42;30:ow=43;30'
 
alias ls="ls -GF"
alias gls="gls --color"
 
zstyle ':completion:*' list-colors 'di=34' 'ln=35' 'so=32' 'ex=31' 'bd=46;34' 'cd=43;34'
```

参考サイト：zshでlsに色をつける  
http://mkit2009.hatenablog.com/entry/2013/01/28/001213