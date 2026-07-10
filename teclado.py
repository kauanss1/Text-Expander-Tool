from pynput  import keyboard
import time
import pyperclip
import gc

class teclado:
    def __init__(self, Gestor_de_arquivos_glb, gerencia_variaveisglb):
        self.temp = ""
        self.digitar = keyboard.Controller()
        self.gerencia_variaveis = gerencia_variaveisglb
        self.gestor = Gestor_de_arquivos_glb
        self.gatilhos_sistema = self.gestor.carregar_gatilhos()

    def tecla_ler( self, tecla):
        try:
            total_objetos = len(gc.get_objects())
            print(f"📊 Objetos vivos na RAM: {total_objetos}")
            tecla_char = tecla.char
            print(f"tecla acionada {tecla_char} ")
            if tecla_char is not None:
                if tecla_char == "\\":
                    print("contra barra encontrada ")
                    self.temp = "\\"

                elif self.temp.startswith("\\"):
                    self.temp += tecla_char
        except AttributeError:
            if tecla == keyboard.Key.backspace and len(self.temp)>0:
                self.temp = self.temp[:-1]
            elif tecla == keyboard.Key.space and self.temp.startswith("\\"):

                if self.temp in self.gatilhos_sistema:
                    texto_sub= self.gatilhos_sistema[self.temp]

                    qtd_char = len(self.temp)+1

                    self.apagar_gatilho(qtd_char , texto_sub)


                self.temp = ""
        
    def apagar_gatilho (self, contagem, texto_novo ):

        time.sleep (0.05)

        


        txt_formatado = self.gerencia_variaveis.formatar_txt(texto_novo)
        for _ in range(contagem):
            self.digitar.press(keyboard.Key.backspace)
            self.digitar.release(keyboard.Key.backspace)
            time.sleep(0.01)


        time.sleep(0.02)
        pyperclip.copy(txt_formatado)
        self.digitar.press(keyboard.Key.ctrl)

        self.digitar.press('v')
        self.digitar.release('v')

        self.digitar.release(keyboard.Key.ctrl)
        
        # LEMBRA DE RETIRAR ISSO DEPOIS 
        self.gatilhos_sistema = self.gestor.carregar_gatilhos()
        # LEMBRA DE RETIRAR ISSO DEPOIS 

        time.sleep(0.02)
        pyperclip.copy("")
        print("area de transferencia limpa ")


                    


