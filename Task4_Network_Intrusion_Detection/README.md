# Task 4: Network Intrusion Detection System

## Project Overview

This project demonstrates the setup and use of a Network Intrusion Detection System (NIDS) using Suricata to monitor network traffic and detect suspicious or potentially malicious activity.
thfyThe project provides pratical experience in network security monitoring, intrusion detection,security rules, alert generation, log analysis, and incident response.

## Objectives

The objective of this task was to configure and demonstrate a Network Intrusion Detection System (NIDS) using Suricata and Wazuh. The system was used to monitor network traffic,identify suspicious activity, generate security alerts,and provide centralized monitoring.


## Intrusion Detection Mechanism

Suricata IDS was used as the primary intrusion detection mechanism. It monitored network traffic on the Ubuntu system using configured detection rules. When network activity matched a rule, Suricata generated a security alert and recorded the event in the 'eve.json' log file located at '/var/log/suricata/eve.json'.

## Tools Used

- Ubuntu Linux
- Suricata IDS
- Wazuh
- Kali Linux
- VirtualBox
- Linux networking tools

## Network Configuration

The Suricata IDS is configured on an Ubuntu viral machine.

- **Operating System:** Ubuntu Linux
- **Network Interface:** enp0s3
- **IP Adress:** Private lab network address

## 1. Suricata Configuration

Suricata was installed and configured on the  Ubuntu machine.

The network interface monitored by Suricata was:

enp0s3

The Suricata configuration was tested using:

bash
sudo suricata -T -c /etc/suricata/suricata.yaml

### Screenshot

![Suricata Configuration Test](Screenshots/suricata_config_test.png)

2. Suricata Rules

Suricata rules were update using:

sudo suricata-update

The update successfully loaded more than 68,000 rules.

### Screenshot

![Suricata Rules Update](Screenshots/suricata_rules_update.PNG)


3. Network Traffic Monitoring

Suricata was configured to monitor network traffic and record events in:

/var/log/suricata/eve.json

The logs contained flow, statistics, and alert events.


 4.Suricata Alert Detection 

 During testing, Suricata successfully detected suspicious network activity and generated an alert.

  The alert was recorded in the 'eve.json' log file.

### Screenshot

![Suricata Alert Detection](Screenshots/suricata_alert_detection.PNG)


5. Wazuh Integration 

Wazuh was used as the security monitoring platform.

The Ubuntu machine was successfully enrolled as 'Vtcsec' agent and successfully connected to the Wazuh manager.

The 'Vtcsec' agent was confirmed as **Active** in the Wazuh dashboard.

### Screenshot

![Wazuh Agent Active](Screenshots/wazuh_vtcsec_active.PNG)


6. Results

The completed setup successfully demonstrated:

. Network traffic monitoring using Suricata
. Suricata rule management and updates.
. Detection and logging of network security events.
. Generation of intrusion detection alerts.
. Integration of Suricata logs with Wazuh.
. Centralized monitoring through the Wazuh dashboard.


7. Conclusion

This task provided pratical experience in deploying and operating a network intrusion detection system. Suricata was used to monitor network traffic and identify suspicious activity, while Wazuh provided centralized security monitoring and visibility.

The exercise improved my understanding of network monitoring, IDS alerts, security event analysis, and the integration of security tools within a cybersecurity environment.

## Author

Ekpenyong Peace Inemesit

## Intership

CodeAlpha CyberSecurity internship
