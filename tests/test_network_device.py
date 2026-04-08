from pyats import aetest
from network_equipment.network_device import NetworkDevice


class TestNetworkDevice(aetest.Testcase):


    @aetest.setup
    def setup(self):
        self.device = NetworkDevice(name="TestDevice", ip_address="192.168.1.1")


    @aetest.test
    def test_creation(self, steps):
        with steps.start("Проверка создания"):
            assert isinstance(self.device, NetworkDevice)
            assert self.device.name == "TestDevice"
            assert self.device.ip_address == "192.168.1.1"


    @aetest.test
    def test_power_on(self, steps):
        with steps.start("Включение"):
            self.device.power_on()
            assert "Active" in self.device.get_info()


    @aetest.test
    def test_power_off(self, steps):
        with steps.start("Выключение"):
            self.device.power_off()
            assert "Inactive" in self.device.get_info()


    @aetest.test
    def test_get_info(self, steps):
        with steps.start("Проверка get_info"):
            info = self.device.get_info()
            assert "Name: TestDevice" in info
            assert "IP: " in info
            assert "Status: " in info


if __name__ == "__main__":
    aetest.main()
