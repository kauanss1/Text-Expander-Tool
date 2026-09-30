import json
import os


class Gestor_de_arquivos:
    def __init__(self, criador_pastasglb):
        self.criador_pastas = criador_pastasglb
        print(f"Tentando usar o caminho: {self.criador_pastas.caminhogatilhos()}")

    def carregar_gatilhos(self):
        try:
            with open(self.criador_pastas.caminhogatilhos(), "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                return dados
        except Exception as e:
            print(f"Erro ao carregar gatilhos: {e}")
            return {}

    def extrair_atalhos_plano(self, no_arvore=None):
        """ Achata a árvore em um dicionário simples {gatilho: texto} para o teclado """
        if no_arvore is None:
            no_arvore = self.carregar_gatilhos()

        mapa = {}
        if not no_arvore:
            return mapa

        for atalho in no_arvore.get("atalhos", []):
            mapa[atalho["gatilho"]] = atalho["conteudo"]

        for subpasta in no_arvore.get("pastas", []):
            mapa.update(self.extrair_atalhos_plano(subpasta))

        return mapa

    def salvargatilho_novo(self, gatilho, texto, pasta_alvo="gatilhos"):
        gatilho = gatilho.strip()
        if not gatilho.startswith("\\"):
            gatilho = "\\" + gatilho
        caminho = self.criador_pastas.caminhogatilhos()
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                dados_arvore = json.load(f)

            def buscar_pasta(no):
                if no.get("nome") == pasta_alvo:
                    return no
                for sub in no.get("pastas", []):
                    resultado = buscar_pasta(sub)
                    if resultado:
                        return resultado
                return None

            pasta_destino = buscar_pasta(dados_arvore)
            if pasta_destino is None:
                pasta_destino = dados_arvore

            atualizado = False
            for atalho in pasta_destino.get("atalhos", []):
                if atalho["gatilho"] == gatilho:
                    atalho["conteudo"] = texto
                    atualizado = True
                    break

            if not atualizado:
                if "atalhos" not in pasta_destino:
                    pasta_destino["atalhos"] = []
                pasta_destino["atalhos"].append({
                    "gatilho": gatilho,
                    "conteudo": texto
                })

            with open(caminho, "w", encoding="utf-8") as f:
                json.dump(dados_arvore, f, ensure_ascii=False, indent=4)

            return True

        except Exception as e:
            print(f"Erro ao salvar o gatilho: {e}")
            return False

    def deletar_gatilho(self, gatilho, pasta_alvo="gatilhos"):
        caminho = self.criador_pastas.caminhogatilhos()
        try:
            with open(caminho, "r", encoding="utf-8") as arquivo:
                dados_arvore = json.load(arquivo)

            def buscar_pasta(no):
                if no.get("nome") == pasta_alvo:
                    return no
                for subpasta in no.get("pastas", []):
                    resultado = buscar_pasta(subpasta)
                    if resultado:
                        return resultado
                return None

            pasta_destino = buscar_pasta(dados_arvore)
            if pasta_destino is None:
                return False

            atalhos = pasta_destino.get("atalhos", [])
            atalhos_restantes = [atalho for atalho in atalhos if atalho.get("gatilho") != gatilho]
            if len(atalhos_restantes) == len(atalhos):
                return False

            pasta_destino["atalhos"] = atalhos_restantes
            with open(caminho, "w", encoding="utf-8") as arquivo:
                json.dump(dados_arvore, arquivo, ensure_ascii=False, indent=4)

            return True
        except Exception as e:
            print(f"Erro ao deletar o gatilho: {e}")
            return False

    def criar_pasta(self, nome, pasta_pai="gatilhos"):
        nome = nome.strip()
        if not nome:
            return False

        caminho = self.criador_pastas.caminhogatilhos()
        try:
            with open(caminho, "r", encoding="utf-8") as arquivo:
                dados_arvore = json.load(arquivo)

            def buscar_pasta(no):
                if no.get("nome") == pasta_pai:
                    return no
                for subpasta in no.get("pastas", []):
                    resultado = buscar_pasta(subpasta)
                    if resultado:
                        return resultado
                return None

            pasta_destino = buscar_pasta(dados_arvore)
            if pasta_destino is None:
                return False

            subpastas = pasta_destino.setdefault("pastas", [])
            if any(subpasta.get("nome", "").casefold() == nome.casefold() for subpasta in subpastas):
                return False

            subpastas.append({
                "nome": nome,
                "atalhos": [],
                "pastas": []
            })

            with open(caminho, "w", encoding="utf-8") as arquivo:
                json.dump(dados_arvore, arquivo, ensure_ascii=False, indent=4)

            return True
        except Exception as e:
            print(f"Erro ao criar a pasta: {e}")
            return False

    def dados_user(self, nome, email, contato):
        dados_user = {
            "nome": nome,
            "email": email,
            "contato": contato
        }
        try:
            with open(self.criador_pastas.caminho_user, "w", encoding="utf-8") as f:
                json.dump(dados_user, f, ensure_ascii=False, indent=4)
                print("Perfil do usuário salvo com sucesso!")
        except Exception as e:
            print(f"Não criou pasta: {e}")

        return 1

    def carregar_dados_user(self):
        try:
            with open(self.criador_pastas.caminhouser(), "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}