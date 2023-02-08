class BuscaChassis:
    def __init__(self, busca):
        self.busca = busca

    def get_busca(self, busca):
        arquivo_lista = open("registro_de_chassis.txt", "r", encoding="utf-8")
        registro_completo = arquivo_lista.readlines()

        cadastro = []
        pesquisa_digitada = busca
        for linha in registro_completo:
            cadastro.append(linha)

            elemento_encontrado = None

            if pesquisa_digitada in linha:
                elemento_encontrado = linha
                print(elemento_encontrado)
                break
        if not elemento_encontrado:
            print("Cadastro não encontrado")