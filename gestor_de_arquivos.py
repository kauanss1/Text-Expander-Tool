import json
import os       


class Gestor_de_arquivos:
    def __init__(self, criador_pastasglb):
        
        self.criador_pastas = criador_pastasglb




        print(f" Tentando usar o caminho: {self.criador_pastas.caminhogatilhos()}")



    def carregar_gatilhos(self):

        try: 
            with open(self.criador_pastas.caminhogatilhos(), "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                return dados
       
        except Exception as e:
            print(f"dsadw {e}")

            return{}
      
      