class ControleChassis:
    def __init__(self, chassis, cliente, lote, mes, ano, observacoes):
        self.chassis = chassis
        self.cliente = cliente
        self.lote = lote
        self.mes = mes
        self.ano = ano
        self.observacoes = observacoes

    def cadastra(self):
        arquivo_lista = open("registro_de_chassis.txt", "a", encoding="utf-8")

        entrada_de_dados = f'Número de chassis = {self.chassis} - Nome do cliente = {self.cliente} - Lote = {self.lote} - Mês = {self.mes} - Ano = {self.ano} - Observações = {self.observacoes}'

        arquivo_lista.write(entrada_de_dados)
        arquivo_lista.write("\n")
        arquivo_lista = open("registro_de_chassis.txt", "r", encoding="utf-8")
        registro_completo = arquivo_lista.readlines()

        cadastro = []

        for linha in registro_completo:
            linha = linha.strip()
            cadastro.append(linha)

        print(f'{self.cliente} cadastrado com sucesso')


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


escolha = 0

while escolha < 4:

    print("***************************************************")
    print("************Controle de chassis 2023***************")
    print("***************************************************")

    print("***************************************************")
    print("**Escolha (1) para cadastrar e (2) para pesquisar**")
    print("***Escolha (3) para mostrar tudo e (4) para sair***")
    print("***************************************************")

    escolha = int(input("Digite: "))

    if escolha == 1:
        numero_chassi = input("Digite o número de chassis\n")
        nome_cliente = input("Digite o nome do cliente\n")
        lote = input(f'Digite o lote do {nome_cliente}\n')
        mes = input("Qual o mês que foi feito?\n")
        ano = input("De qual ano?\n")
        observacoes = input("Tem alguma observação?\n")

        controle_2023 = ControleChassis(numero_chassi, nome_cliente, lote, mes, ano, observacoes)

        controle_2023.cadastra()

    elif escolha == 2:
        pesquisa = input("Digite o número de chassis com 4 digitos: ")

        resultado = BuscaChassis(pesquisa)

        resultado.get_busca(pesquisa)

    elif escolha == 3:
        arquivo_lista = open("registro_de_chassis.txt", "r", encoding="utf-8")
        registro_completo = arquivo_lista.readlines()

        cadastro = []

        for linha in registro_completo:
            linha = linha.strip()
            cadastro.append(linha)
            print(linha)