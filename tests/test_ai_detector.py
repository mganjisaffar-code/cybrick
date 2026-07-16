from ai_detector import AIThreatDetector
from threat_intelligence import ThreatIntelligence


def test_ai_detector_initialization():
    detector = AIThreatDetector()

    result = detector.analyze({})

    assert result.threat_detected is False
    assert result.confidence == 0.0


def test_detect_suspicious_modbus_function():
    detector = AIThreatDetector()

    result = detector.analyze({
        "function_code": 8
    })

    assert result.threat_detected is True
    assert result.confidence == 0.95


def test_threat_alert_format():
    detector = AIThreatDetector()

    result = detector.analyze({
        "function_code": 8
    })

    assert result.threat_detected is True
    assert result.severity == "high"
    assert result.protocol == "Modbus TCP"
    assert result.mitre == "T0804"
    assert result.confidence == 0.95


def test_ai_detector_with_threat_intelligence():
    ti = ThreatIntelligence()

    detector = AIThreatDetector(
        threat_intelligence=ti
    )

    result = detector.analyze({
        "function_code": 8
    })

    assert result.threat_detected is True
    assert result.confidence == 0.95
