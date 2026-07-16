from threat_intelligence import IOC, ThreatIntelligence


def test_add_ioc():
    ti = ThreatIntelligence()

    ioc = IOC(
        indicator="192.168.1.100",
        indicator_type="ip",
        description="Test IOC"
    )

    ti.add_ioc(ioc)

    assert ti.count() == 1
