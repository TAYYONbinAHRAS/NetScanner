import scapy.all as scapy                                    
import optparse                                         

def get_user_inputs():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--ipaddress",dest="ip_address",help="Enter IP Address")   
    (user_input,arguments) = parse_object.parse_args()
    if not user_input.ip_address:
        print("Enter IP Address !")
    return user_input

def net_scanner(ip):
    arp_request_packet = scapy.ARP(pdst=ip)                             
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")   
    combined_packed = broadcast_packet/arp_request_packet        
        
    (answered_list,unanswered_list) = scapy.srp(combined_packed,timeout=1)                         
    answered_list.summary()

while True:
    user_ip_address = get_user_inputs()
    net_scanner(user_ip_address.ip_address)
    break


