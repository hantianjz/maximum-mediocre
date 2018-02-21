CURR_FILE_DIR="$(cd "$(dirname "${(%):-%N}" )" && pwd )"
source ${CURR_FILE_DIR}/shellrc.generic
unset CURR_FILE_DIR

if exist tmuxinator; then
	source ${CURR_FILE_DIR}/tmuxinator.zsh
fi
