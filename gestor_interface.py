import webview

class gestorinterface:
    def __init__(self):
          self.interface= None

    def abri (self, icon = None, item = None):
          if self.interface:
                self.interface.show()

    def ocutar (self):
          if self.interface:
                self.interface.hide()
                return False

    def abrir_interface(self):
            self.interface = webview.create_window(
            title="Atalhos de Texto",
            url = "interface/index.html",
            width=700,
            height=500,
            resizable=True,
            hidden=True
            )
            self.interface.events.closing +=self.ocutar
            


