CURR_FILE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd )"

pushd () {
    command pushd "$@" > /dev/null
}

popd () {
    command popd "$@" > /dev/null
}

alias cd=pushd

source ${CURR_FILE_DIR}/shellrc.generic

if exist tmuxinator; then
	source ${CURR_FILE_DIR}/tmuxinator.bash
fi

unset CURR_FILE_DIR
