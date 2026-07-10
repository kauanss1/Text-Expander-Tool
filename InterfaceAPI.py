import json

class InterfaceAPI:
    def __init__(self, gestor_de_arquivos_glb):
        self.gestor = gestor_de_arquivos_glb

    def carregarjs(self):
        print("📦 [Python] JavaScript solicitou os atalhos via API .")
        gatilhos = self.gestor.carregar_gatilhos()
        return gatilhos if gatilhos else {}

    def salvargatilho(self, gatilho, texto):
        
        return self.gestor.salvargatilho_novo(gatilho, texto)
        
