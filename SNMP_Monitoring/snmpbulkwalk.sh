#! /bin/bash

echo -- SNMP BULK WALK --

echo router:----R1----
echo interface_name:$(snmpwalk -v 1 -c public 198.51.100.1 ifDescr.1 | awk '{print $4}')
echo Description:$(snmpwalk -v 1 -c public 198.51.100.1 ifDescr.3 | awk '{print $4}')
echo Operational_status:$(snmpwalk -v 1 -c public 198.51.100.1 ifOperStatus.1 | awk '{print $4}')
echo Physical_address:$(snmpwalk -v 1 -c public 198.51.100.1 ifPhysAddress.1 | awk '{print $4}')
echo Admin_status:$(snmpwalk -v 1 -c public 198.51.100.1 ifAdminStatus.1 | awk '{print $4}')
echo Incoming_unicast_packets:$(snmpwalk -v 1 -c public 198.51.100.1 ifInUcastPkts.1 | awk '{print $4}')

echo router:----R2----
echo interface_name:$(snmpbulkwalk -v2c -c public 198.51.100.3 ifDescr.1 | awk '{print $4}')
echo Description:$(snmpbulkwalk -v2c -c public 198.51.100.3 ifDescr.3 | awk '{print $4}')
echo Operational_status:$(snmpbulkwalk -v2c -c public 198.51.100.3 ifOperStatus.1 | awk '{print $4}')
echo Physical_address:$(snmpbulkwalk -v2c -c public 198.51.100.3 ifPhysAddress.1 | awk '{print $4}')
echo Admin_status:$(snmpbulkwalk -v2c -c public 198.51.100.3 ifAdminStatus.1 | awk '{print $4}')
echo Incoming_unicast_packets:$(snmpbulkwalk -v2c -c public 198.51.100.3 ifInUcastPkts.1 | awk '{print $4}')

echo router:----R3----
echo interface_name:$(snmpbulkwalk -v3 -l authpriv -u kelly -a SHA -A "netmanager" -x DES -X "netmanager" 198.51.100.4 ifDescr.1 | awk '{print $4}')
echo Description:$(snmpbulkwalk -v3 -l authpriv -u kelly -a SHA -A "netmanager" -x DES -X "netmanager" 198.51.100.4 ifDescr.3 | awk '{print $4}')
echo Operational_status:$(snmpbulkwalk -v3 -l authpriv -u kelly -a SHA -A "netmanager" -x DES -X "netmanager" 198.51.100.4 ifOperStatus.1 | awk '{print $4}')
echo Physical_address:$(snmpbulkwalk -v3 -l authpriv -u kelly -a SHA -A "netmanager" -x DES -X "netmanager" 198.51.100.4 ifPhysAddress.1 | awk '{print $4}')
echo Admin_status:$(snmpbulkwalk -v3 -l authpriv -u kelly -a SHA -A "netmanager" -x DES -X "netmanager" 198.51.100.4 ifAdminStatus.1 | awk '{print $4}')
echo Incoming_unicast_packets:$(snmpbulkwalk -v3 -l authpriv -u kelly -a SHA -A "netmanager" -x DES -X "netmanager" 198.51.100.4 ifInUcastPkts.1 | awk '{print $4}')
