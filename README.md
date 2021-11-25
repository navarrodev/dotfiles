# Configurações Pessoais

Aqui são apenas meus dotfiles(arquivos de configuração do meu sistema pessoal ArchLinux, coisas como configurações do VIM, ambiente de terminal etc..

# Tutorial Rápido

Todo mundo já passou pela deliciosa situação de ter que reinstalar o SO por alguma eventualidade e BOOM, tralhas e mais tralhas que você usa no dia a dia, tem que ser reinstaladas e reconfiguradas Powerline, VScode e seus 450 plugins, Atom, Sublimetext e no meu caso o VIM, além disso os softwares base ambientes virtuais, configurações do ZSH ou Tmux, i3wm e por aí vai, UFA!

Bom eu uso ArchLinux então existem diversas soluções para isto eu gosto de uma bem simples e "KISS" (Keep is simple stupid). a única coisa que precisamos é o git instalado e 3 linhas de comando.

#### `git init --bare $HOME/.presets`


Com esse comando você inicializa um repositório local vazio que no caso é no meu home com o nome de `.presets`. Esse repositório vai rastrear os nossos arquivos que pretendemos guardar.

#### `alias preset='/usr/bin/git --git-dir=$HOME/.presets/ --work-tree-$HOME'`

Aqui criamos um alias preset para ele interagir apenas com nosso repósitorio de configuração.

#### `preset config --local status.showUntrackedFiles no`

Aqui vamos criar uma flag(sinalizador) para que não seja listados arquivos não rastreados.

#### `echo "alias preset='/usr/bin/git --git-dir$HOME/.presets/ --work-tree=$HOME'" >> $HOME/.zshrc`

Em seguida opcinalmente crio um alias no meu zshrc pra ter esse "atalho" pra todo shell aberto. Agora qualquer arquivo na sua $HOME pode ser "versinado" com o git. No caso eu estou usando o alias preset, digamos para adicionar o arquivo ".vimrc" o comando ficaria assim:

#### `preset add .vimrc`

Agora é só fazer o commit e o push para seu repositório no GitHub por exemplo, as maiores vantagens desse método é que não precisa de nada além do git instalado e pode reconfigurar sua máquina ou servidor rapidamente com apenas alguns comandos, além do que nosso repositório vazio vai ignorar outros repositórios que você casualmente mantenha em seu sistema.

Aqui foi só uma pequena amostra do que podemos fazer com o git, mas acho que pode ser útil principalmente para usuários Linux, uma solução para usuários Windows seria MUDAR PARA O LINUX kkkk.
