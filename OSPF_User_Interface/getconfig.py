from napalm import get_network_driver
import json
import os
import datetime
import time


def get_config(ios_router, router):
	driver = get_network_driver('ios')
	iosv12 = driver(**ios_router)
	iosv12.open()
	out = iosv12.get_config()
	out1 = json.dumps(out, indent=4)
	ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H:%M:%S')
	file_name = router + "_" + ts + ".txt"
	f = open(file_name, 'w')
	f.write(out1)
	#files.append(file_name)
	#print(files)
	iosv12.close()
	return file_name


def main():
	files = []
	if os.path.isfile('sshInfo.json'):
		fh = open('sshInfo.json', 'r')
		ssh_data = json.load(fh)
		#print(ssh_data)
		rout = ["R1", "R2", "R3", "R4"]
		for item in rout:
			filenames = get_config(ssh_data[item], item)
			files.append(filenames)
		return files
	else:
		print("file not found")
