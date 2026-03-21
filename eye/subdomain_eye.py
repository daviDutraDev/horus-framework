import dns.resolver


class SubdomainScanner():

    def __init__(self, target):
        self.target = target
        self.wordlist = []
        self.subdomains = []
        self.subdomains_found = []

    def load_wordlist(self):
        """ Carregando a WordList"""
        with open('scrolls/subdomain_teste.txt', 'r') as file:
            for line in file:
                self.wordlist.append(line)

    def generate_subdomains(self):
        """Deixando subdominios no formato correto. que seria wordlist + "." + target """
        for subdomain in self.wordlist:
            subdomain = subdomain.strip()
            sub = f"{subdomain}.{self.target}"
            self.subdomains.append(sub)

    def resolve_dns(self):
        """Aqui eu vou verificar se o subdominio tem dns. ou seja se o subdominio tem um ip se tiver ele e valido """
        for subdomain in self.subdomains:

            try:
                dns.resolver.resolve(subdomain, "A")
                self.subdomains_found.append(subdomain)

            except:
                continue

    def show_results(self):
        """Aqui e basicamente para mostrar resultados e se o usuario quiser baixar eles em um arquivo txt """

        if not self.subdomains_found:
            print("Nenhum subdomínio encontrado")
            return
        for sub in self.subdomains_found:
            print(sub)

    def save_results(self):
        escolha = input("Salvar resultados em arquivo? (s/n): ")
        escolha = escolha.lower()

        if escolha == "s":
            with open("artifacts/" + self.target + "_subdomains.txt", "w") as file:
                for sub in self.subdomains_found:
                    file.write(sub + "\n")

            print("Arquivo baixado no diretorio artifacts/" +
                  self.target + "_subdomains.txt")

        else:
            print("Subdominios nao foram baixados")

    def run_subdomain(self):
        self.load_wordlist()
        self.generate_subdomains()
        self.resolve_dns()
        self.show_results()
        self.save_results()
        return self.subdomains_found
