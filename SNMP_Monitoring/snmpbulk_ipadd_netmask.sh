#! /bin/bash
echo --Displaying the IP and Subnet--

echo -- R1 --
echo IPADDR:$(snmpwalk -v 1 -c public 198.51.100.1 .1.3.6.1.2.1.4.20.1.1 | awk '{print $4}')
echo SUBNET:$(snmpwalk -v 1 -c public 198.51.100.1 .1.3.6.1.2.1.4.20.1.3 | awk '{print $4}')

echo -- R2 --
echo IPADDR:$(snmpwalk -v 2c -c public 198.51.100.3 .1.3.6.1.2.1.4.20.1.1 | awk '{print $4}')
echo SUBNET:$(snmpwalk -v 2c -c public 198.51.100.3 .1.3.6.1.2.1.4.20.1.3 | awk '{print $4}')

echo -- R3 --
echo IPADDR:$(snmpwalk -v3 -l authpriv -u kelly -a SHA -A "netmanager" -x DES -X "netmanager" 198.51.100.4 .1.3.6.1.2.1.4.20.1.1 | awk '{print $4}')
echo SUBNET:$(snmpwalk -v3 -l authpriv -u kelly -a SHA -A "netmanager" -x DES -X "netmanager" 198.51.100.4 .1.3.6.1.2.1.4.20.1.3 | awk '{print $4}') 

 
