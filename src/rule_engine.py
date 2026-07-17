"""
Cybrick Rule Engine
Version 0.2
"""


class RuleEngine:
    """Initial rule engine for ICS/SCADA."""

    def evaluate(self, features):

        if features.get("function_code") == 8:
            return {
                "severity": "high",
                "mitre": "T0804"
            }

        return None
