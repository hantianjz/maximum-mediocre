" don't bother with vi compatibility
set nocompatible

" enable syntax highlighting
syntax enable

" configure Vundle
filetype on " without this vim emits a zero exit status, later, because of :ft off
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" install Vundle bundles
if filereadable(expand("~/.vimrc.bundles"))
    source ~/.vimrc.bundles
 endif

call vundle#end()

" ensure ftdetect et al work by including this after the Vundle stuff
filetype plugin indent on

set autoindent
set cindent
set cino=(0
set autoread                                                 " reload files when changed on disk, i.e. via `git checkout`
set backspace=2                                              " Fix broken backspace in some setups
set backupcopy=yes                                           " see :help crontab
set clipboard=unnamedplus                                        " yank and paste with the system clipboard
set directory-=.                                             " don't store swapfiles in the current directory
set encoding=utf-8
set expandtab                                                " expand tabs to spaces
set ignorecase                                               " case-insensitive search
set incsearch                                                " search as you type
set laststatus=2                                             " always show statusline
set list                                                     " show trailing whitespace
set listchars=tab:▸\ ,trail:▫
"set number                                                   " show line numbers
"set relativenumber                                           " show relative line numbers
set ruler                                                    " show where you are
set scrolloff=3                                              " show context above/below cursorline
set shiftwidth=4                                             " normal mode indentation commands use 4 spaces
set showcmd
set smartcase                                                " case-sensitive search if any caps
set softtabstop=4                                            " insert mode tab and backspace use 4 spaces
set tabstop=4                                                " actual tabs occupy 8 characters
set wildignore=log/**,node_modules/**,target/**,tmp/**,*.rbc
set wildmenu                                                 " show a navigable menu for tab completion
set wildignore+=*/tmp/*,*.so,*.o,*.swp,*.zip
set timeoutlen=1000 ttimeoutlen=0
set nohlsearch                                               " Disable seach highlight

" Enable basic mouse behavior such as resizing buffers.
set mouse=a
" if exists('$TMUX')  " Support resizing in tmux
"   set ttymouse=xterm2
" endif

set background=dark

" keep a copy of last edit
" if this throws errors, make sure the backup dir exists
set backup
set backupdir=~/.vim/backup/

" keyboard shortcuts
let mapleader = '\'
" noremap <C-h> <C-w>h
" noremap <C-j> <C-w>j
" noremap <C-k> <C-w>k
" noremap <C-l> <C-w>l

let g:tmux_navigator_no_mappings = 1
nnoremap <silent> <C-h> :TmuxNavigateLeft<cr>
nnoremap <silent> <C-j> :TmuxNavigateDown<cr>
nnoremap <silent> <C-k> :TmuxNavigateUp<cr>
nnoremap <silent> <C-l> :TmuxNavigateRight<cr>
nnoremap <silent> <C-p> :TmuxNavigatePrevious<cr>

noremap <leader>l :Align
nnoremap <leader>a :Ag<space>
" nnoremap <leader>b :CtrlPBuffer<CR>
nnoremap <leader>d :NERDTreeToggle<CR>
nnoremap <leader>f :NERDTreeFind<CR>
" nnoremap <leader>t :CtrlP<CR>
nnoremap <leader>t :FZF<CR>
" nnoremap <leader>] :TagbarToggle<CR>
nnoremap <leader><space> :call whitespace#strip_trailing()<CR>
nnoremap <leader>c <Plug>Kwbd

nmap s <Plug>(easymotion-overwin-f2)

" in case you forgot to sudo
cnoremap w!! %!sudo tee > /dev/null %

" plugin settings
" let g:ctrlp_match_window = 'order:ttb,max:20'
let g:NERDSpaceDelims=1
let g:gitgutter_enabled = 0

" Use The Silver Searcher https://github.com/ggreer/the_silver_searcher
if executable('ag')
  let g:ackprg = 'ag -i --nogroup --column'

  " Use Ag over Grep
  set grepprg=ag\ --nogroup\ --nocolor

  " Use ag in CtrlP for listing files. Lightning fast and respects .gitignore
  " let g:ctrlp_user_command = 'ag %s -l --nocolor -g ""'
endif

autocmd BufRead,BufNewFile *.def set filetype=c
autocmd BufRead,BufNewFile *.ino set filetype=c
autocmd BufRead,BufNewFile *.i set filetype=c
autocmd BufRead,BufNewFile *.groovy set filetype=java
" fdoc is yaml
autocmd BufRead,BufNewFile *.fdoc set filetype=yaml
" md is markdown
autocmd BufRead,BufNewFile *.md set filetype=markdown
autocmd BufRead,BufNewFile *.md set spell
" extra rails.vim help
autocmd User Rails silent! Rnavcommand decorator      app/decorators            -glob=**/* -suffix=_decorator.rb
autocmd User Rails silent! Rnavcommand observer       app/observers             -glob=**/* -suffix=_observer.rb
autocmd User Rails silent! Rnavcommand feature        features                  -glob=**/* -suffix=.feature
autocmd User Rails silent! Rnavcommand job            app/jobs                  -glob=**/* -suffix=_job.rb
autocmd User Rails silent! Rnavcommand mediator       app/mediators             -glob=**/* -suffix=_mediator.rb
autocmd User Rails silent! Rnavcommand stepdefinition features/step_definitions -glob=**/* -suffix=_steps.rb
" automatically rebalance windows on vim resize
autocmd VimResized * :wincmd =

" Fix Cursor in TMUX
if exists('$TMUX')
  let &t_SI = "\<Esc>Ptmux;\<Esc>\<Esc>]50;CursorShape=1\x7\<Esc>\\"
  let &t_EI = "\<Esc>Ptmux;\<Esc>\<Esc>]50;CursorShape=0\x7\<Esc>\\"
else
  let &t_SI = "\<Esc>]50;CursorShape=1\x7"
  let &t_EI = "\<Esc>]50;CursorShape=0\x7"
endif

" Go crazy!
if filereadable(expand("~/.vimrc.local"))
  " In your .vimrc.local, you might like:
  "
  " set autowrite
  " set nocursorline
  " set nowritebackup
  " set whichwrap+=<,>,h,l,[,] " Wrap arrow keys between lines
  "
  " autocmd! bufwritepost .vimrc source ~/.vimrc
  " noremap! jj <ESC>
  source ~/.vimrc.local
endif

colorscheme mirodark

set cursorline
set cursorcolumn
set noswapfile
set tags=tags;/

"nnoremap <leader>jd :YcmCompleter GoToDefinitionElseDeclaration<CR>
"nnoremap <F5> :YcmForceCompileAndDiagnostics<CR>
let g:ycm_confirm_extra_conf = 0

let g:syntastic_quiet_messages = { "level": "warnings" }
let g:ycm_complete_in_comments = 1
let g:ycm_collect_identifiers_from_tags_files = 1
let g:ycm_autoclose_preview_window_after_completion = 1

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_error_symbol = '✗'
let g:syntastic_warning_symbol = '!'

let g:syntastic_c_no_default_include_dirs = 1
let g:syntastic_c_check_header = 1
let g:syntastic_c_include_dirs = [ 'inc', 'includes' ]
let g:syntastic_c_compiler = 'gcc'
let g:syntastic_c_compiler_options = '-DTARGET_WIN=0'
let g:syntastic_c_auto_refresh_includes = 1
let g:ycm_seed_identifiers_with_syntax = 1
let g:syntastic_enable_highlighting = 0

let g:syntastic_python_checkers=["flake8"]
let g:syntastic_python_flake8_args="--ignore=E501"
autocmd FileType c nnoremap <buffer> <silent> <C-]> :YcmCompleter GoTo<cr>

" let g:airline#extensions#tabline#enabled = 1

"let g:solarized_termcolors=256
" let g:ctrlp_regexp = 1
" let g:ctrlp_open_new_file = 't'

nnoremap <Leader>q :Bdelete<CR>
let g:ycm_global_ycm_extra_conf = '~/Development/maximum-awesome/ycm_conf/ycm_riker_conf.py'

let g:semanticTermColors = [28,1,2,3,4,5,6,7,25,9,10,34,12,13,14,15,125,124,19]
let g:semanticEnableFileTypes = ["c", "python", "cpp", "cmake"]
let g:semanticBlacklistOverride = {'c': ['define', 'typedef', 'struct', 'enum', 'for', 'if', 'static', 'void']}

" Vim hardmode
" autocmd VimEnter,BufNewFile,BufReadPost * silent! call HardMode()

nnoremap <leader>h <Esc>:call ToggleHardMode()<CR>

" EasyMotion
let g:EasyMotion_smartcase = 1

" FZF
set rtp+=~/.fzf
let g:fzf_nvim_statusline = 0 " disable statusline overwriting
let g:fzf_height = 10
let g:fzf_buffers_jump = 1

