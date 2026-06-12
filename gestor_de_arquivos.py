import json
import os       


class Gestor_de_arquivos:
    def __init__(self):
        

        pasta_user = os.path.expanduser("~")
        self.pasta_sistema = os.path.join(pasta_user,"Text-Expander-Tool")
        self.caminho_json = os.path.join(self.pasta_sistema, "gatilhos.Json")
        print(f" Tentando usar o caminho: {self.pasta_sistema}")

        if not os.path.exists(self.pasta_sistema):
            os.makedirs(self.pasta_sistema)
            print("pasta criada ")


    def carregar_gatilhos(self):

        if not os.path.exists(self.caminho_json):
            print("arquivos nao encontrado criando nova pasta  ")

            dados_iniciais = {
                "\\help": "Olá! Sou o suporte técnico. Como posso te ajudar hoje?"
            }
            
        
            try:
                with open (self.caminho_json, "w", encoding="utf-8") as arquivo:
                    json.dump(dados_iniciais, arquivo , ensure_ascii= False, indent=4)
                    
                    print(f" Sucesso! {len(dados_iniciais)} gatilhos carregados do JSON.")
                return dados_iniciais

            except Exception as e:
                
                print(f"erro ao ler arquivos: {e}")

                return{}
        try: 
            with open(self.caminho_json, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                return dados
       
        except Exception as e:
            print(f"dsadw {e}")
      
      