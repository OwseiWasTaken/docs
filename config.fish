set fish_greeting ""
sudo cp /home/owsei/Documents/py/util.py /usr/lib/python3.9/util.py
sudo swapoff -a
cd /home/owsei/.config/fish
# hamachi
# /etc/init.d/logmein-hamachi start
# colors
# res = 1680 x 1050
set -g black (set_color black)
set -g red (set_color red)
set -g green (set_color green)
set -g yellow (set_color yellow)
set -g blue (set_color blue)
set -g magenta (set_color magenta)
set -g cyan (set_color cyan)
set -g white (set_color white)
set -g BrBlack (set_color brblack)
set -g BrRed (set_color brred)
set -g BrGreen (set_color brgreen)
set -g BrYellow (set_color bryellow)
set -g BrBlue (set_color brblue)
set -g BrMagenta (set_color brmagenta)
set -g BrCyan (set_color brcyan)
set -g BrWhite (set_color brwhite)
set -g normal (set_color normal)
set -g nc $normal

set -g CppFile

#aliases
#
#
#

alias temp "/home/owsei/Documents/py/temp.py"
alias StalkerKill "pkill XR_3DA.exe"
alias ytdown "/home/owsei/Documents/py/ytdown.py"
alias vs "code"
alias netspeed "speedtest-cli"
alias ... "cd ../.."
alias stt "/home/owsei/Documents/py/stt.py"
alias tmp "nvim ~/tmp"
alias clock "/home/owsei/Documents/py/clock.py"
alias own "sudo chown owsei -R ~"
alias todo "~/Documents/py/todo2.py"
alias naut "nautilus ."
alias ls "ls --color=auto -Fa"
#alias cap "~/Documents/py/cap.py $argv"
alias cap "~/Documents/py/mkf.py "
alias mkf "~/Documents/py/mkf.py "
alias ref "source ~/.config/fish/config.fish"
alias py "python3.9"
alias py8 "python3.8"
alias pyl "cd /usr/lib/python3.9/"
alias util "/home/owsei/Documents/py/util.py"
alias amod "nvim /home/owsei/.config/alacritty/alacritty.yml"
#alias asm "nasm -f elf32 -o program.obj $argv.asm;ld -m elf_i386 -o $argv.run program.obj; rm program.obj"
alias asm "/home/owsei/Documents/py/asm.py"
alias dl "/home/owsei/Documents/bin/dado" # in /usr/bin/d so alias is not needed


alias mc "mc --nosubshell" 
alias rcase "/home/owsei/Documents/py/rcase.py"
# ProgramminD
alias jsd "cd /home/owsei/Documents/js"
alias csd "cd /home/owsei/Documents/cs"
alias pyd "cd /home/owsei/Documents/py"
alias jld "cd /home/owsei/Documents/jl"
alias cpd "cd /home/owsei/Documents/cp"
alias fcd "cd /home/owsei/Documents/py/FCP"
alias asd "cd /home/owsei/Documents/asm"
alias ncd "cd /home/owsei/Documents/nc"

# cmd acts
alias cat "batcat"
alias ocat "/bin/cat"
alias cod "code -g ~/Documents/"
alias mod "code ~/.config/fish/config.fish"
alias tmod "nvim ~/.config/fish/config.fish ; ref"
abbr instl "sudo apt install"
abbr sinstl "sudo snap install"
abbr aptrm "sudo apt remove"
abbr saptrm "sudo snap remove"
alias updt "sudo apt update ; sudo apt upgrade ; sudo apt autoremove ; clear"
alias l "ls --color=yes -FA"
alias :wq "exit"
alias :q "exit"

#sets
set -g UseRightPrompt 1
set USER "owsei"
set -g NVIM_TUI_ENABLE_TRUE_COLOR 1



# exports
export NVIM_TUI_ENABLE_TRUE_COLOR


# dirs
alias vids "cd ~/Videos"
alias docs "cd ~/Documents"
alias down "cd ~/Downloads"
alias pics "cd ~/Pictures"
alias desk "cd ~/Desktop"
alias temp "cd /tmp"

# function preexec_test --on-event fish_preexec
	# set -g start 
# end

# function postexec_test --on-event fish_postexec
# end

function fish_right_prompt
	# set -l FishVer (fish --version)
	# set -l FishVer (string replace 'fish, version ' '' $yeet)
	set -l Mem (/home/owsei/Documents/py/GetMemory.py)
	set -l time (date)
	echo $Mem
	# $time
end

# fish prompt

source fish_prompt.fish

# > instl ssh
# > sudo systemctl status ssh
# > sudo systemctl start ssh
# > sudo systemctl stop ssh
# > sudo ufw allow ssh
# > sudo ufw enable
# > sudo ufw status
# > sudo ufw disable


# remmina : connect to "Owsei-Lenovo-Ubuntu"



# cowsay "hi" and clear
cd /home/owsei
clear

# cowsay:
# apt bud-frogs bunny calvin cheese cock cower daemon default dragon dragon-and-cow duck elephant elephant-in-snake eyes flaming-sheep fox ghostbusters gnu hellokitty kangaroo kiss koala kosh luke-koala mech-and-cow milk moofasa moose pony pony-smaller ren sheep skeleton snowman stegosaurus stimpy suse three-eyes turkey turtle tux unipony unipony-smaller vader vader-koala www
# 44 elements (+ pony, unipony)
# awk random number gen
#set -l element (awk -v min=1 -v max=44 'BEGIN{srand(); print int(min+rand()*(max-min+1))}')

# (my) c++ random number gen 
set -l element (d 1 44)
set -l things apt bud-frogs bunny calvin cheese cock cower daemon default dragon dragon-and-cow duck elephant elephant-in-snake eyes flaming-sheep fox ghostbusters gnu hellokitty kangaroo kiss koala kosh luke-koala mech-and-cow milk moofasa moose pony-smaller ren sheep skeleton snowman stegosaurus stimpy suse three-eyes turkey turtle tux unipony-smaller vader vader-koala www
set -l CowFile $things[$element]
cowsay -f $CowFile "o/ owsei" | lolcat


#https://www.coursera.org/learn/python-crash-course%20%20
#https://vim.rtorr.com
