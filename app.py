import os
import webview
from pynput  import keyboard
from teclado import escutar


        


if __name__ == '__main__':
    print("debug")
    
    escutarr = escutar()
    
    ouvinte = keyboard.Listener(escutarr.tecla_ler)

    ouvinte.start()
    
    


    ouvinte.join()
    


    