# Simbotic
## Simulation Engine for Multi-Agent Autonomy


![Alt text](Assets/capture.png?raw=true "Simbotic Simulation Engine")

## Setup Instructions

### Install UnrealEngine

```
git clone -b 4.21 git@github.com:EpicGames/UnrealEngine.git
cd UnrealEngine
./Setup.sh
./GenerateProjectFiles.sh
make
```

For more info visit [Building on Linux](https://wiki.unrealengine.com/Building_On_Linux).

### Git Large File Storage (Git LFS)

```
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
git lfs install
```

For more info visit [Git LFS](https://git-lfs.github.com/)

### Setup Simbotic (this repo)

Clone repo:
```
git clone git@github.com:VertexStudio/Simbotic.git --recursive
```

Environment variables:

```
export SIMBOTIC_UE4=/path/to/UE4_21
export SIMBOTIC_ROOT=/path/to/Simbotic
```

Generate project files and build:
```
cd $SIMBOTIC_ROOT
./generate.sh
./build_airsim.sh
./build.sh
```

Run sim:
```
./run.sh
```

Debug sim:
```
./debug.sh
```


### Test simulation script

First time setup:
```
pip install msgpack-rpc-python
```

Modify `$SIMBOTIC_ROOT/Config/AirSim/settings.json` to configure the simulation. By default it looks like the following:
```
{
  "SettingsVersion": 1.2,
  "SimMode": "Multirotor",
  "Vehicles": {
    "Drone1": {
      "VehicleType": "SimpleFlight",
      "X": 4,
      "Y": 0,
      "Z": -2,
      "Yaw": -180
    },
    "Drone2": {
      "VehicleType": "SimpleFlight",
      "X": 8,
      "Y": 0,
      "Z": -2
    }
  }
}
```

To point to a different `settings.json` edit `run.sh`.

For more info visit [AirSim Settings](https://github.com/Microsoft/AirSim/blob/master/docs/settings.md)

Run Simbotic and hit Play in Editor, then
Run script:

```
cd $SIMBOTIC_ROOT/Scripts/Python
python3 multiagent.py
```

For C++ example check out: [Multirotor](https://github.com/VertexStudio/AirSim/blob/3cff53b172fc1a3edd373d257f451dd388091799/Multirotor/main.cpp).

For more info visit [AirSim APIs](https://github.com/Microsoft/AirSim/blob/master/docs/apis.md)

### Aditional Info

[AirSim Docs](https://github.com/Microsoft/AirSim/tree/master/docs)
