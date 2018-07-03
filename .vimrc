set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" Vundle START
Plugin 'VundleVim/Vundle.vim'
Plugin 'tpope/vim-fugitive'
Plugin 'flazz/vim-colorschemes'
Plugin 'valloric/youcompleteme'
Plugin 'scrooloose/nerdtree'
Plugin 'Xuyuanp/nerdtree-git-plugin'
Plugin 'itchyny/lightline.vim'

" Vundle END
call vundle#end()            " required
filetype plugin indent on    " required

" Backup
set nobackup
set nowritebackup

set number
syntax enable

"colorscheme OceanicNext
"colorscheme Monokai
colorscheme onedark
"colorscheme railscasts

" On pressing tab, insert 2 spaces
set expandtab
" show existing tab with 2 spaces width
set tabstop=2
set softtabstop=2
" when indenting with '>', use 2 spaces width
set shiftwidth=2

" ==== Buffers ====
nnoremap <F5> :buffers<CR>:buffer<Space>

" Buffers - explore/next/previous: Alt-F12, F12, Shift-F12.
nnoremap <silent> <M-F9> :buffers<CR>
nnoremap <silent> <F9> :bn<CR>
nnoremap <silent> <S-F9> :bp<CR>

nnoremap <Tab> :bnext<CR>
nnoremap <S-Tab> :bprevious<CR>

" set paste no ident
set paste

" nerdtree
nmap <silent> <F2> :NERDTreeToggle<CR>
let NERDTreeQuitOnOpen=1

set laststatus=2
" hide mode since we are using laststauts=2
set noshowmode
" add branch to statusline
let g:lightline = {
      \ 'active': {
      \   'left': [ [ 'mode', 'paste' ],
      \             [ 'gitbranch', 'readonly', 'filename', 'modified' ] ]
      \ },
      \ 'component_function': {
      \   'gitbranch': 'gitbranch#name'
      \ },
      \ }

" disable .viminfo files
let skip_defaults_vim=1
set viminfo=""

" resize Vsplit
nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l




