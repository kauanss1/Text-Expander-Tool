import json

class InterfaceAPI:
    def __init__(self, gestor_de_arquivos_glb):
        self.gestor = gestor_de_arquivos_glb

    def carregarjs(self):
        print("📦 [Python] JavaScript solicitou os atalhos via API .")
        gatilhos = self.gestor.carregar_gatilhos()
        return gatilhos if gatilhos else {}

    def salvargatilho(self, gatilho, texto):
        print(f"📥 [Python] Tentando salvar: {gatilho} -> {texto}")
        try:
            
            gatilhos_atuais = self.gestor.carregar_gatilhos()
            
           
            gatilho_formatado = gatilho if gatilho.startswith("\\") else f"\\{gatilho}"
            
           
            gatilhos_atuais[gatilho_formatado] = texto
            
            
            caminho_arquivo = self.gestor.criador_pastas.caminhogatilhos()
            
           
            import json
            with open(caminho_arquivo, "w", encoding="utf-8") as f:
                json.dump(gatilhos_atuais, f, ensure_ascii=False, indent=4)
                
            print("✅ [Python] Gatilho salvo com sucesso no JSON!")
            return True 
            
        except Exception as e:
            print(f"❌ [Python] Erro ao salvar gatilho: {e}")
            return False