from pyats.aetest import Testcase, setup, test
from pyats import aetest
from network_equipment.network_device import NetworkDevice


class TestNetworkDevice(Testcase):

    @setup
    def setup(self):
        self.device = NetworkDevice(name="TestDevice", ip_address="192.168.1.1")

    @test
    def test_creation(self, steps):
        with steps.start("Проверка создания"):
            assert self.device.name == "TestDevice"
            assert self.device.ip_address == "192.168.1.1"

    @test
    def test_power_on(self, steps):
        with steps.start("Включение"):
            self.device.power_on()
            assert "Active" in self.device.get_info()

    @test
    def test_power_off(self, steps):
        with steps.start("Выключение"):
            self.device.power_off()
            assert "Inactive" in self.device.get_info()

    @test
    def test_get_info(self, steps):
        with steps.start("Проверка get_info"):
            info = self.device.get_info()
            assert "Name: TestDevice" in info


if __name__ == "__main__":
    aetest.main()
