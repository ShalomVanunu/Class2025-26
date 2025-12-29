from scapy.all import sniff
from scapy.layers.inet import IP, TCP,ICMP
from scapy.layers.dns import DNS

def dns_query_callback(packet):
    """
    Callback function to process each captured packet.
    """
    # Check if the packet has an IP layer and a DNS layer
    print(packet.show())
    if packet.haslayer(DNS) and packet.haslayer(IP):
        # We are only interested in DNS queries (requests), not responses
        # A DNS query has the QR (Query/Response) flag set to 0
        if packet[DNS].qr == 0:
            # Extract the DNS question section
            dns_question = packet[DNS].qd

            # Check if there is a DNS question record
            if dns_question:
                # Get the domain name from the question record and decode it
                domain_name = dns_question.qname.decode('utf-8')

                # Print the source IP and the requested domain
                print(f"DNS Query from {packet[IP].src}: {domain_name}")
                print("-" * 30)


def start_dns_sniffer():
    """
    Starts the network sniffer to capture DNS query packets.
    """
    print("Starting DNS query sniffer... Press Ctrl+C to stop. 🔎")

    # Use the sniff function to capture packets
    # filter="udp port 53" captures all UDP packets on port 53, the standard DNS port
    # prn=dns_query_callback sets the function to be called for each packet
    try:
        sniff(filter="udp port 53", prn=dns_query_callback, store=0)
    except KeyboardInterrupt:
        print("\nSniffer stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    start_dns_sniffer()