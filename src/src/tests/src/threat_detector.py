"""
Cybrick Threat Detection Engine

Initial implementation of the AI-assisted threat detection module.
"""


class ThreatDetector:

    def __init__(self):
        self.name = "Cybrick Threat Detector"

    def analyze_packet(self, protocol, port):
        if protocol == "Modbus TCP" and port == 502:
            return {
                "risk": "Low",
                "message": "Valid Modbus traffic detected."
            }

        return {
            "risk": "Unknown",
            "message": "Protocol not recognized."
        }


if __name__ == "__main__":
    detector = ThreatDetector()
    print(detector.analyze_packet("Modbus TCP", 502))
