import yaml
import csv


csv_final = []
rout1 = {}
rout2 = {}
rout3 = {}


def config(router, rout):
	with open("router_config.csv", 'r') as csvfile:
		r = csv.DictReader(csvfile)
		intf_name = []
		intf_type = []
		ip_subnet = []
		ospf = []
		ospf_area = []
		pid = []
		for row in r:
			if row['hostname'] == router:
				intf_name.append(row['interfacename'])
				intf_type.append(row['interfacetype'])
				ip_subnet.append(row['ip_subnet'])
				ospf.append(row['ospfnetwork'])
				pid.append(row['processid'])
				ospf_area.append(row['ospfarea'])
			rout['hostname'] = router
		rout['processid'] = pid
		rout['interfacetype'] = intf_type
		rout['interfacename'] = intf_name
		rout['ip_subnet'] = ip_subnet
		rout['ospfnetwork'] = ospf
		rout['ospfarea'] = ospf_area
		csv_final.append(rout)

config('R1', rout1)
config('R2', rout2)
config('R3', rout3)
print(csv_final)


with open('main.yaml', 'w') as file:
	file.write(yaml.dump({'lab8config':csv_final}))
