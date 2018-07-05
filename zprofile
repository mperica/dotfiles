typeset -U path
path=(~/.local/bin $path[@])

# load ssh keys from directory
ssh-add ~/.ssh/private_keys/* 2>/dev/null
