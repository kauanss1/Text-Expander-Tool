from datetime import datetime

class variaveis_manege:
    def __init__(self):
    
        self.VARIAVEIS_PADRAO = {
            "nome": "Kauan Santos Silva",
            "email": "kauan.silva@kinross.com",
            "contato": "+55 (38) 99999-9999",
            "data":"",
            "hora": ""
        }
    
   


    def formatar_txt(self, gatilho):
        txt_formatado = gatilho
        agora = datetime.now()
        self.VARIAVEIS_PADRAO["data"]= agora.strftime("%d/%m/%y")
        self.VARIAVEIS_PADRAO["hora"]= agora.strftime("%H:%M")

        for variaveis, valor_real in self.VARIAVEIS_PADRAO.items():
            busca = f"{{{variaveis}}}"

            if busca in txt_formatado:
                print(" buscando variaveis no texto")
                txt_formatado = txt_formatado.replace(busca, valor_real)

        return txt_formatado


