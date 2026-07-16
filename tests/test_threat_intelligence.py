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


def test_find_ioc():
    ti = ThreatIntelligence()

    ioc = IOC(
        indicator="10.10.10.10",
        indicator_type="ip",
        description="Known malicious host"
    )

    ti.add_ioc(ioc)

    result = ti.find_by_indicator("10.10.10.10")

    assert result is not None
    assert result.indicator == "10.10.10.10"
    assert result.indicator_type == "ip"
 def test_map_ioc_to_mitre():
    ti = ThreatIntelligence()

    ioc = IOC(
        indicator="192.168.10.50",
        indicator_type="ip",
        description="ICS suspicious host"
    )

    ti.add_ioc(ioc)

    technique = "T0804 - Block Command Message"

    result = ti.map_ioc_to_mitre(
        "192.168.10.50",
        technique
    )

    assert result is True

    found = ti.find_by_indicator("192.168.10.50")

    assert found.mitre_technique == technique
