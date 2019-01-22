#!/usr/bin/env bash
SIMBOTIC_SETTINGS_PATH=$1

"$SIMBOTIC_UE4"/Engine/Binaries/Linux/UE4Editor "$SIMBOTIC_ROOT"/Simbotic.uproject --airsim "$SIMBOTIC_SETTINGS_PATH"
