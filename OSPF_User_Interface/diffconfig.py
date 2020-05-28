import os
import json
import diffios
from pprint import pprint
from napalm import get_network_driver


def main():
	### Get the config files saved from getconfig function ###
	file_list = []
	dir_path = os.path.dirname(os.path.realpath(__file__))
	lis = os.listdir(dir_path)
	for i in range (1,5):
		for item in lis:
			if "R"+str(i) in item:
				file_list.append(item)

	
	### SSH connection to routers ###
	if os.path.isfile('sshInfo.json'):
		fh = open('sshInfo.json', 'r')
		ssh_data = json.load(fh)
		print(ssh_data)
		for items in file_list:
			rout = ["R1", "R2", "R3", "R4"]
			for item in rout:
				if item in items:
					#print(item + ":" + items + " " + "yass")
					driv = get_network_driver('ios')
					iosv = driv(ssh_data[item]["hostname"], ssh_data[item]["username"], ssh_data[item]["password"])
					iosv.open()
					fh = open('config.txt', 'w')
					out = str(iosv.get_config())
					#for k,v in out.items():
						#fh.write(k + ":" + v)
					fh.write(out)
					fh.close()
					diff = diffios.Compare('config.txt', items)
					print(diff.pprint_missing())
					iosv.close()
	
