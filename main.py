import pyodbc

class ControleChassis:
    def __init__(self, chassis, cliente, lote, mes):
        self.chassis = chassis
        self.cliente = cliente
        self.lote = lote
        self.mes = mes

    def cadastra(self):
        dados_conexao = (
            "Driver={SQL Server};"
            "Server=DESKTOP-NARQ1ID;"
            "Database=PTO_TRUCK;"
        )

        conexao = pyodbc.connect(dados_conexao)

        cursor = conexao.cursor()

        query = f"""INSERT INTO [dbo].[Registro de Chassis]
            ([Número de Chassis]
            ,[Nome do cliente]
            ,[Lote]
            ,[Mês])
                VALUES
                    ('{self.chassis}', '{self.cliente}', '{self.lote}', '{self.mes}')"""

        cursor.execute(query)
        cursor.commit()

        print('Chassis cadastrado')



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

        controle_2023 = ControleChassis(numero_chassi, nome_cliente, lote, mes)

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