#!/bin/bash


IFS='/' read -r -a array <<< "$SHELL"
rc_path="$HOME/.${array[-1]}rc"


if ! type poetry > /dev/null 2>&1
then
    echo "Installing poetry"
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
    echo '' >> ${rc_path}
    echo '# poetry' >> ${rc_path}
    echo 'export PATH="$HOME/.poetry/bin:$PATH"' >> ${rc_path}
    echo "Poetry successfully installed"
    export PATH="$HOME/.poetry/bin:$PATH"
    echo "Restart the shell to use poetry"
fi


package_dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd ${package_dir}


poetry config virtualenvs.create false --local


if ! poetry check > /dev/null 2>&1
then
    echo "Initialize virtual environment"
    poetry init
    echo "Virtual environment created"
else
    echo "Valid pyproject.toml exists"
fi


if poetry install
then
    echo "Successfully installed the dependencies"
else
    echo "====================================="
    echo "- Installation failed, try updating -"
    echo "====================================="

    if poetry update
    then
        echo "Successfully updated the dependencies"
    else
        echo "========================================="
	echo "- poetry failed to resolve dependencies -"
        echo "========================================="
    fi
fi

