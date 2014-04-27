# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
bindkey -e
bindkey    "^[[3~"          delete-char
bindkey    "^[3;5~"         delete-char
bindkey "^[[7~" beginning-of-line       # Pos1
bindkey "^[[8~" end-of-line             # End

# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/patrick/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall
autoload -U promptinit
promptinit
prompt adam2 

alias ls='ls --color=auto -lh'
alias cd..='cd ..'
#alias m5='md5chk -d %1Fty~5PTQ'

function m5 {
	md5chk -d $1Fty~5PTQ
}

[ -r /etc/profile.d/cnf.sh ] && . /etc/profile.d/cnf.sh

cowthink "Was machen Sachen? Moo."
