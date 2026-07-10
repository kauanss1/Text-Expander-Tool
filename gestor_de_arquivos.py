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
    


    def salvargatilho_novo(self, gatilho, texto):
            print(f"📥 [Python] Tentando salvar: {gatilho} -> {texto}")
            try:
            
                gatilhos_atuais = self.carregar_gatilhos()
            
           
                gatilho_formatado = gatilho if gatilho.startswith("\\") else f"\\{gatilho}"
            
           
                gatilhos_atuais[gatilho_formatado] = texto
            
            
                caminho_arquivo = self.criador_pastas.caminhogatilhos()
            
           
                import json
                with open(caminho_arquivo, "w", encoding="utf-8") as f:
                    json.dump(gatilhos_atuais, f, ensure_ascii=False, indent=4)
                
                    
                    return True 
            
            except Exception as e:
                
                return False
      