from napalm import get_network_driver
from prettytable import PrettyTable
from werkzeug.datastructures import ImmutableMultiDict
import validateIP
from netmiko import ConnectHandler
import ipaddress


def myprint(out, ipadd):
	for k,v in out.items():
		if k == 'ipv4':
			for key,val in v.items():
				ipadd.append(key)
		elif isinstance(v, dict):		
			myprint(v, ipadd)
	return ipadd


def interf(out):
	intf = []
	for k,v in out.items():
		#print(k)
		intf.append(k)
	return intf


def ospf_main(dict_data):	
	for i in range (1,5):
		ip_test = dict_data["host" + str(i)]
		user = dict_data["user" + str(i)]
		passw = dict_data["pass" + str(i)]
		proc_id = dict_data["pid" + str(i)]
		loopback = dict_data["loop" + str(i)]
		if i == 1:
			net1 = dict_data["net1_1"]
			net2 = dict_data["net1_2"]
			area1 = dict_data["area1_1"]
			comm = "router" + " " + "ospf" + " " + proc_id
			comm1 = "network" + " " + loopback + " " + "0.0.0.0" + " " + "area" + " " + area1
			comm2 = "network" + " " + net1 + " " + "area" + " " + area1
			comm3 = "network" + " " + net2 + " " + "area" + " " + area1
		if i == 2:
			net1 = dict_data["net2_1"]
			net2 = dict_data["net2_2"]
			area1 = dict_data["area2_1"]
			area2 = dict_data["area2_2"]
			comm = "router" + " " + "ospf" + " " + proc_id
			comm1 = "network" + " " + loopback + " " + "0.0.0.0" +" " + "area" + " " + area1
			comm2 = "network" + " " + net1 + " " + "area" + " " + area1
			comm3 = "network" + " " + net2 + " " + "area" + " " + area2
		if i == 3:
			net1 = dict_data["net3_1"]
			area1 = dict_data["area3_1"]
			comm = "router" + " " + "ospf" + " " + proc_id
			comm1 = "network" + " " + loopback + " " + "0.0.0.0" + " " + "area" + " " + area1
			comm2 = "network" + " " + net1 + " " + "area" + " " + area1
		if i == 4:
			net1 = dict_data["net4_1"]
			net2 = dict_data["net4_2"]
			area1 = dict_data["area4_1"]
			area2 = dict_data["area4_2"]
			comm = "router" + " " + "ospf" + " " + proc_id
			comm1 = "network" + " " + loopback + " " + "0.0.0.0" + "  " + "area" + " " + area1
			comm2 = "network" + " " + net1 + " " + "area" + " " + area1
			comm3 = "network" + " " + net2 + " " + "area" + " " + area2

		fh = open('ospf.cfg', 'w')
		fh.write(comm + "\n")
		fh.write(comm1 + "\n")
		fh.write(comm2 + "\n")
		if comm3:
			fh.write(comm3)
		fh.close()
		driv = get_network_driver('ios')
		iosv = driv(ip_test, user, passw)
		iosv.open()
		iosv.load_merge_candidate(filename='ospf.cfg')
		diff = iosv.compare_config()
		if len(diff) > 0:
			iosv.commit_config()
		iosv.close()


def ping_loop(dict_data):
	ios_output = []
	driver = get_network_driver('ios')
	iosr = driver(dict_data["host1"], dict_data["user1"], dict_data["pass1"])
	iosr.open()
	ios_output0 = iosr.ping(dict_data["loop2"])
	ios_output1 = iosr.ping(dict_data["loop3"])
	ios_output2 = iosr.ping(dict_data["loop4"])
	ios_output.append(ios_output0)
	ios_output.append(ios_output1)
	ios_output.append(ios_output2)
	return ios_output
	#print(ios_output)
	#print(ios_output1)
	#print(ios_output2)	



def main(dat):
	output = PrettyTable(["Router", "Interface", "IP_address"])
	dict_data = dat.to_dict(flat=True)
	print(dict_data)
	for i in range (1,5):
		ip_test = dict_data["host" + str(i)]
		user = dict_data["user" + str(i)]
		passw = dict_data["pass" + str(i)]
		if validateIP.main(ip_test):
			driv = get_network_driver('ios')
			iosv = driv(ip_test, user, passw)
			iosv.open()
			out  = iosv.get_interfaces_ip()
			iosv.close()
			ip = []
			ipadd = myprint(out, ip)
			intf = interf(out)
			l = len(ipadd) 
			for j in range(0, l):
				if ipadd[j] == ip_test:
					print("configured")
					output.add_row(["R" + str(i), intf[j], ipadd[j]])
	print(output)
	#ospf_main(dict_data)
	data = ping_loop(dict_data)
	return data
	
			
