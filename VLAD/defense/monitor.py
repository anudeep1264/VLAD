import psutil

class SystemMonitor:

    def get_running_processes(self):
        processes = []
        for proc in psutil.process_iter(['pid', 'name']):
            processes.append(proc.info)
        return processes

    def get_open_ports(self):
        ports = []
        for conn in psutil.net_connections(kind='inet'):
            if conn.laddr:
                ports.append(conn.laddr.port)
        return list(set(ports))
