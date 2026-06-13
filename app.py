import os
import webview
from pynput  import keyboard
from teclado import teclado
from criador_pastas import Obj_criador_de_pasta


        


if __name__ == '__main__':

    Obj_criador_de_pasta.configuracao()

    escutarr = teclado()
    
    ouvinte = keyboard.Listener(escutarr.tecla_ler)

    ouvinte.start()
    
    


    ouvinte.join()
    


    