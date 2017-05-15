# vi-keys.tmux - vi key bindings for tmux

bind-key -Tcopy-mode-vi  Escape send -X cancel
bind-key -Tcopy-mode-vi  'v' send -X begin-selection

# bind-key -t vi-edit Escape cancel

# Cursor Movement
bind-key C-j select-pane -D
bind-key j   select-pane -D

bind-key C-k select-pane -U
bind-key k   select-pane -U

bind-key C-h select-pane -L
bind-key h   select-pane -L

bind-key C-l select-pane -R
bind-key l   select-pane -R

# Opening and Closing Windows/Panes
bind-key C-s split-window -v
bind-key s   split-window -v

bind-key C-v split-window -h
bind-key v   split-window -h

bind-key C-n new-window
bind-key n   new-window

bind-key C-q kill-pane
bind-key q   kill-pane

bind-key C-o kill-pane -a
bind-key o   kill-pane -a

# Resizing Panes
# bind-key -   resize-pane -D
# bind-key +   resize-pane -U
# bind-key <   resize-pane -L
# bind-key >   resize-pane -R
# bind-key _   resize-pane -Z

# Detect if pane is running vim(1), based on vim-tmux-navigator;
# see: https://github.com/christoomey/vim-tmux-navigator.
is_vim="ps -o comm= -t #{pane_tty} | grep -E -i -q '(vi|vim(diff)?)$'"

# bind-key -n C-w if-shell "$is_vim" "send-keys C-w" "switch-client -T vi-select"

bind -n C-h run "(tmux display-message -p '#{pane_current_command}' | grep -iqE '(^|\/)vim$' && tmux send-keys C-h) || tmux select-pane -L"
bind -n C-j run "(tmux display-message -p '#{pane_current_command}' | grep -iqE '(^|\/)vim$' && tmux send-keys C-j) || tmux select-pane -D"
bind -n C-k run "(tmux display-message -p '#{pane_current_command}' | grep -iqE '(^|\/)vim$' && tmux send-keys C-k) || tmux select-pane -U"
bind -n C-l run "(tmux display-message -p '#{pane_current_command}' | grep -iqE '(^|\/)vim$' && tmux send-keys C-l) || tmux select-pane -R"
bind -n C-\ run "(tmux display-message -p '#{pane_current_command}' | grep -iqE '(^|\/)vim$' && tmux send-keys 'C-\\') || tmux select-pane -l"
bind C-l send-keys 'C-l'

# vim: ft=tmux
