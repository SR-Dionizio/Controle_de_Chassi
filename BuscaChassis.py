import pyodbc

class BuscaChassis:
    def __init__(self, busca):
        self.busca = busca

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

