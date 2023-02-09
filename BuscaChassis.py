<<<<<<< HEAD
=======
import pyodbc

>>>>>>> testes
class BuscaChassis:
    def __init__(self, busca):
        self.busca = busca

<<<<<<< HEAD
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
=======
    def get_busca(self):
        dados_conexao = (
            "Driver={SQL Server};"
            "Server=DESKTOP-NARQ1ID;"
            "Database=PTO_TRUCK;"
        )

        conexao = pyodbc.connect(dados_conexao)

        cursor = conexao.cursor()

        query = f"""select * from [Registro de Chassis] where [Número de Chassis] = '{self.busca}'"""

        cursor.execute(query)
        resultado = cursor.fetchall()
        for item in resultado:
            print(item)

    def retornar_todos_dados(self):
        dados_conexao = (
            "Driver={SQL Server};"
            "Server=DESKTOP-NARQ1ID;"
            "Database=PTO_TRUCK;"
        )

        conexao = pyodbc.connect(dados_conexao)

        cursor = conexao.cursor()

        query = f"""select * from [Registro de Chassis]"""

        cursor.execute(query)
        resultado = cursor.fetchall()
        for item in resultado:
            print(item)
>>>>>>> testes
