from datetime import datetime

import os
import json

class variaveis_manege:
    def __init__(self, Gestor_de_arquivos_glb):

        self.gestGestor_de_arquivos = Gestor_de_arquivos_glb
        self.VARIAVEIS_PADRAO = {}
        self.carregar_variaveis_do_arquivo()
    
   
    def carregar_variaveis_do_arquivo(self):
        caminho_user = self.gestGestor_de_arquivos.caminhouser()
        
        self.VARIAVEIS_PADRAO = {
            "data": "",
            "hora": ""
        }

        try:

            if os.path.exists(caminho_user):
                with open (caminho_user, "r", encoding="utf-8") as f:
                    dados = json.load(f)
                    dados_limpos = {}
                    for chave, valor in dados.items():
                        dados_limpos[chave] = str(valor).replace("\x08", "").strip()
                    self.VARIAVEIS_PADRAO.update(dados_limpos)
                
        except Exception as e:
            print(f"[Variaveis] Erro ao atualizar do arquivo: {e}")


    def formatar_txt(self, gatilho):
        
        self.carregar_variaveis_do_arquivo()
        
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
    


