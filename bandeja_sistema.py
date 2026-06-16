import os 
from PIL import Image
import pystray

class bandeja:
    def __init__(self, encerrar):

        self.encerrar = encerrar
        self.icon = None


    def criar_icon(self):
        caminho = "icon.png"

        if os.path.exists(caminho):
            imagem = Image.open(caminho)
        else:
            imagem = Image.new('RGB', (64,64), color= 'blue')

        menu_bandeja = pystray.Menu(
            pystray.MenuItem('empansor de texto ', lambda: None, enabled=False),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem('SAIR', self.encerrar)
        )

        self.icon = pystray.Icon("TextExpander", imagem, "Text Expander Tool", menu_bandeja)
        self.icon.run()

    def parar_icone(self):
        if self.icon:
            self.icon.stop()
            os._exit(0)

