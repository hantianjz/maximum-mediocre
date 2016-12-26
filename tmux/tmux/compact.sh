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
	# Reattach to the per-user namespace to access the pasteboard.
	# For macOS Sierra, specify  `--with-wrap-pbcopy-and-pbpaste`
	# when installing reattach-to-user-namespace via brew(1);
	# see: https://github.com/ChrisJohnsen/tmux-MacOSX-pasteboard,
	#      http://superuser.com/a/413233.
	tmux set-option -g default-command "reattach-to-user-namespace -l $SHELL"

	# Key Bindings
	tmux bind-key -t vi-copy Enter copy-pipe "pbcopy"
	tmux bind-key -t vi-copy y     copy-pipe "pbcopy"
	tmux bind-key ] run-shell "pbpaste | tmux load-buffer - && tmux paste-buffer"

    # Enable native Mac OS X copy/paste
    set-option -g default-command "/bin/bash -c 'which reattach-to-user-namespace >/dev/null && exec reattach-to-user-namespace $SHELL -l || exec $SHELL -l'"

    # Disable assume-paste-time, so that iTerm2's "Send Hex Codes" feature works
    # with tmux 2.1. This is backwards-compatible with earlier versions of tmux,
    # AFAICT.
    set-option -g assume-paste-time 0

	;;
Linux)
	# Disable terminal clipboard when using gnome-terminal;
	# see: http://askubuntu.com/a/507215.
	tmux set-option -g set-clipboard off

	# Key Bindings
	tmux bind-key -t vi-copy Enter copy-pipe "xsel -i -b"
	tmux bind-key -t vi-copy y     copy-pipe "xsel -i -b"
	tmux bind-key ] run-shell "xsel -o -b | tmux load-buffer - && tmux paste-buffer"
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
