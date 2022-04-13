from scapy.all import *

ip = IP(src="10.9.0.105", dst="10.9.0.6")
tcp = TCP(sport=1023, dport=514, flags="A", seq=778933537, ack=3680096251)

if tcp.flags == "A":
	print("Establishing ACK packet")


pkt = ip/tcp
ls(pkt)
send(pkt, verbose=0)
