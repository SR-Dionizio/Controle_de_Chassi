from datas_br import DatasBR
from BuscaChassis import BuscaChassis
from ControleChassis import ControleChassis

cadastra_mes = DatasBR()
formato_mes = cadastra_mes.mes_cadastro()

cadastra_ano = DatasBR()
formato_ano = cadastra_ano.Ano()

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
        mes = formato_mes
        ano = formato_ano
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