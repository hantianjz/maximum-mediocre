#!/bin/sh -x
# compat.sh - tmux compatibility

# tmux does a terrible job integrating with the underlying operating
# system, especially when it is executing in a graphical environment.
# To add insult to injury, backward compatibility is not maintained for
# options, which change meaning between versions. This script attempts
# to bridge this divide so a common tmux.conf can be used on different
# systems running different versions without issue.

case `uname -s` in
Darwin)

    # Setup 'v' to begin selection as in Vim
    bind-key -t vi-copy v begin-selection
    bind-key -t vi-copy y copy-pipe "reattach-to-user-namespace pbcopy"

    # Update default binding of `Enter` to also use copy-pipe
    unbind -t vi-copy Enter
    bind-key -t vi-copy Enter copy-pipe "reattach-to-user-namespace pbcopy"

	;;
Linux)
    # Setup 'v' to begin selection as in Vim
    bind-key -t vi-copy v begin-selection
    bind-key -t vi-copy y copy-pipe "reattach-to-user-namespace xclip -sel clip -i"

    # Update default binding of `Enter` to also use copy-pipe
    unbind -t vi-copy Enter
    bind-key -t vi-copy Enter copy-pipe "reattach-to-user-namespace xclip -sel clip -i"

	;;
esac

version=`tmux -V | cut -c 6-`
has_version() {
	return `echo $@ | awk "{print (($version >= \$1) == 0)}"`
}

if has_version 2.1; then
	# Enable mouse support:
    set-option -g -q mouse on
    bind -n WheelUpPane if-shell -F -t = "#{mouse_any_flag}" "send-keys -M" "if -Ft= '#{pane_in_mode}' 'send-keys -M' 'copy-mode -e'"

    # Fix to allow mousewheel/trackpad scrolling in tmux 2.1
    bind-key -T root WheelUpPane if-shell -F -t = "#{alternate_on}" "send-keys -M" "select-pane -t =; copy-mode -e; send-keys -M"
    bind-key -T root WheelDownPane if-shell -F -t = "#{alternate_on}" "send-keys -M" "select-pane -t =; send-keys -M"

elif has_version 1.6; then
	# Enable mouse support:
	tmux set-option -g mouse-mode on
	tmux set-option -g mouse-resize-pane on
	tmux set-option -g mouse-select-pane on
	tmux set-option -g mouse-select-window on
fi
exit 0
