#Program to run tcpdump and extract mac-address from the results


from scapy.all import *
import ipaddress


def main():
    pkt = rdpcap('test.pcap')
    loop = int(len(pkt))
    list1 = []
    list2 = []
    list3 = []


    #Parsing pcap file and getting IPv6 address from the packets
    for i in range(0, loop):
        try:
            if pkt[i][ICMPv6EchoRequest]:
                list1.append(pkt[i][IPv6].src)
        except IndexError:
            al = 'no ipv6'
    final = list(set(list1))
    for item in final:
        n = ipaddress.IPv6Address(item)
        list3.append(n.exploded)


    #Function to extract the mac address from the IPv6 address
    def mac(lis_ele):
        list4 = []
        list5 = []
        part = lis_ele.split(':')
        for parts in part[-4:]:
            list5.append(parts)
        list4.append(list5[0])
        list4.append(list5[1][:2] + list5[2][2:])
        list4.append(list5[3])
        #Inverting the 7th bit
        a = list4[0]
        ig = int(a, 16)
        print(ig)
        str(ig)
        print(ig)
        lis = []
        for f in range(0, len(bin(ig))):
            lis.append(bin(ig)[f])
        if int(bin(ig)[8]) == 1:
            lis[8] = '0'
        else:
            lis[8] = '1'
        fin = ''.join(str(v) for v in lis)
        fin1 = (hex(int(fin, 2)))
        list4[0] = fin1[2] + fin1[3] + fin1[4] + fin1[5]
        mac_a = '.'.join(list4)
        list2.append(mac_a)


    #Function call
    for elements in list3:
        mac(elements)
    print(list2)


if __name__ == "__main__":
    main()