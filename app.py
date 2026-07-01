import os
import webview
from pynput  import keyboard
from teclado import teclado
from criador_pastas import Obj_criador_de_pasta
from bandeja_sistema import bandeja
from threading import Thread
import asyncio
from gestor_interface import gestorinterface

app_bandeja = None
controlador_inteface = gestorinterface()
def fechar(icon, item):
    print("fechando")
    if app_bandeja:
        app_bandeja.parar_icone()
    os._exit(0)
        

def start_teclado():
    Obj_criador_de_pasta.configuracao()
    print(" teclado ativado.")
    escutarr = teclado()
    ouvinte = keyboard.Listener(on_press=escutarr.tecla_ler)  
    ouvinte.start()



async def rodar_bandeja():
    global app_bandeja
    app_bandeja = bandeja(encerrar=fechar, abri= controlador_inteface.abri)
    await asyncio.get_event_loop().run_in_executor(None, app_bandeja.criar_icon)

if __name__ == '__main__':

    segundo_plano = Thread(target=start_teclado, daemon=True)
    segundo_plano.start()




    controlador_inteface.abrir_interface()
    
    def iniciar_loop():
        asyncio.run(rodar_bandeja())
    webview.start(iniciar_loop)
    


        