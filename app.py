import os
import webview
from pynput  import keyboard
from teclado import teclado
from criador_pastas import Obj_criador_de_pasta
from bandeja_sistema import bandeja
from threading import Thread


app_bandeja = None

def fechar(icon, item):
    print("fechando")
    if app_bandeja:
        app_bandeja.parar_icone()
    os._exit
        

def start_teclado():
    Obj_criador_de_pasta.configuracao()
    print(" teclado ativado.")
    escutarr = teclado()
    ouvinte = keyboard.Listener(on_press=escutarr.tecla_ler)  
    ouvinte.start()
        


if __name__ == '__main__':

    segundo_plano = Thread(target=start_teclado, daemon=True)
    segundo_plano.start()


    app_bandeja = bandeja(encerrar=fechar)
    app_bandeja.criar_icon()

        