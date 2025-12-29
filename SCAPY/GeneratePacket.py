from scapy.layers.inet import *
from scapy.all import *
from scapy.layers.l2 import Ether

packet = Ether(src= "" ,dst = "")/ IP(dst="192.168.1.1") / ICMP()
send(packet)