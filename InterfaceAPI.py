class InterfaceAPI:
    def __init__(self, gestor_de_arquivos_glb):
        self.gestor = gestor_de_arquivos_glb

    def carregarjs(self):
        print("📦 [Python] JavaScript solicitou os atalhos via .")
        gatilhos = self.gestor.carregar_gatilhos()
        return gatilhos if gatilhos else {}
