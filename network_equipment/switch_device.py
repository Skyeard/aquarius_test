from .network_device import NetworkDevice
from dataclasses import dataclass, field


@dataclass
class Switch(NetworkDevice):
    vlan: int = field(init=True)


    def __post_init__(self):
        self.__validate_vlan(vlan_id=self.vlan)


    @staticmethod
    def __validate_vlan(vlan_id: int):
        if type(vlan_id) not in (int,) or vlan_id <= 0:
            raise ValueError(f'Некорректно указан vlan: {vlan_id}\nОжидается формат целого числа, больше нуля')
    

    def get_info(self):
        device_info = super().get_info()
        switch_info = f"""{device_info}\nVlan: {self.vlan if self.vlan else ''}"""
        return switch_info
    

    def create_vlan(self, vlan_id: int):
        if not self.vlan:
            self.__validate_vlan(vlan_id=vlan_id)
            self.vlan = vlan_id
        

    def delete_vlan(self, vlan_id: int):
        if self.vlan == vlan_id:
            self.vlan = ''
