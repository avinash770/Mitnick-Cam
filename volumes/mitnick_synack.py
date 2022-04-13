from scapy.all import *



ip = IP(src="10.9.0.105", dst="10.9.0.6")

tcp = TCP(sport=9091, dport=514, flags="SA", seq=2390674446)



pkt = ip/tcp

ls(pkt)

send(pkt, verbose=0)
