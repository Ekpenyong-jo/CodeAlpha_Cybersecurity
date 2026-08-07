# Task 1:Basic Network Sniffer

## Project Overview

This project demonstrates the development of a Python-based network packet sniffer capable of capturing and analyzing network traffic in real time.
The program monitors packets travelling across the network and extracts useful information such as the source IP address, destination IP, protocol type and packet payload. This project provides pratical experience in understanding how network communication works and how cybersecurity professionals inspect network traffic for troubleshooting and security monitoring.

## Objective

The objective of this project is to build a basic network packet sniffer using python and scapy to capture live network traffic and analyze packet information. The project also aims to improve understanding of network protocols and packet structures used in cybersecurity.

## Tools Used

- Python 3
- Scapy
- kali Linux
- Oracle VirtualBox

## Project Structure

Task1_Basic_Network_Sniffer/
 - README.md
 - network_sniffer.py
 - Screenshots/

## Project Requirements
 
  - Python 3 installed
  - Scapy library installed
  - Administrator/root privileges
  - Active network connection

## How the program works

  The network sniffer captures packets passing through the selected network interface. Every captured packet is inspected and useful information such as:
  - Source IP Address
  - Destination IP Address
  - Protocol
  - Packet Length
  - Payload
is displayed on the terminal.

This enables network administrators and cybersecurity analysts to monitor network commmunication and identify suspicious traffic.

## Features

- Captures live packets
- Displays source IP Address
- Displays destination IP Address
- Identifies protocols
- Displays packet payload
- Supports continuous packet monitoring

## Python Source Code Explanation

The network sniffer was developed using python and the scapy library. Scapy provides powerful packet manipulation capabilities, allowing the program to capture and inspect packets in real time.

The program performs the following functions:

- Captures packets from the network interface.
- Checks whether the packet contains an IP layer.
- Extracts the source IP address.
- Extracts the destination IP address.
- Identifies the protocol used
- Displays packet information on the terminal.
- Continues monitoring until the program is stopped.

This demonstrates the basic principles of network traffic analysis used by cybersecurity professionals.

## How to Run the Program

- Open the terminal.
- Navigate to the project directory.
- Run the following command:

  sudo python3 network_sniffer.py

- Generate network traffic by:
  . Opening websites
  . Running ping google.com
  . Browsing the internet

- Observe the captured packets displayed in the terminal.


## Expected Output

The program displays information similar to the following:

Source IP: 10.116.131.192
Destination IP: 216.58.223.238
Protocol: TCP
Packet Length: 74 bytes

## Results

The developed packet sniffer successfully captured live network packets and displayed important packet information, including source and destination IP addresses,protocol types, and packet details. This demonstrated how network monitoring tools can inspect traffic for troubleshooting and security analysis.

## Challenges Encountered

During the development of this project, a few challenges were encountered:

 - Understanding how packets sniffing works.
 - Running the program with administrator privileges.
 - Installing and configuring the Scapy library.
 - Capturing meaningful network traffic for testing.
 - Interpreting different protocol types.

These challenges were resolved through research,testing, and repeated practice.

## Skills Gained

Through this project, I gained practical experience in:

 - Python programming
 - Network packet analysis
 - Scapy library usage
 - IP addressing
 - Network protocols
 - Linux command-line operations
 - Basic cybersecurity monitoring
 - Github project documentation

## Conclusion

This project provided hands-on experience in developing a basic network packet sniffer using python. It improved my understanding of network communication, packet structures, and traffic analysis. The Knowledge gained from this project forms a strong foundation for more advanced cybersecurity topics such as intrusion detection, threat anaysis, and network forensics.

## Author

Ekpenyong Peace Inemesit

## Internship

CodeAlpha Cyber Security Internship
