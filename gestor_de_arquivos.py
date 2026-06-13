import json
import os       
from criador_pastas import Obj_criador_de_pasta

class Gestor_de_arquivos:
    def __init__(self):
        
        


        self.caminho_user = Obj_criador_de_pasta.caminhouser()
        self.caminho_json = Obj_criador_de_pasta.caminhogatilhos()

        print(f" Tentando usar o caminho: {self.caminho_json}")



    def carregar_gatilhos(self):

        try: 
            with open(self.caminho_json, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                return dados
       
        except Exception as e:
            print(f"dsadw {e}")

            return{}
      
      