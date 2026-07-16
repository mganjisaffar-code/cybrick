def test_detect_suspicious_modbus_function():
    detector = AIThreatDetector()

    result = detector.analyze({
        "function_code": 8
    })

    assert result["threat_detected"] is True
    assert result["confidence"] == 0.95
