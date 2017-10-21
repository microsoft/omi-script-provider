#!/bin/bash

function check_omi {
    echo "Checking if OMI directory exists"
    OMI_FOUND=0
    if [ -d "$START_DIR/../omi" ]; then
        OMI_FOUND=1
    fi
}

function check_built_omi {
    echo "Checking if OMI directory has been built before"
    OMI_BUILT=0;
    pushd $START_DIR/../omi/Unix >/dev/null
    if [ -d "output" ]; then
        cd output
        if [ -d "bin" ]; then
            cd bin
            #count all files in current directory
            FILE_COUNT=`ls -1 . 2>/dev/null | wc -l`
            FILE_FOUND="0"

            echo "Checking if output directory contains all the built binaries"
            for f in chkshlib mkdep nits_debug_build_sample nits_hook_build_sample omiagent omicli omiengine omigen_py omireg strhash DogPreExec nits nits_default_linkage_sample oigenc omicheck omiconfigeditor omigen omiserver; do
                #check if file is present in current directory
                if [ -f "$f" ]; then
                    echo "Binary $f was found ... yes"
                    FILE_FOUND=$((FILE_FOUND+1))
                else
                    echo "Binary $f was found ... NO!"
                fi
            done

            #check if files found is same as files counted
            if [ "$FILE_COUNT" -eq "$FILE_FOUND" ]; then
                OMI_BUILT=1
            else
                echo "Error; non matching number of output binaries; found $FILE_FOUND/$FILE_COUNT"
            fi
        fi
    fi
    popd >/dev/null
}

function pull_omi {
    pushd $START_DIR/.. >/dev/null
    echo "Cloning OMI in parent directory"
    git clone https://github.com/Microsoft/omi --depth 1
    popd >/dev/null
}

function build_omi {
    check_omi
    if [ "$OMI_FOUND" -eq "0" ]; then
        echo "OMI directory not found"
        pull_omi
    else
        echo "OMI directory found"
    fi

    check_built_omi
    if [ "$OMI_BUILT" -eq "0" ]; then
        pushd $START_DIR/../omi/Unix >/dev/null

        echo "Building OMI"
        ./configure --dev --outputdirname=output
        make
        make install

        popd >/dev/null
    else
        echo "OMI was built before"
    fi
}

function copy_version_file {
    pushd $START_DIR/.. >/dev/null
    echo "Cloning Build OMI script provider repository"
    git clone https://github.com/Microsoft/Build-omi-script-provider --depth 1
    cd Build-omi-script-provider
    cp omiscriptprovider.version ..
    cd ..
    rm -rf Build-omi-script-provider
    popd >/dev/null
}

START_DIR=`pwd`
cd ..
if [ -d "omi-script-provider" ]; then
    mv omi-script-provider scriptprovider
    cd scriptprovider
else
    cd $START_DIR
fi

START_DIR=`pwd`
build_omi

copy_version_file

echo "Building OMI Python Script provider"
export CPPFLAGS="-fpermissive"
./configure
make
sudo make install
