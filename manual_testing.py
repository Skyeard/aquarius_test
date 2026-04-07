from network_equipment.router_device import Router
from network_equipment.switch_device import Switch


if __name__ == '__main__':
    router_1 = Router(name='Router1', ip_address='192.168.4.1', routing_table={'192.168.4.101': '192.168.4.1'})
    router_2 = Router(name='Router2', ip_address='192.168.3.1', routing_table={'192.168.3.98': '192.168.3.1'})
    switch_1 = Switch(name="Switch_1", ip_address='192.168.4.101', vlan=3)
    switch_2 = Switch(name="Switch_2", ip_address='192.168.3.98', vlan=15)
    print(router_1.get_info(), end='\n\n')
    print(switch_1.get_info(), end='\n\n')

    router_1.power_on()
    switch_1.power_on()
    router_2.power_on()
    switch_2.power_on()
    print(switch_1.get_info(), end='\n\n')
    print(switch_1.get_info(), end='\n\n')
    switch_2.power_off()
    print(switch_2.get_info(), end='\n\n')
    switch_2.delete_vlan(15)
    print(switch_2.get_info(), end='\n\n')
    switch_2.create_vlan(7)
    print(switch_2.get_info(), end='\n\n')
    router_1.add_route(destinition="192.168.4.102", gateway="192.168.4.1")
    print(router_1.get_info(), end='\n\n')
    router_2.remove_route(destinition="192.168.3.98")
    print(router_2.get_info(), end='\n\n')