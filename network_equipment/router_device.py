from .network_device import NetworkDevice
from dataclasses import dataclass
from typing import Dict


@dataclass
class Router(NetworkDevice):
    routing_table: Dict[str, str] 


    def __post_init__(self):
        self.__validate_routing_table()


    def __validate_routing_table(self):
        for destinition, gateway in self.routing_table.items():
            self._validate_ipv4(destinition)
            self._validate_ipv4(gateway)


    def add_route(self, destinition, gateway):
        self._validate_ipv4(destinition)
        self._validate_ipv4(gateway)

        if not self.routing_table.get(destinition, False):
            self.routing_table[destinition] = gateway


    def remove_route(self, destinition):
        if self.routing_table.get(destinition, False):
            del self.routing_table[destinition]
    
    def get_info(self):
        device_info = super().get_info()
        router_info = f"""{device_info}\nRouting Table: {self.routing_table}"""
        return router_info
            


if __name__ == "__main__":
    obj = Router(name='Router1', ip_address='192.168.4.20', routing_table={'192.168.4.101':'192.168.4.1'})
    print(obj.get_info())
    obj.add_route(destinition='192.168.4.102', gateway='192.168.4.1')
    print(obj.get_info())
    obj.remove_route(destinition='192.168.4.101')
    obj.remove_route(destinition='192.168.4.101')
    print(obj.get_info())