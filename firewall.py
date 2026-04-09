from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def _handle_PacketIn(event):
    packet = event.parsed

    
    ip_packet = packet.find('ipv4')

    if ip_packet:
        src_ip = ip_packet.srcip

        
        if str(src_ip) == "10.0.0.1":
            log.info("Blocked packet from IP %s", src_ip)

            # Install drop rule in switch
            msg = of.ofp_flow_mod()
            msg.match.dl_type = 0x0800   # IPv4
            msg.match.nw_src = ip_packet.srcip
            msg.actions = []  # no action = drop

            event.connection.send(msg)
            return

    # Allow other traffic
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
