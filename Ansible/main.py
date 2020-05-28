from netmiko import ConnectHandler
import time
from pythonping import ping


def config(router, ip_add):
	rout = {'device_type':'cisco_ios',
		'username':'lab',
		'password':'lab123',
		'ip':ip_add
		}
	routers = ConnectHandler(**rout)
	routers.enable()
	routers.send_config_from_file('/home/netman/'+router+'.txt')


#config('R1', '198.51.100.1')
#config('R2', '198.51.100.4')
#config('R3', '198.51.100.3')


#time.sleep(5)
ping('10.0.0.1', verbose=True)
ping('20.0.0.1', verbose=True)
ping('30.0.0.1', verbose=True)
ping('198.51.101.3', verbose=True)
ping('198.51.102.3', verbose=True)
ping('198.51.101.4', verbose=True)
ping('198.51.102.5', verbose=True)
