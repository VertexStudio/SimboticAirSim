#!/usr/bin/env bash

# Location of the AirSim settings.json
SIMBOTIC_SETTINGS_PATH="$SIMBOTIC_ROOT"/Config/AirSim

"$SIMBOTIC_UE4"/Engine/Binaries/Linux/UE4Editor "$SIMBOTIC_ROOT"/Simbotic.uproject --airsim "$SIMBOTIC_SETTINGS_PATH"
