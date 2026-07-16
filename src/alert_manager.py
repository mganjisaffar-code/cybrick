"""
Cybrick Alert Manager
Version 0.1
"""


class AlertManager:

    def __init__(self):
        self.alerts = []

    def add_alert(self, alert):
        self.alerts.append(alert)

    def count(self):
        return len(self.alerts)

    def get_all(self):
        return self.alerts
    def clear(self):
    self.alerts.clear()
