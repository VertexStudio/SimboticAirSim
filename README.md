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

### Get Simbotic (this repo)

```
git clone git@github.com:VertexStudio/Simbotic.git --recursive
```

### Test multi-agent script

First time setup:
```
pip install msgpack-rpc-python
```

Create or modify `~/Documents/AirSim/settings.json` to configure simulation:
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
For more info visit [AirSim Settings](https://github.com/Microsoft/AirSim/blob/master/docs/settings.md)

Run script:

```
cd Simbotic/Scripts/Python
python python multiagent.py
```

For more info visit [AirSim APIs](https://github.com/Microsoft/AirSim/blob/master/docs/apis.md)

### Aditional Info

[AirSim Docs](https://github.com/Microsoft/AirSim/tree/master/docs)
