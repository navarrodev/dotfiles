" ativar sintaxe colorida
syntax on

" ativar indentação automática
set autoindent

" ativa indentação inteligente, o Vim tentará adivinhar qual é a melhor indentação para o código quando você
" efetuar quebra de linha. Funciona bem para linguagem C
set smartindent

" por padrão o vim armazena os últimos 50 comandos que você
" digitou em seu histórico. Eu sou exagerado, prefiro armazenar
" os últimos 5000
set history=5000

" ativar numeração de linha
set number

" destaca a linha em que o cursor está posicionado
" ótimo para quem não enxerga muito bem
set cursorline

" ativa o clique do mouse para navegação pelos documentos
set mouse=a

" ativa o compartilhamento de área de transferência entre o Vim
" e a interface gráfica
set clipboard=unnamedplus

" converte o tab em espaços em branco
" ao teclar tab o Vim irá substituir por 2 espaços
set tabstop=2 softtabstop=2 expandtab shiftwidth=2

" ao teclar a barra de espaço no modo normal, o Vim
" irá colapsar ou expandir o bloco de código do cursor
" foldlevel é a partir de que nível de indentação o
" código iniciará colapsado
set foldmethod=syntax
set foldlevel=99
nnoremap <space> za

">>> Esquema de Cores
" set Vim-specific sequences for RGB colors
let &t_8f = "\<Esc>[38;2;%lu;%lu;%lum"
let &t_8b = "\<Esc>[48;2;%lu;%lu;%lum"
colorscheme orbital

">>>> Linhas de indentação
let g:indentLine_enabled = 1
map <c-k>i :IndentLinesToggle<cr>

">>>>> Navegador de Arquivos

map <C-n> :NERDTreeToggle<cr>
set encoding=utf8

">>>>>>>> Fonte para o Nerd-tree

set guifont="Fira Code Retina":h12

">>>>> Barra Airline

set laststatus=2
let g:airline#extensions#tabline#enabled = 1
let g:airline_powerline_fonts = 1
let g:airline_statusline_ontop=0
let g:airline_theme='light'

let g:airline#extensions#tabline#formatter = 'default'
" navegação entre os buffers
nnoremap <M-Right> :bn<cr>
nnoremap <M-Left> :bp<cr>
nnoremap <c-x> :bp\|bd #<cr>

">>>>>> Análise de Código
let g:ale_linters = {'python': ['flake8', 'pylint'], 'javascript': ['eslint'], 'html': ['htmlhint'], 'css': ['stylelint']} 
let g:ale_completion_enabled = 0
let g:ale_fixers = {'html': ['prettier']}
let g:ale_fixers.python = ['black']
let g:ale_linters_explicit = 1
let g:ale_fix_on_save = 1
">>>>>>>>COC
source ~/.vim/coc.nvimrc

">>>>>ExecutarPython
map <F5> <Esc>:w<CR>:!clear;python3 %<CR>

">>> Cores
set term=xterm-256color

">>>> Alternando Linhas
nnoremap <silent> <M-Down> :m +1<CR>
nnoremap <silent> <M-Up> :m -2<CR>

">>>>>>>> Copiar com Ctrl+C
vnoremap <c-c> "+y<CR>


">>>>>>>> Prettier
packloadall

">>>>>>>>>>>> FZF
set rtp+=~/.fzf

">>>> NerdCommenter
filetype plugin on
let g:NERDSpaceDelims = 1
let g:NERDDefaultAling = 'left'
map cc <Plug>NERDCommenterInvert


">>>>>>>>>>>>
set incsearch


">>>>>>>
let g:ctrlp_custom_ignore = '\v[\/]\.(swp|zip)$'
let g:ctrlp_user_command = ['.git', 'cd %s && git ls-files -co --exclude-standard']
let g:ctrlp_show_hidden = 1
