from scapy.all import *

ip = IP(src="10.9.0.105", dst="10.9.0.6")
tcp = TCP(sport=1023, dport=514, flags="S", seq=778933536)

pkt = ip/tcp
ls(pkt)
send(pkt,verbose=0)
