def test_detect_suspicious_modbus_function():
    detector = AIThreatDetector()

    result = detector.analyze({
        "function_code": 8
    })

    assert result["threat_detected"] is True
    assert result["confidence"] == 0.95
    def test_threat_alert_format():

    detector = AIThreatDetector()

    result = detector.analyze({
        "function_code": 8
    })

    assert result["threat_detected"] is True
    assert result["severity"] == "high"
    assert result["protocol"] == "Modbus TCP"
    assert result["mitre"] == "T0804"
    assert result["confidence"] == 0.95
