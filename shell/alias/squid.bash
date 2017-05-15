
alias x2e='source ~/x2_debug_board/pyenv; python -c "from x2_debug_board import X2DebugBoard; X2DebugBoard(timeout=5).reboot_to_edl()"; deactivate'
alias x2ex='source ~/x2_debug_board/pyenv; python -c "from x2_debug_board import X2DebugBoard; X2DebugBoard(timeout=5).edl_disable()"; deactivate'
alias x2hb='source ~/x2_debug_board/pyenv; python -c "from x2_debug_board import X2DebugBoard; X2DebugBoard(timeout=5)._send_cmd(\"hodor_press 3000\")"; deactivate'

#Temp fix for python verification bug
export PYTHONHTTPSVERIFY=0

export BUILD_ENABLE_CCACHE=1


workonhodor() {
    pushd /data/$1/android
    source build/envsetup.sh
    lunch hodor_msm8916_64-userdebug
    popd
}
