from defense.monitor import SystemMonitor
from defense.rules import SUSPICIOUS_PROCESSES, SUSPICIOUS_PORTS

class Defender:

    def __init__(self, speaker):
        self.monitor = SystemMonitor()
        self.speaker = speaker

    def scan(self):
        alerts = []

        # Process scan
        for proc in self.monitor.get_running_processes():
            name = (proc["name"] or "").lower()
            for bad in SUSPICIOUS_PROCESSES:
                if bad in name:
                    alerts.append(f"Suspicious process detected: {name}")

        # Port scan
        ports = self.monitor.get_open_ports()
        for port in ports:
            if port in SUSPICIOUS_PORTS:
                alerts.append(f"Suspicious open port detected: {port}")

        return alerts
