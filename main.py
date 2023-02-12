from datas_br import DatasBR
from BuscaChassis import BuscaChassis
from ControleChassis import ControleChassis
<<<<<<< HEAD

cadastra_mes = DatasBR()
formato_mes = cadastra_mes.mes_cadastro()
=======
>>>>>>> testes

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
<<<<<<< HEAD
        mes = formato_mes
        ano = formato_ano
        observacoes = input("Tem alguma observação?\n")
=======
        mes = input(f'Digite o mês que foi feito\n')
        ano = formato_ano
>>>>>>> testes

        controle_2023 = ControleChassis(numero_chassi, nome_cliente, lote, mes, ano)

        controle_2023.cadastra()

    elif escolha == 2:
        pesquisa = input("Digite o número de chassis com 4 digitos: ")

        resultado = BuscaChassis(pesquisa)

        resultado.get_busca()

    elif escolha == 3:
        BuscaChassis(escolha).retornar_todos_dados()