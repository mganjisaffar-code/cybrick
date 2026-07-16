"""
Cybrick Feature Extraction Module
Extracts basic features from ICS/SCADA traffic.
"""

class FeatureExtractor:

    @staticmethod
    def extract(packet: bytes):

        return {
            "packet_length": len(packet),
            "is_empty": len(packet) == 0,
        }
