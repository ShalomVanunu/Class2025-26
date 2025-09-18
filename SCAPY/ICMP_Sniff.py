
from scapy.all import *
from scapy.layers.inet import IP, TCP,ICMP

def icmp_packet_callback(packet):
    """
    A callback function to process each captured packet.
    """
    # Check if the packet has an IP layer
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)

        # Check if the IP packet contains an ICMP layer
        if ip_layer.haslayer(ICMP):
            print(f"ICMP Packet Detected! 📡")
            print(f"Source IP: {ip_layer.src}")
            print(f"Destination IP: {ip_layer.dst}")
            print("-" * 30)


def start_sniffer():
    """
    Starts the network sniffer to capture ICMP packets.
    """
    print("Starting ICMP packet sniffer... Press Ctrl+C to stop.")

    # Use the sniff function to capture packets
    # filter="icmp" specifies we only want to capture ICMP packets
    # prn=icmp_packet_callback sets the function to be called for each packet
    try:
        sniff(filter="icmp", prn=icmp_packet_callback)
    except KeyboardInterrupt:
        print("\nSniffer stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    start_sniffer()