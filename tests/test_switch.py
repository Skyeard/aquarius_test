from pyats import aetest
from network_equipment.switch_device import Switch
from network_equipment.network_device import NetworkDevice


class TestSwitch(aetest.Testcase):


    @aetest.setup
    def setup(self):
        self.switch = Switch(name="Switch1", ip_address="192.168.4.10", vlan=10)


    @aetest.test
    def test_inheritance(self, steps):
        with steps.start("Проверка наследования"):
            assert isinstance(self.switch, NetworkDevice)


    @aetest.test
    def test_create_vlan(self, steps):
        with steps.start("Создание VLAN"):
            self.switch.delete_vlan(10)  
            self.switch.create_vlan(20)
            assert self.switch.vlan == 20


    @aetest.test
    def test_delete_vlan(self, steps):
        with steps.start("Удаление VLAN"):
            self.switch.delete_vlan(20)
            assert self.switch.vlan == ''


    @aetest.test
    def test_get_info(self, steps):
        with steps.start("Проверка get_info"):
            self.switch.create_vlan(14)
            info = self.switch.get_info()
            assert "Vlan: 14" in info
            assert "Name: Switch1" in info


if __name__ == "__main__":
    aetest.main()
