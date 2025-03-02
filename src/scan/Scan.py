import nmap

class Scan:
    def __init__(self, domain):
        self.domain = domain

    def run_nmap(self, ports="1-1000"):
        nm = nmap.PortScanner()
        nm.scan(self.domain, ports)

        for host in nm.all_hosts():
            print(f"Host: {host} ({nm[host].hostname()})")
            print(f"State: {nm[host].state()}")

            for proto in nm[host].all_protocols():
                print(f"Protocol: {proto}")
                ports = nm[host][proto].keys()

                for port in sorted(ports):
                    print(f"Port: {port}, State: {nm[host][proto][port]['state']}")
