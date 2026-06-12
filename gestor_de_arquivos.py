import json
import os       


class Gestor_de_arquivos:
    def __init__(self):
        self.caminho_json = "gatilhos.Json"


    def carregar_gatilhos(self):

        if not os.path.exists(self.caminho_json):
            print("arquivos nao encontrado ")
            return{}
        
        try:
            with open (self.caminho_json, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                print(f"[Gestor] Sucesso! {len(dados)} gatilhos carregados do JSON.")
            return dados
        

        except Exception as e:
            
            print(f"erro ao ler arquivos: {e}")

            return{}