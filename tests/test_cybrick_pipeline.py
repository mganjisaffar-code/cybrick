from modbus_parser import ModbusParser
from feature_extractor import FeatureExtractor
from ai_detector import AIThreatDetector


def test_cybrick_detection_pipeline():

    packet = bytes([
        0x00, 0x01,
        0x00, 0x00,
        0x00, 0x06,
        0x01,
        0x08
    ])

    parsed = ModbusParser.parse(packet)

    features = FeatureExtractor.extract(packet)

    detector = AIThreatDetector()

    result = detector.analyze(features)

    assert parsed.function_code == 8
    assert features["function_code"] == 8
    assert result.threat_detected is True
    assert result.severity == "high"
    assert result.protocol == "Modbus TCP"
    assert result.mitre == "T0804"
