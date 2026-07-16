from alert import Alert


def test_alert_json_conversion():

    alert = Alert(
        threat_detected=True,
        severity="high",
        protocol="Modbus TCP",
        threat="Suspicious Function Code",
        confidence=0.95,
        mitre="T0804"
    )

    data = alert.to_dict()

    assert data["severity"] == "high"
    assert data["protocol"] == "Modbus TCP"
    assert data["mitre"] == "T0804"


def test_alert_json_output():

    alert = Alert(
        threat_detected=True,
        severity="high",
        protocol="Modbus TCP",
        threat="Suspicious Function Code",
        confidence=0.95,
        mitre="T0804"
    )

    result = alert.to_json()

    assert "Modbus TCP" in result
    assert "T0804" in result
