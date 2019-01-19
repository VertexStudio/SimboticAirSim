#!/usr/bin/env bash
echo "Generating Simbotic project files"
echo "----------------------"
$HOME/UE4_21/GenerateProjectFiles.sh -project=$(pwd)/Simbotic.uproject -game -engine -Makefile -vscode
