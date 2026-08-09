# Task 4: Network Intrusion Detection System

## Project Overview

This project demonstrates the setup and use of a Network Intrusion Detection System (NIDS) using Suricata to monitor network traffic and detect suspicious or potentially malicious activity.

The project provides pratical experience in network security monitoring, intrusion detection,security rules, alert generation, log analysis, and incident response.

## Objectives

The main objective of this project are to:

- Set up a network-based intrusion detection system using suricata.
- Configure and test suricata detection rules.
- Monitor network traffic for suspicious activity.
- Generate and analyze security alerts.
- Examine suricata event logs.
- Integrate security monitoring with Wazuh where applicable.
- Demonstrate appropriate response machanisms for detected threats.
- Document the complete implementation and findings.

## Tools and Technologies

- Ubuntu Linux
- Suricata IDS
- Wazuh
- Kali Linuxs
- Nmap
- VirtualBox
- Network monitoring and log analysis tools

## Network Configuration

The Suricata IDS is configured on an Ubuntu viral machine.

- **Operating System:** Ubuntu Linux
- **Network Interface:** enp0s3
- **IP Adress:** Private lab network address

## Implementation

### 1. Suricata installation and Verification

Suricata was installed on the Ubuntu system and verified to ensure that the service was running correctly.

### 2. Network Interface Configuration

Suricata is configured to monitor the active network interface and inspect network traffic for suspicious activity.

### 3. Detection Rules

Suricata rules are used to identify suspicious network behaviour and generate alerts when matching traffic is detected.

### 4. Network Traffic Monitoring

Controlled network traffic is generated and monitored to verify that suricata can detect and record relevant network events.

### 5. Alert and Log Analysis

Suricata logs are examined to identify detected events, including network flows, protocols, source addresses, destination addresses, and alert information.

### 6. Wazuh Intergration

Where applicable, Suricata security events are forwarded to Wazuh for centeralized monitoring and visualization.

### Testing

Controlled network-security tests are performed to verify the functionality of the intrusion detection system.

Testing may include:

- Network connectivity testing
- Port scanning in a controlled lab environment
- Detection rule testing
- Suricata alert verfication
- Log analysis
- Wazuh event monitoring

  
## Screenshots

Screenshots documenting the implementation and testing process will be added to the 'Screenshots' folder.

## Findings 

The project demonstrates how a network intrusion detection system can monitor network activity and identify potentially suspicious behavior.

The generated alerts and logs provide useful information for security monitoring and incident investigation.

## Response Mechanism

when suspicious activity is detected, the event can be investigated using the available logs and security monitoring tools. Appropriate response actions may include identifying the source of the activity, reviewing affected systems, blocking malicious traffic where appropriate, and documenting the incident.

## Conclusion

This project provided pratical experience in deploying and operating a network intrusion detection system using Suricata. It also demonstrated the importance of network monitoring, detection rules, security alerts, log analysis,and incident response in cybersecurity.

## Author

Ekpenyong Peace Inemesit

## Intership

CodeAlpha Cyber Security internship
