import os
import webview
from pynput  import keyboard
from teclado import teclado
from criador_pastas import Obj_criador_de_pasta
from bandeja_sistema import bandeja
from threading import Thread
import asyncio


app_bandeja = None

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
    app_bandeja = bandeja(encerrar=fechar)
    await asyncio.get_event_loop().run_in_executor(None, app_bandeja.criar_icon)
def abrir_interface():
        interface = webview.create_window(
        title="Atalhos de Texto",
        url = "interface/index.html",
        width=700,
        height=500,
        resizable=True
        )
        webview.start()

if __name__ == '__main__':

    segundo_plano = Thread(target=start_teclado, daemon=True)
    segundo_plano.start()


    # thread_interface = Thread(target=start_interface, daemon=True)
    # thread_interface.start()


    app_bandeja = bandeja(encerrar=fechar,abri= abrir_interface)
    app_bandeja.criar_icon()

    def iniciar_loop():
        asyncio.run(rodar_bandeja())
    webview.start(iniciar_loop)

        