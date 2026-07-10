import os
import json

class criador_pastas:
    def __init__(self):
        pasta_user = os.path.expanduser("~")
        self.pasta_sistema= os.path.join(pasta_user, "Text-Expander-Tool")

        self.caminho_gatilhos = os.path.join(self.pasta_sistema, "gatilhos.Json")
        self.caminho_user= os.path.join(self.pasta_sistema,"dados_user.Json" )


    def configuracao(self):
        if not os.path.exists(self.pasta_sistema):
            print("bem vindo🚀🚀🚀🚀 \nprecisamos de algumas informacoes")
            os.makedirs(self.pasta_sistema)


        if not os.path.exists(self.caminho_user):
            print("\n" + "="*40)
            print("📋 CONFIGURAÇÃO DE PERFIL OBRIGATÓRIA")
            print("="*40)

            nome =""

            while not nome.strip():
                nome = input("digite seu nome:")

            
            Email =""

            while not Email.strip():
                Email = input("digite seu Email:")

            
            contato =""

            while not contato.strip():
                contato = input("digite seu contato:")


            print("="*40 + "\n")

            dados_user ={
                "nome": nome.strip(),
                "email": Email.strip(),
                "contato": contato.strip()

            }
            
            try:
                with open(self.caminho_user, "w", encoding="utf-8") as f:
                    json.dump(dados_user, f , ensure_ascii=False , indent=4)
                    print(" Perfil do usuário salvo com sucesso!")
            except Exception  as e:
                print(f"nao criou pasta {e}")

        if not os.path.exists(self.caminho_gatilhos):
            dados_iniciais = {
                "\\help": "Olá! Sou o suporte técnico. Como posso te ajudar hoje?"
            }

            try:
                with open(self.caminho_gatilhos, "w", encoding="utf-8") as f:
                    json.dump(dados_iniciais, f , ensure_ascii=False, indent=4)
                    print("\\help criado ")

            except Exception as e:
                print(f"falha ao criar gatilho {e}")


    def caminhouser(self):
        return self.caminho_user

    def caminhogatilhos(self):
        return self.caminho_gatilhos
