from datetime import datetime
class DatasBR:

    def __init__(self):
        self.momento_cadastro = datetime.today()
    def mes_cadastro(self):
        meses_ano = [
            "Janeiro", "Fevereiro", "Março", "Abril", 
            "maio", "Junho", "Julho", "Agosto", "Setembro",
            "Outubro", "Novembro", "Dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month -1
        return meses_ano[mes_cadastro]

    def Ano(self):
        dia_cadastro = self.momento_cadastro.year
        return dia_cadastro
