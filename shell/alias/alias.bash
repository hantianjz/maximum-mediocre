alias vim=nvim

# Convenient stuff
alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."

alias l="ls -Gal"
alias ls="ls -G"
alias ll="ls -Ghal"
alias empties="find . -empty -type d -maxdepth 2"
tableflip() {
  echo "（╯°□°）╯ ┻━┻";
}

alias pg="ps ax | grep -v grep | grep -i "
alias ip="ifconfig | grep 'inet '"
alias df='df -h'
alias ducks='du -cksh * | sort -rn|head -11' # Lists folders and files sizes in the current folder
alias profileme="history | awk '{print \$4}' | awk 'BEGIN{FS=\"|\"}{print \$1}' | sort | uniq -c | sort -n | tail -n 20 | sort -nr"
