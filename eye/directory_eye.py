import requests


class Directorfuzzer():

    def __init__(self, hosts, target):
        self.hosts = hosts
        self.target = target
        self.wordlist = []
        self.found = []

    def load_wordlist(self):
        with open('scrolls/subdomain_directory.txt', 'r') as file:
            for line in file:
                self.wordlist.append(line.strip())

    def build_url(self, host, directory):

        host, port = host.split(":")

        if port == "443":
            return f"https://{host}/{directory}"
        else:
            return f"http://{host}:{port}/{directory}"

    def fuzz(self):
        print(f"\n[THOTH] Explorando: {self.target}")
        for host in self.hosts:

           

            for directory in self.wordlist:

                url = self.build_url(host, directory)
                try:
                    response = requests.get(url, timeout=3)

                    if response.status_code in [200, 301, 302, 403]:
                        self.found.append(
                            f"{url:<50} {response.status_code}")

                except requests.RequestException:
                    continue

    def show_results(self):
        if not self.found:
            print("Nenhum Diretorio Encontrado")
            return

        print("\n[THOTH] Resultados:\n")

        for item in self.found:
            print(item)

    def save_results(self):
        escolha = input("Salvar resultados em arquivo? (s/n): ")
        escolha = escolha.lower()

        if escolha == "s":
            with open("artifacts/" + self.target + "_directory.txt", "w") as file:
                for directory in self.found:
                    file.write(directory + "\n")

            print("Arquivo baixado no diretorio artifacts/" +
                  self.target + "_directory.txt")

        else:
            print("Subdominios nao foram baixados")

    def run_directory(self):
        self.load_wordlist()
        self.fuzz()
        self.show_results()
        self.save_results()
        return self.found
