#!/usr/bin/env bash
echo "Generating Simbotic project files"
echo "----------------------"
"$SIMBOTIC_UE4"/GenerateProjectFiles.sh -project="$SIMBOTIC_ROOT"/Simbotic.uproject -game -engine -Makefile -vscode
