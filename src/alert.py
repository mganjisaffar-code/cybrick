"""
Cybrick Alert Model
Version 0.1
"""

from dataclasses import dataclass


@dataclass
class Alert:

    threat_detected: bool
    severity: str
    protocol: str
    threat: str
    confidence: float
    mitre: str
