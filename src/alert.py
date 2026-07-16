"""
Cybrick Alert Model
Version 0.2
"""

from dataclasses import dataclass, asdict
import json


@dataclass
class Alert:

    threat_detected: bool
    severity: str
    protocol: str
    threat: str
    confidence: float
    mitre: str

    def to_dict(self):
        return asdict(self)

    def to_json(self):
        return json.dumps(
            self.to_dict(),
            indent=2
        )
