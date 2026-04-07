from pyats.aetest import Testcase, setup, test
from pyats import aetest
from network_equipment.router_device import Router
from network_equipment.network_device import NetworkDevice


class TestRouter(Testcase):

    @setup
    def setup(self):
        self.router = Router(name="Router1", ip_address="192.168.4.1", routing_table={"192.168.4.100": "192.168.4.1"})

    @test
    def test_inheritance(self, steps):
        with steps.start("Проверка наследования"):
            assert isinstance(self.router, NetworkDevice)

    @test
    def test_add_route(self, steps):
        with steps.start("Добавление маршрута"):
            self.router.add_route("192.168.4.101", "192.168.4.1")
            assert self.router.routing_table["192.168.4.101"] == "192.168.4.1"

    @test
    def test_remove_route(self, steps):
        with steps.start("Удаление маршрута"):
            self.router.remove_route("192.168.1.101")
            assert "192.168.1.100" not in self.router.routing_table

    @test
    def test_get_info(self, steps):
        with steps.start("Проверка get_info"):
            info = self.router.get_info()
            assert "Routing Table" in info
            assert "Name: Router1" in info


if __name__ == "__main__":
    aetest.main()
