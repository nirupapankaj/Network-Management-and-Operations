
#! /usr/bin/env python
from netmiko import ConnectHandler
import threading

#function to ssh into router and run config
def router(address):
    ios_r1 = {
        'device_type':'cisco_ios',
        'username':'lab',
        'password':'lab123',
        'ip':address
        }
    net_connect=ConnectHandler(**ios_r1)
    conf1=['int f0/1', 'ip address dhcp', 'no shut']
    out1=net_connect.send_config_set(conf1)

#threads to login and run config simultaneously in all routers
t1 = threading.Thread(target=router, args=('10.1.2.2',))
t2 = threading.Thread(target=router, args=('10.1.2.3',))
t3 = threading.Thread(target=router, args=('10.1.2.4',))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()