from datetime import datetime

import os
import json
import re
import pyperclip

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
        self.VARIAVEIS_PADRAO["ctrl"] = pyperclip.paste()

        telefone = self.VARIAVEIS_PADRAO.get("telefone") or self.VARIAVEIS_PADRAO.get("contato", "")
        self.VARIAVEIS_PADRAO["telefone"] = telefone
        self.VARIAVEIS_PADRAO.setdefault("contato", telefone)
        return self.VARIAVEIS_PADRAO.copy()

    def salvar_variavel(self, nome, valor):
        nome = nome.strip().casefold()
        if not re.fullmatch(r"[a-z_][a-z0-9_]*", nome):
            return False

        reservadas = {"data", "hora", "ctrl", "telefone", "contato", "nome", "email"}
        if nome in reservadas:
            return False

        caminho_user = self.gestGestor_de_arquivos.caminhouser()
        try:
            if os.path.exists(caminho_user):
                with open(caminho_user, "r", encoding="utf-8") as arquivo:
                    dados = json.load(arquivo)
            else:
                dados = {}

            if not isinstance(dados, dict) or nome in {chave.casefold() for chave in dados}:
                return False

            dados[nome] = valor
            with open(caminho_user, "w", encoding="utf-8") as arquivo:
                json.dump(dados, arquivo, ensure_ascii=False, indent=4)
            return True
        except (OSError, json.JSONDecodeError) as erro:
            print(f"[Variaveis] Erro ao salvar variável: {erro}")
            return False

    def editar_variavel(self, nome_antigo, nome_novo, valor):
        nome_antigo = nome_antigo.strip().casefold()
        nome_novo = nome_novo.strip().casefold()
        if not re.fullmatch(r"[a-z_][a-z0-9_]*", nome_novo):
            return False

        reservadas = {"data", "hora", "ctrl", "telefone", "contato", "nome", "email"}
        if nome_antigo in reservadas or nome_novo in reservadas:
            return False

        caminho_user = self.gestGestor_de_arquivos.caminhouser()
        try:
            with open(caminho_user, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
            if not isinstance(dados, dict):
                return False

            chave_antiga = next(
                (chave for chave in dados if chave.casefold() == nome_antigo), None
            )
            if chave_antiga is None:
                return False

            if nome_novo in {
                chave.casefold() for chave in dados if chave != chave_antiga
            }:
                return False

            del dados[chave_antiga]
            dados[nome_novo] = valor
            with open(caminho_user, "w", encoding="utf-8") as arquivo:
                json.dump(dados, arquivo, ensure_ascii=False, indent=4)
            return True
        except (OSError, json.JSONDecodeError) as erro:
            print(f"[Variaveis] Erro ao editar variável: {erro}")
            return False

    def formatar_txt(self, gatilho):
        variaveis = self.obter_variaveis()

        def substituir(match):
            nome = match.group(1).casefold()
            valor = variaveis.get(nome)
            return str(valor) if valor is not None else match.group(0)

        return re.sub(r"\{\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*\}", substituir, gatilho)



