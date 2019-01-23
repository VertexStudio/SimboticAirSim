#!/usr/bin/env bash

set -e

if [ -z "$(ls -A "./AirSim")" ]; then
   echo "AirSim is empty. Make sure to run 'git submodule init && git submodule update'"
fi

# check for libc++
if [[ ! (-d "./AirSim/llvm-build/output/lib") ]]; then
    # ERROR: clang++ and libc++ is necessary to compile AirSim and run it in Unreal engine
    # Running setup.sh first to fix the problem described above.
    ./AirSim/setup.sh
fi

# check for rpclib
if [ ! -d "./AirSim/external/rpclib/rpclib-2.2.1" ]; then
    # ERROR: new version of AirSim requires newer rpclib.
    # Running setup.sh first to fix the problem described above.
    ./AirSim/setup.sh
fi

# check for cmake build
if [ ! -d "./AirSim/cmake_build" ]; then
    # ERROR: cmake build was not found.
    # Running setup.sh first to fix the problem described above.
    ./AirSim/setup.sh    
fi

#install EIGEN library
if [[ ! (-d "./AirSim/AirLib/deps/eigen3/Eigen") ]]; then 
    # eigen is not installed.
    # Running setup.sh first to fix the problem described above.
    ./AirSim/setup.sh    
fi

# Building AirSim plugin.
./AirSim/build.sh

echo
echo "Updating AirSim plugin at Simbotic/Plugins"
rsync -a --delete ./AirSim/Unreal/Plugins/ ./Plugins/

echo 
echo -e -n "\xE2\x9C\x94 "
echo "AirSim plugin updated."
echo