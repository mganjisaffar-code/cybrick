from feature_extractor import FeatureExtractor


def test_extract_packet_length():
    packet = bytes([0x01, 0x02, 0x03])

    result = FeatureExtractor.extract(packet)

    assert result["packet_length"] == 3
    assert result["is_empty"] is False
