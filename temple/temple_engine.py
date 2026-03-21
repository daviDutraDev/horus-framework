class TempleEngine():

    def __init__(self, target):
        self.target = target

    def run_engine(self):
        print("[HORUS] Awakening...\n")

        # 1 Subdomain Scanner
        from eye.subdomain_eye import SubdomainScanner

        scanner = SubdomainScanner(self.target)
        subdomains = scanner.run_subdomain()

        #  HTTP Probe
        from eye.http_probe_eye import HttpProbe

        probe = HttpProbe(subdomains, self.target)
        subdomains_live = probe.run_probe()

        # port scanner
        print("[ANUBIS] Scanning ports...\n")

        from eye.port_eye import PortScanner

        port = PortScanner(subdomains_live, self.target)
        ports_open = port.run_ports()

        print("\n[TEMPLE] Scan complete.")
