from dataclasses import dataclass, field
from ipaddress import IPv4Address


@dataclass
class NetworkDevice:
    name: str
    ip_address: str
    __status: str = field(init=False, default='Inactive')


    def __post_init__(self):
        self._validate_ipv4(self.ip_address)
        self._validate_name()

    @staticmethod
    def _validate_ipv4(ip):
        try:
            IPv4Address(ip)
            if not isinstance(ip, str):
                raise ValueError    
        except ValueError:
            raise ValueError(f"Некорректный формат: '{ip}'\n Ожидается IPv4 формат.")


    def _validate_name(self):
        if not isinstance(self.name, str) or not self.name:
            raise ValueError(f'Имя должно иметь формат строки, не пустой')


    def power_on(self):
        self.__status = 'Active'

    
    def power_off(self):
        self.__status = 'Inactive'

    def get_info(self):
        return f"""Name: {self.name}
IP: {self.ip_address}
Status: {self.__status}"""

if __name__ == '__main__':
    obj = NetworkDevice(name='Device', ip_address='192.168.4.2')
    print(obj.get_info())
    obj.power_on()
    print(obj.get_info())
