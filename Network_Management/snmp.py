from easysnmp import Session
import re
import json
from subprocess import check_output
import time
import matplotlib.pyplot as plt


def main():
    time_list = []
    cpu_list = []
    snmp_dict = {}
    snmp_stat = {}
	
#function to obtain ipv4 addresses with interface
    def ipv4(ip):
        ch_dict = {}
        sess = Session(hostname=ip, community='public', version=2)
        sys = sess.walk(oids=u'.1.3.6.1.2.1.4.34.1.3.1')
        for item in sys:
            ipv4 = '{oid}.{oid_index} {snmp_type} = {value}'.format(
                oid=item.oid,
                oid_index=item.oid_index,
                snmp_type=item.snmp_type,
                value=item.value
            )
            add1 = re.split(r'\s', ipv4)
            add2 = add1[0].split('.')
            ch_dict[add1[-1]] = add2[-4] + '.' + add2[-3] + '.' + add2[-2] + '.' + add2[-1]
        return ch_dict

#function to obtain ipv6 addresses
    def ipv6(ip):
        interface = []
        ch_dict1 = {}
        p1 = check_output(["snmpwalk", "-v", "2c", "-c", "public", ip, ".1.3.6.1.2.1.4.34.1.3.2"])
        p2 = p1.split('\n')
        p2.pop()
        for items in p2:
            interface.append(items.split('"')[2].split('=')[1][10])
            ch_dict1[items.split('"')[2].split('=')[1][10]] = items.split('"')[1]
        return ch_dict1, interface

#function to get dictionary of interfaces along with ipv4 and ipv6 addresses
    def ip_main(ip):
        addr = {}
        x = ipv4(ip)
        a, b = ipv6(ip)
        dict_intf = {'1': 'fa0/0', '2': 'fa1/0', '3': 'fa1/1'}
        i = 0
        for i in range(0, len(b)):
            intf_name = dict_intf[b[i]]
            addr[intf_name] = {'v4': x[b[i]] + '/24', 'v6': a[b[i]] + '/64'}
            i += 1
        return addr

#fuction to return interface name and status
    def intstat(ip):
        ip_stat = {}
        list1 = []
        list2 = []
        dict_intf = {'1': 'fa0/0', '2': 'fa1/0', '3': 'fa1/1', '4': 'fa0/1'}
        dict_status = {'1': 'up', '2': 'down'}
        sess = Session(hostname=ip, community='public', version=2)
        sys = sess.walk(oids=u'.1.3.6.1.2.1.2.2.1.8')
        count = 0
        for item in sys:
            int1 = '{oid}.{oid_index} {snmp_type} = {value}'.format(
                oid=item.oid,
                oid_index=item.oid_index,
                snmp_type=item.snmp_type,
                value=item.value
            )
            add3 = re.split(r'\s', int1)
            add4 = add3[0].split('.')
            list1.append(add4[-1])
            list2.append(add3[-1])
            count += 1
        for i in range(0, count):
            int_name = dict_intf[list1[i]]
            int_stat = dict_status[list2[i]]
            ip_stat[int_name] = int_stat
        return ip_stat

#function to find CPU utilization
    def cpu_uti(ip):
        for i in range(0, 25):
            p1 = check_output(["snmpwalk", "-v", "2c", "-c", "public", ip, ".1.3.6.1.4.1.9.2.1.56"])
            list1 = re.split(r'\s', p1)
            cpu_list.append(list1[-2])
            time_list.append(time.strftime('%M'))
            time.sleep(5)
        print(cpu_list)
        print(time_list)
        plt.ylabel("CPU metric")
        plt.xlabel("Time")
        plt.plot(cpu_list, time_list)
        plt.show()
        plt.savefig("cpuutil.png", format='png')

    cpu_uti('10.1.2.1')
    router = ['R1', 'R2', 'R3', 'R4', 'R5']
    router_ip = ['10.1.2.1', '10.1.1.2', '10.1.1.3', '198.51.100.3', '10.1.1.1']
    for i in range(0, len(router)):
        fin = ip_main(router_ip[i])
        snmp_dict[router[i]] = fin
        stat = intstat(router_ip[i])
        snmp_stat[router[i]] = stat
    print(snmp_dict)
    print(snmp_stat)

    with open('obj3.txt', 'w') as file:
        json.dump(snmp_dict, file, indent=4, sort_keys=True)

    with open('obj3.txt', 'a') as file:
        json.dump(snmp_stat, file, indent=4, sort_keys=True)


if __name__ == "__main__":
    main()