import os
import webview
from pynput  import keyboard
from teclado import teclado
from criador_pastas import criador_pastas
from bandeja_sistema import bandeja
from threading import Thread
import asyncio
from gestor_interface import gestorinterface
from gestor_de_arquivos import Gestor_de_arquivos
from variaveis import variaveis_manege



def fechar(icon, item):
    print("fechando")
    if app_bandeja:
        app_bandeja.parar_icone()
    os._exit(0)
        

def start_teclado():
    criador_pastasglb.configuracao()
    print(" teclado ativado.")
    escutarr = teclado(Gestor_de_arquivos_glb, gerencia_variaveisglb)
    ouvinte = keyboard.Listener(on_press=escutarr.tecla_ler)  
    ouvinte.start()



async def rodar_bandeja():
    global app_bandeja
    app_bandeja = bandeja(encerrar=fechar, abri= controlador_inteface.abri)
    await asyncio.get_event_loop().run_in_executor(None, app_bandeja.criar_icon)

if __name__ == '__main__':

    # criacao de todos os obijetos 
    criador_pastasglb = criador_pastas()
    Gestor_de_arquivos_glb = Gestor_de_arquivos(criador_pastasglb)
    gerencia_variaveisglb = variaveis_manege(criador_pastasglb)
    controlador_inteface = gestorinterface()
    # ===========================================================
    
    
    app_bandeja = None



    segundo_plano = Thread(target=start_teclado, daemon=True)
    segundo_plano.start()




    controlador_inteface.abrir_interface()
    
    def iniciar_loop():
        asyncio.run(rodar_bandeja())
    webview.start(iniciar_loop)
    


        