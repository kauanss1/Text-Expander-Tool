from datetime import datetime

import os
import json
import re

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

    def obter_variaveis(self):
        self.carregar_variaveis_do_arquivo()

        agora = datetime.now()
        self.VARIAVEIS_PADRAO["data"] = agora.strftime("%d/%m/%y")
        self.VARIAVEIS_PADRAO["hora"] = agora.strftime("%H:%M")

        telefone = self.VARIAVEIS_PADRAO.get("telefone") or self.VARIAVEIS_PADRAO.get("contato", "")
        self.VARIAVEIS_PADRAO["telefone"] = telefone
        self.VARIAVEIS_PADRAO.setdefault("contato", telefone)
        return self.VARIAVEIS_PADRAO.copy()

    def formatar_txt(self, gatilho):
        variaveis = self.obter_variaveis()

        def substituir(match):
            nome = match.group(1).casefold()
            valor = variaveis.get(nome)
            return str(valor) if valor is not None else match.group(0)

        return re.sub(r"\{\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*\}", substituir, gatilho)



