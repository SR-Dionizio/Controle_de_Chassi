from datetime import datetime
class DatasBR:

    def __init__(self):
        self.momento_cadastro = datetime.today()
    def mes_cadastro(self):
        meses_ano = [
            "Jan", "Fev", "Mar", "Abr", 
            "mai", "Jun", "Jul", "Ago", "Set",
            "Out", "Nov", "Dez"
        ]
        mes_cadastro = self.momento_cadastro.month -1
        return meses_ano[mes_cadastro]

    def Ano(self):
        dia_cadastro = self.momento_cadastro.year
        return dia_cadastro
