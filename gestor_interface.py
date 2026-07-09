import webview
class gestorinterface:
    def __init__(self, InterfaceAPIGLB):
        self.InterfaceAPI = InterfaceAPIGLB
        self.interface = None
        
          

    def abri (self, icon = None, item = None):
          if self.interface:
                self.interface.show()

    def ocutar (self):
          if self.interface:
                self.interface.hide()
                return False
          


    def abrir_interface(self):
            api_isolada = self.InterfaceAPI

            self.interface = webview.create_window(
            title="Atalhos de Texto",
            url = "interface/index.html",
            width=1300,
            height=900,
            resizable=True,
            hidden=True,
            js_api=api_isolada
            )
            self.interface.events.closing +=self.ocutar
            


