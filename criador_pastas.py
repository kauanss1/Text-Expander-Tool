import os
import json

class criador_pastas:
    def __init__(self):
        pasta_user = os.path.expanduser("~")
        self.pasta_sistema= os.path.join(pasta_user, "Text-Expander-Tool")

        self.caminho_gatilhos = os.path.join(self.pasta_sistema, "gatilhos.Json")
        self.caminho_user= os.path.join(self.pasta_sistema,"dados_user.Json" )


    def configuracao_inicial(self):
        # Cria a pasta do sistema se não existir
        if not os.path.exists(self.pasta_sistema):
            os.makedirs(self.pasta_sistema)
            
        # Cria o arquivo de atalhos com a pasta padrão "gatilhos"
        if not os.path.exists(self.caminho_gatilhos):
            dados_iniciais = {
                "nome": "gatilhos",
                "atalhos": [
                    {
                        "gatilho": "\\help",
                        "conteudo": "Olá! Sou o suporte técnico. Como posso te ajudar hoje?"
                    }
                ],
                "pastas": []
            }

            try:
                with open(self.caminho_gatilhos, "w", encoding="utf-8") as f:
                    json.dump(dados_iniciais, f, ensure_ascii=False, indent=4)
                print("Pasta raiz 'gatilhos' e atalho \\help criados com sucesso!")

            except Exception as e:
                print(f"Falha ao criar estrutura inicial: {e}")

    def dados_user(self):
        if not os.path.exists(self.caminho_user):

            return 1


    def caminhouser(self):
        return self.caminho_user

    def caminhogatilhos(self):
        return self.caminho_gatilhos
    
