import socket


class PortScanner():
    def __init__(self, subdomains_live, Target):
        self.subdomains_live = subdomains_live
        self.target = Target
        self.subdomains_ports = []
        self.ports_open = []

    def parse_subdomains(self):
        for subdominio in self.subdomains_live:

            subdominio = subdominio.strip()

            subdominio = subdominio.split()[0]

            if subdominio.startswith("https://"):
                subdominio = subdominio[8:]
            elif subdominio.startswith("http://"):
                subdominio = subdominio[7:]

            if subdominio not in self.subdomains_ports:
                self.subdomains_ports.append(subdominio)

    def scan_ports(self):
        ports = [80, 443, 8080, 3000, 8000, 22]

        for host in self.subdomains_ports:

            print(f"\n[Anubis] Escaneando templo: {host}")

            open_ports = 0

            for port in ports:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(1)

                    result = s.connect_ex((host, port))

                    if result == 0:
                        print(f"Portal {port} aberto")
                        self.ports_open.append(f"{host}:{port}")
                        open_ports += 1
                    else:
                        print(f"Portal {port} selado")

                    s.close()

                except Exception:
                    continue

            print(f"Portais encontrados: {open_ports}")

    def save_results(self):
        escolha = input("Salvar resultados em arquivo? (s/n): ")
        escolha = escolha.lower()

        if escolha == "s":
            with open("artifacts/" + self.target + "_ports.txt", "w") as file:
                for sub in self.ports_open:
                    file.write(sub + "\n")

            print("Arquivo baixado no diretorio artifacts/" +
                  self.target + "_ports.txt")

        else:
            print("Subdominios nao foram baixados")

    def run_ports(self):
        self.parse_subdomains()
        self.scan_ports()
        self.save_results()
        return self.ports_open
