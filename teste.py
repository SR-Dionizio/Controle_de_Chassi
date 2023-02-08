import pyodbc
dados_conexao = (
            "Driver={SQL Server};"
            "Server=DESKTOP-NARQ1ID;"
            "Database=PTO_TRUCK;"
        )
conexao = pyodbc.connect(dados_conexao)

print('deu bom')

cursor = conexao.cursor()

query = """INSERT INTO [dbo].[Registro de Chassis]
            ([Número de Chassis]
            ,[Nome do cliente]
            ,[Lote]
            ,[Mês])
                VALUES
                    ('{self.chassis}', '{self.cliente}', '{self.lote}', '{self.mes}')"""

cursor.execute(query)