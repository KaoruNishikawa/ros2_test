#!/bin/bash


IFS='/' read -r -a array <<< "$SHELL"
rc_path="$HOME/.${array[-1]}rc"


if ! type poetry > /dev/null 2>&1
then
    echo "Installing poetry"
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
    if grep '.poetry/bin' ${rc_path} > /dev/null 2>&1
    then
        echo -e "\033[46mPoetry path has already been set\033[0m"
    else
        echo -e "\033[46mSetting path in ${rc_path}\033[0m"
        echo '' >> ${rc_path}
        echo '# poetry' >> ${rc_path}
        echo 'export PATH="$HOME/.poetry/bin:$PATH"' >> ${rc_path}
        echo -e "\033[46;1mPoetry successfully installed\033[0m"
        export PATH="$HOME/.poetry/bin:$PATH"
        echo -e "\033[46mRestart the shell to use poetry\033[0m"
    fi
fi


package_dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd ${package_dir}


poetry config virtualenvs.create false --local


if ! poetry check > /dev/null 2>&1
then
    echo -e "\033[46mInitialize virtual environment\033[0m"
    poetry init
    echo -e "\033[46mVirtual environment created\033[0m"
else
    echo -e "\033[46mValid pyproject.toml exists\033[0m"
fi


if poetry install
then
    echo -e "\033[46;1m===========================================\033[0m"
    echo -e "\033[46;1m= Successfully installed the dependencies =\033[0m"
    echo -e "\033[46;1m===========================================\033[0m"
else
    echo -e "\033[46;1m=====================================\033[0m"
    echo -e "\033[46;1m= Installation failed, try updating =\033[0m"
    echo -e "\033[46;1m=====================================\033[0m"

    if poetry update
    then
        echo -e "\033[46;1m=========================================\033[0m"
        echo -e "\033[46;1m= Successfully updated the dependencies =\033[0m"
        echo -e "\033[46;1m=========================================\033[0m"
    else
        echo -e "\033[46;1m=========================================\033[0m"
	echo -e "\033[46;1m= poetry failed to resolve dependencies =\033[0m"
        echo -e "\033[46;1m=========================================\033[0m"
    fi
fi

