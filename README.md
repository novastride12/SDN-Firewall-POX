# SDN-Based Firewall using POX

## Problem Statement

The aim of this project is to implement a Software Defined Networking (SDN) based firewall that can control communication between hosts. The firewall should block or allow traffic based on defined rules and maintain logs of blocked packets.

---

## Tools Used

* Mininet
* POX Controller
* Ubuntu Virtual Machine
* Python

---

## Working

In SDN, the control plane is separated from the data plane, and a centralized controller makes decisions about traffic.

In this project, the POX controller listens for PacketIn events. It checks the source IP address of incoming packets and applies filtering rules.

* Traffic from IP **10.0.0.1 (h1)** is blocked
* Traffic between other hosts is allowed

Additionally, the controller installs a **drop rule in the switch using OpenFlow**, so repeated packets are blocked directly at the switch without involving the controller.

Blocked packets are logged in the controller terminal.

---

## Testing

### Blocked Case

Command:
h1 ping -c 3 h2

Result:
Packets are not delivered and show "Destination Host Unreachable" with 100% packet loss.

---

### Allowed Case

Command:
h2 ping -c 3 h3

Result:
Communication is successful with 0% packet loss.

---

## Steps to Run

1. Start POX controller:
   cd pox
   ./pox.py firewall

2. Start Mininet:
   sudo mn --topo single,3 --controller remote

3. Test:
   h1 ping -c 3 h2
   h2 ping -c 3 h3

---

## Output

* Traffic from h1 is blocked
* Traffic between other hosts is allowed
* Drop rules are installed in the switch
* Logs are displayed in the controller terminal

---

## Conclusion

This project demonstrates how SDN can be used to control network traffic using a centralized controller. A firewall was implemented using IP-based filtering and OpenFlow rules to efficiently block unwanted traffic.

---

## Future Scope

* MAC-based filtering
* Logging to file
* Advanced firewall rules
