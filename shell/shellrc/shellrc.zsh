CURR_FILE_DIR="$(cd "$(dirname "${(%):-%N}" )" && pwd )"
source ${CURR_FILE_DIR}/shellrc.generic

if exist tmuxinator; then
	source ${CURR_FILE_DIR}/tmuxinator.zsh
fi

unset CURR_FILE_DIR
