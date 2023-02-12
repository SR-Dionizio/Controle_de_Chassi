import pyodbc

class ControleChassis:
    def __init__(self, chassis, cliente, lote, mes, ano):

        self.chassis = chassis
        self.cliente = cliente
        self.lote = lote
        self.mes = mes
        self.ano = ano

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
            ,[Mês]
            ,[Ano])
                VALUES
                    ('{self.chassis}', '{self.cliente}', '{self.lote}', '{self.mes}','{self.ano}')"""

        cursor.execute(query)
        cursor.commit()

        print(f'{self.cliente} cadastrado com sucesso')

