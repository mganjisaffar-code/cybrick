"""
Cybrick Threat Intelligence Module
Version 0.1
"""

class IOC:

    def __init__(self, indicator, indicator_type, description):
        self.indicator = indicator
        self.indicator_type = indicator_type
        self.description = description
        self.mitre_technique = None


class ThreatIntelligence:

    def __init__(self):
        self.iocs = []

    def add_ioc(self, ioc):
        self.iocs.append(ioc)

    def count(self):
        return len(self.iocs)
    def map_ioc_to_mitre(self, indicator, technique):
        for ioc in self.iocs:
            if ioc.indicator == indicator:
                ioc.mitre_technique = technique
                return True

        return False
    def find_by_indicator(self, indicator):
        for ioc in self.iocs:
            if ioc.indicator == indicator:
                return ioc
        return None
