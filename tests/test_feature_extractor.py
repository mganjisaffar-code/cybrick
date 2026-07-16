from feature_extractor import FeatureExtractor


def test_extract_modbus_features():
    packet = bytes([
        0x00, 0x01,
        0x00, 0x00,
        0x00, 0x06,
        0x01,
        0x03
    ])

    result = FeatureExtractor.extract(packet)

    assert result["packet_length"] == 8
    assert result["transaction_id"] == 1
    assert result["unit_id"] == 1
    assert result["function_code"] == 3
