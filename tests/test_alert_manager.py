from alert import Alert
from alert_manager import AlertManager


def test_add_alert():

    manager = AlertManager()

    alert = Alert(
        threat_detected=True,
        severity="high",
        protocol="Modbus TCP",
        threat="Suspicious Function Code",
        confidence=0.95,
        mitre="T0804"
    )

    manager.add_alert(alert)

    assert manager.count() == 1


def test_get_all_alerts():

    manager = AlertManager()

    alert = Alert(
        threat_detected=True,
        severity="high",
        protocol="Modbus TCP",
        threat="Suspicious Function Code",
        confidence=0.95,
        mitre="T0804"
    )

    manager.add_alert(alert)

    alerts = manager.get_all()

    assert len(alerts) == 1
    assert alerts[0].severity == "high"
