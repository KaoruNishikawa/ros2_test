#!/bin/bash


if ! type poetry > /dev/null 2>&1
then
    echo "Installing poetry"
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
    echo '# poetry' >> ~/.bashrc
    echo '# poetry' >> ~/.zshrc
    echo 'export PATH="$HOME/.poetry/bin:$PATH"' >> ~/.bashrc
    echo 'export PATH="$HOME/.poetry/bin:$PATH"' >> ~/.zshrc
    echo "Poetry successfully installed"
fi


IFS='/' read -r -a array <<< "$SHELL"
source "$HOME/.${array[-1]}rc"


package_dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd ${package_dir}


poetry config virtualenvs.create false --local


if ! poetry check > /dev/null 2>&1
then
    poetry init
fi


if ! poetry install -q
then
    poetry update -q
fi

