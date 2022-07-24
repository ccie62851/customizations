#!/usr/bin/python3
import os
import re
from pathlib import Path

home_dir = Path.home()
oh_my_zsh_path = f'{home_dir}/.oh-my-zsh/'
zshrc_file = f'{home_dir}/.zshrc'
vimrc_file = f'{home_dir}/.vimrc'
vim_path = f'{home_dir}/.vim/'
vim_color_path = f'{vim_path}colors/'
vim_autoload_path = f'{vim_path}autoload/'
zsh_plugin_path = f'{oh_my_zsh_path}custom/plugins/zsh-autosuggestions'
plugins = '''plugins=( 
    git
    zsh-autosuggestions
)
'''
#zsh_setup
if not os.path.isdir(oh_my_zsh_path):
    print("Oh-MY-ZSH is not installed, Installing\n")
    oh_my_zsh_cmd = 'sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"'
    os.system(oh_my_zsh_cmd)
if not os.path.isdir(zsh_plugin_path):
    print("Installing zsh-autosuggestions\n")
    auto_suggestion_cmd = 'git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions'
    os.system(auto_suggestion_cmd)

print("Updating 'gnzh' as default Oh-MY-ZSH theme\n")
with open(zshrc_file, 'r') as file:
    data = file.read()
data = re.sub(r'ZSH_THEME.*', 'ZSH_THEME="gnzh"', data)
data = re.sub(r'plugins=\(git\)', plugins, data)
with open(zshrc_file, 'w') as file:
    file.write(data)
os.system(f'zsh && source {zshrc_file}')

# vim setup
theme_name = 'onedark.vim'
color_url = 'https://raw.githubusercontent.com/joshdick/onedark.vim/main/colors/onedark.vim'
autoload_url = 'https://raw.githubusercontent.com/joshdick/onedark.vim/main/autoload/onedark.vim'

print("Checking VIM Setup\n")
if not os.path.isdir(vim_path):
    print(f"Creating {vim_path}")
    os.system(f'mkdir {vim_path}')
if not os.path.isdir(vim_color_path):
    print(f"Creating {vim_color_path}")
    os.system(f'mkdir {vim_color_path}')
if not os.path.isdir(vim_autoload_path):
    print(f"Creating {vim_autoload_path}")
    os.system(f'mkdir {vim_autoload_path}')


print("\nDownloading VIM Theme files\n")
os.system(f'curl -o {vim_color_path}{theme_name} {color_url}')
os.system(f'curl -o {vim_autoload_path}{theme_name} {autoload_url}')

if not os.path.isfile(vimrc_file):
    print(f"Creating {vimrc_file}")
    os.system(f'touch {vimrc_file}')

with open(vimrc_file, "w") as file_object:
    print(f"Updating theme in {vimrc_file}")
    file_object.write("syntax on\ncolorscheme onedark")