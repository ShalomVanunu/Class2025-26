

# This script uses the Scapy library to sniff network traffic
# and specifically look for ARP broadcast responses.
# It requires elevated privileges (e.g., sudo) to run.

from scapy.all import sniff
from scapy.layers.l2 import ARP


def arp_callback(packet):
    """
    This function is a callback for the sniff() function.
    It is executed for every packet that is captured.
    """
    # Check if the packet is an ARP packet
    if packet.haslayer(ARP):
        # Check if the ARP packet is a response (op=2)
        # An ARP request is op=1, and a reply is op=2
        if packet[ARP].op == 2:
            print("--------------------------------------------------")
            print("ARP Response Captured!")
            if packet[ARP].pdst == "172.20.130.12":
                # Extract and print the source IP address (psrc)
                # and the source MAC address (hwsrc) from the ARP layer.
                # The 'psrc' field contains the sender's IP address.
                print(f"IP source of the sender: {packet[ARP].psrc}")
                print(f"IP destnation of the sender: {packet[ARP].pdst}")
                # The 'hwsrc' field contains the sender's hardware (MAC) address.
                print(f"The MAC address of the sender: {packet[ARP].hwsrc}")
                print(f"The MAC address of the target: {packet[ARP].hwdst}")
                print("--------------------------------------------------")

def start_sniffer():
    """
    Starts the packet sniffer with a filter for ARP packets.
    The prn parameter specifies the callback function to be called
    for each packet.
    """
    print("Starting ARP sniffer... Press Ctrl+C to stop.")
    # The filter "arp" ensures we only capture ARP packets,
    # making the process more efficient.
    sniff(filter="arp", prn=arp_callback, store=0)

if __name__ == "__main__":
    start_sniffer()
