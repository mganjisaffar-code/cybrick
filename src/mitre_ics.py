"""
Cybrick MITRE ATT&CK for ICS
Version 0.1
"""


class MITRETechnique:

    def __init__(self, technique_id, name, tactic):
        self.technique_id = technique_id
        self.name = name
        self.tactic = tactic


class MITREICSDatabase:

    def __init__(self):
        self.techniques = []

    def add(self, technique):
        self.techniques.append(technique)

    def count(self):
        return len(self.techniques)

    def load_default(self):
        self.add(
            MITRETechnique(
                "T0804",
                "Block Command Message",
                "Impair Process Control"
            )
        )

        self.add(
            MITRETechnique(
                "T0855",
                "Unauthorized Command Message",
                "Execution"
            )
        )
