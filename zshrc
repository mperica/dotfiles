# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
bindkey -v
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
#zstyle :compinstall filename '~/.zshrc'

#autoload -Uz compinit
#compinit
# End of lines added by compinstall
#

## AWS Completer ###
#source /usr/local/aws/bin/aws_zsh_completer.sh


### ANTIGEN ####
#
source ~/.antigen.zsh

# Load the oh-my-zsh's library.
antigen use oh-my-zsh

# Bundles from the default repo (robbyrussell's oh-my-zsh).
antigen bundle git
#antigen bundle heroku
antigen bundle pip
#antigen bundle lein
antigen bundle zsh-users/zsh-completions
#antigen bundle ssh-agent
antigen bundle twang817/zsh-ssh-agent

# Syntax highlighting bundle.
antigen bundle zsh-users/zsh-syntax-highlighting

# Plugins
plugins=(git ssh-agent)

# Load the theme.
#antigen theme robbyrussell
#antigen theme af-magic
#antigen theme jdavis/zsh-files themes/jdavis
antigen theme bira

# Tell Antigen that you're done.
antigen apply

# For SSH, starting ssh-agent is annoying
zstyle :omz:plugins:ssh-agent agent-forwarding on

# PATH
export PATH=~/.local/bin:$PATH

export TERM=rxvt-unicode
export VISUAL="vim"


#ssh-add ~/.ssh/*.pem &>/dev/null

#neofetch
screenfetch

