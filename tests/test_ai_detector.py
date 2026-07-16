from ai_detector import AIThreatDetector


def test_ai_detector_initialization():
    detector = AIThreatDetector()

    result = detector.analyze({})

    assert result["threat_detected"] is False
    assert result["confidence"] == 0.0
