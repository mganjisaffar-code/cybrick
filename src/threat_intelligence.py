"""
Cybrick Threat Intelligence Module
Version 0.1
"""


class IOC:

    def __init__(self, indicator, indicator_type, description):
        self.indicator = indicator
        self.indicator_type = indicator_type
        self.description = description


class ThreatIntelligence:

    def __init__(self):
        self.iocs = []

    def add_ioc(self, ioc):
        self.iocs.append(ioc)

    def count(self):
        return len(self.iocs)
