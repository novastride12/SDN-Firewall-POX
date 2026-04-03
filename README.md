# SDN-Based Firewall using POX

## Problem Statement

The aim of this project is to implement a Software Defined Networking (SDN) based firewall that can control communication between hosts. The firewall should block or allow traffic based on defined rules and also maintain logs of blocked packets.

---

## Tools Used

* Mininet
* POX Controller
* Ubuntu Virtual Machine
* Python

---

## Working

In SDN, the control plane is separated from the data plane, and a centralized controller is responsible for making decisions.

In this project, the POX controller listens for incoming packets (PacketIn events). Based on the defined rule, it decides whether to allow or block the packet.

The rule implemented is simple:

* Traffic coming from host h1 is blocked
* Traffic between other hosts is allowed

Whenever a packet is blocked, a message is printed in the controller terminal.

---

## Testing

### Blocked Case

Command:
h1 ping -c 3 h2

Result:
The packets are not delivered and show "Destination Host Unreachable" with 100% packet loss.

---

### Allowed Case

Command:
h2 ping -c 3 h3

Result:
The communication is successful with 0% packet loss.

---

## Screenshots

The following screenshots are included in the repository:

* blocked.png (shows blocked communication)
* allowed.png (shows successful communication)
* logs.png (shows controller logs)

---

## Steps to Run

1. Start the POX controller:
   cd pox
   ./pox.py firewall

2. Start Mininet:
   sudo mn --topo single,3 --controller remote

3. Test the network:
   h1 ping -c 3 h2
   h2 ping -c 3 h3

---

## Output

* Traffic from h1 is blocked
* Traffic between other hosts is allowed
* Logs are displayed in the controller terminal

---

## Conclusion

This project shows how SDN can be used to control network traffic using a centralized controller. A simple firewall was implemented using POX to block and allow communication between hosts.

---

## Future Scope

* Implement IP-based filtering
* Add MAC address filtering
* Store logs in a file
* Extend to more complex firewall rules
