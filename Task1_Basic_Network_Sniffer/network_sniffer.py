
from scapy.all import sniff
from scapy.layers.inet import IP,TCP,UDP,ICMP
from scapy.packet import Raw

def packet_callback(packet):

  print ("="*60)

  if packet.haslayer(IP):

     print (f"Source IP    :{packet[IP].src}")
     print (f"Destination IP:{packet[IP].dst}")

     protocol=packet[IP].proto

     if protocol  == 6:
        print ("Protocol :TCP")

     elif protocol == 17:
        print ("Protocol  :UDP")

     elif protocol ==1:
        print ("Protocol :ICMP")

     else:
       print (f"Protocol Number: {protocol}")

     if packet.haslayer(Raw):
        try:
          payload = packet[Raw].load.decode(errors="ignore")
          print ("\nPayload:")
          print (payload)
        except:
            print ("Unable to decode payload")

print ("Starting Network Sniffer...")
print ("Press CTRL + C to stop.\n")

sniff(prn=packet_callback, store=False)

