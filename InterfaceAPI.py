import json

class InterfaceAPI:
    def __init__(self, gestor_de_arquivos_glb):
        self.gestor = gestor_de_arquivos_glb
        self._janela = None

    def registrar_janela(self, janela_webview):
        self._janela = janela_webview

    def chamar_js(self, nome_funcao):
        if self._janela:
            self._janela.evaluate_js(f"{nome_funcao}()")

    def carregarjs(self):
        print("📦 [Python] JavaScript solicitou os atalhos via API .")
        gatilhos = self.gestor.carregar_gatilhos()
        return gatilhos if gatilhos else {}

    def salvargatilho(self, gatilho, texto):
        
        return self.gestor.salvargatilho_novo(gatilho, texto)