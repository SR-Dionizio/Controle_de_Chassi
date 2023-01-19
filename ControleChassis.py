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

