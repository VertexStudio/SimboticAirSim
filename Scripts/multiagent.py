#import setup_path 
import airsim

import numpy as np
import os
import tempfile
import pprint

# Use below in settings.json with Blocks environment
"""
{
	"SeeDocsAt": "https://github.com/Microsoft/AirSim/blob/master/docs/settings.md",
	"SettingsVersion": 1.2,
	"SimMode": "Multirotor",
	"ClockSpeed": 1,
	
	"Vehicles": {
		"agent.o": {
		  "VehicleType": "SimpleFlight",
		  "X": 4, "Y": 0, "Z": -2
		},
		"agent.1": {
		  "VehicleType": "SimpleFlight",
		  "X": 8, "Y": 0, "Z": -2
		}

    }
}
"""

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True, "agent.0")
client.enableApiControl(True, "agent.1")
client.armDisarm(True, "agent.0")
client.armDisarm(True, "agent.1")

airsim.wait_key('Press any key to takeoff')
f1 = client.takeoffAsync(vehicle_name="agent.0")
f2 = client.takeoffAsync(vehicle_name="agent.1")
f1.join()
f2.join()

state1 = client.getMultirotorState(vehicle_name="agent.0")
s = pprint.pformat(state1)
print("state: %s" % s)
state2 = client.getMultirotorState(vehicle_name="agent.1")
s = pprint.pformat(state2)
print("state: %s" % s)

airsim.wait_key('Press any key to move vehicles')
f1 = client.moveToPositionAsync(-5, 5, -10, 5, vehicle_name="agent.0")
f2 = client.moveToPositionAsync(5, -5, -10, 5, vehicle_name="agent.1")
f1.join()
f2.join()

airsim.wait_key('Press any key to take images')
# get camera images from the car
responses1 = client.simGetImages([
    airsim.ImageRequest("0", airsim.ImageType.DepthVis),  #depth visualization image
    airsim.ImageRequest("1", airsim.ImageType.Scene, False, False)], vehicle_name="agent.0")  #scene vision image in uncompressed RGBA array
print('agent.0: Retrieved images: %d' % len(responses1))
responses2 = client.simGetImages([
    airsim.ImageRequest("0", airsim.ImageType.DepthVis),  #depth visualization image
    airsim.ImageRequest("1", airsim.ImageType.Scene, False, False)], vehicle_name="agent.1")  #scene vision image in uncompressed RGBA array
print('agent.1: Retrieved images: %d' % len(responses2))

tmp_dir = os.path.join(tempfile.gettempdir(), "airsim_drone")
print ("Saving images to %s" % tmp_dir)
try:
    os.makedirs(tmp_dir)
except OSError:
    if not os.path.isdir(tmp_dir):
        raise

for idx, response in enumerate(responses1 + responses2):

    filename = os.path.join(tmp_dir, str(idx))

    if response.pixels_as_float:
        print("Type %d, size %d" % (response.image_type, len(response.image_data_float)))
        airsim.write_pfm(os.path.normpath(filename + '.pfm'), airsim.get_pfm_array(response))
    elif response.compress: #png format
        print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
        airsim.write_file(os.path.normpath(filename + '.png'), response.image_data_uint8)
    else: #uncompressed array
        print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
        img1d = np.fromstring(response.image_data_uint8, dtype=np.uint8) #get numpy array
        img_rgba = img1d.reshape(response.height, response.width, 4) #reshape array to 4 channel image array H X W X 4
        img_rgba = np.flipud(img_rgba) #original image is flipped vertically
        img_rgba[:,:,1:2] = 100 #just for fun add little bit of green in all pixels
        airsim.write_png(os.path.normpath(filename + '.greener.png'), img_rgba) #write to png

airsim.wait_key('Press any key to reset to original state')

client.armDisarm(False, "agent.0")
client.armDisarm(False, "agent.1")
client.reset()

# that's enough fun for now. let's quit cleanly
client.enableApiControl(False, "agent.0")
client.enableApiControl(False, "agent.1")


