CURR_FILE_DIR="$(cd "$(dirname "${(%):-%N}" )" && pwd )"
source ${CURR_FILE_DIR}/shellrc.generic
unset CURR_FILE_DIR
