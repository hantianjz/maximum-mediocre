
alias x2e='source ~/x2_debug_board/pyenv; python -c "from x2_debug_board import X2DebugBoard; X2DebugBoard(timeout=5).reboot_to_edl()"; deactivate'
alias x2ex='source ~/x2_debug_board/pyenv; python -c "from x2_debug_board import X2DebugBoard; X2DebugBoard(timeout=5).edl_disable()"; deactivate'
alias x2hb='source ~/x2_debug_board/pyenv; python -c "from x2_debug_board import X2DebugBoard; X2DebugBoard(timeout=5)._send_cmd(\"hodor_press 3000\")"; deactivate'
