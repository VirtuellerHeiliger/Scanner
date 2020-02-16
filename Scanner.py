import scapy.all as scapy
import optparse
parser = optparse.OptionParser()
parser.add_option("-i",dest="iprange" ,help="specific ip or range of ip")
(option,args)  = parser.parse_args()




def scan(ip):
	arp_obj = scapy.ARP(pdst = ip)
	broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
	arp_obj_broadcast = broadcast/arp_obj
	ans = scapy.srp(arp_obj_broadcast,timeout = 1, verbose = False)[0]
	print("IP\t\t\tMAC\n-------------------------------")
	for element in ans:
		print(element[1].psrc+"\t\t"+element[1].hwsrc)



ip = option.iprange;
scan(ip)