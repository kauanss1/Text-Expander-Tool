import os
from time import time
import webview
from pynput  import keyboard
from teclado import teclado
from criador_pastas import criador_pastas
from bandeja_sistema import bandeja
from threading import Thread
from gestor_interface import gestorinterface
from gestor_de_arquivos import Gestor_de_arquivos
from variaveis import variaveis_manege
from InterfaceAPI import InterfaceAPI



def fechar(icon, item):
    print("fechando")
    if app_bandeja:
        app_bandeja.parar_icone()
    os._exit(0)
        

def start_teclado():
    print(" teclado ativado.")
    escutarr = teclado(Gestor_de_arquivos_glb, gerencia_variaveisglb)
    ouvinte = keyboard.Listener(on_press=escutarr.tecla_ler)  
    ouvinte.start()



def start_bandeja():
    global app_bandeja
    app_bandeja = bandeja(encerrar=fechar, abri=controlador_inteface.abri)
    app_bandeja.criar_icon()




if __name__ == '__main__':

    # criacao de todos os obijetos 

    criador_pastasglb = criador_pastas()
    Gestor_de_arquivos_glb = Gestor_de_arquivos(criador_pastasglb)
    gerencia_variaveisglb = variaveis_manege(criador_pastasglb)
    InterfaceAPI_GLB = InterfaceAPI(Gestor_de_arquivos_glb)
    controlador_inteface = gestorinterface(InterfaceAPI_GLB)
    # ===========================================================
    
    
    app_bandeja = None
    
    # gera interface em segundo plano 
    controlador_inteface.abrir_interface()


    # verifica as pastas e cria se nao existir      
    criador_pastasglb.configuracao_inicial()
            
     
    thread_teclado = Thread(target=start_teclado, daemon=True)
    thread_da_bandeja = Thread(target=start_bandeja, daemon=True)

  
    thread_teclado.start()
    thread_da_bandeja.start()


    # webview.start(gui='edgechromium')

    
    def inicializar_sistema():
        i = criador_pastasglb.dados_user()
        if i == 1:
            InterfaceAPI_GLB.chamar_js("confg_abri")

    webview.start(inicializar_sistema,gui='edgechromium')

 



        