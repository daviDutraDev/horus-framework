
import requests


class HttpProbe():

    def __init__(self, subdomains, Target):
        self.target = Target
        self.subdomains_found = subdomains
        self.subdomains_live = []

    def probe_hosts(self):

        for hosts in self.subdomains_found:
            hosts.strip()
            https_url = f"https://{hosts}"
            http_url = f"http://{hosts}"
            try:

                response = requests.get(https_url,  headers={
                                        "User-Agent": "HorusScanner"}, timeout=3, verify=False)
                status = response.status_code

                if status in [200, 301, 302, 401, 403, 500]:
                    self.subdomains_live.append(f"{https_url} {status}")

            except requests.RequestException:

                try:
                    response = requests.get(http_url, timeout=3)
                    status = response.status_code

                    if status in [200, 301, 302, 401, 403, 500]:
                        self.subdomains_live.append(f"{http_url} {status}")

                except requests.RequestException:
                    continue

    def show_results(self):

        if not self.subdomains_live:
            print("Nenhum subdomínio Vivo")
            return
        for sub in self.subdomains_live:
            print(sub)

    def save_results(self):

        escolha = input("Salvar resultados em arquivo? (s/n): ")
        escolha = escolha.lower()

        if escolha == "s":
            with open("artifacts/" + self.target + "_live_hosts.txt", "w") as file:
                for sub in self.subdomains_live:
                    file.write(sub + "\n")

            print("Arquivo baixado no diretorio artifacts/" +
                  self.target + "_live_hosts.txt")

        else:
            print("Subdominios nao foram baixados")

    def run_probe(self):
        self.probe_hosts()
        self.show_results()
        self.save_results()
        return self.subdomains_live
