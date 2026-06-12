from pynput  import keyboard
import time
import pyperclip
from variaveis import variaveis_manege



GATILHOS = {
    "\\help": "Olá! Sou o suporte técnico. Como posso te ajudar hoje?",
    "\\ma": """Prezado(a),
    Seu pedido foi enviado para aprovação do(a) 
 
    🔗 Acesse o Kinross Vault por aqui:
    https://launcher.myapps.microsoft.com/api/signin/c41d7696-8371-41c3-98bf-58e45fef2d77?tenantId=296c0af8-f0e6-43a0-ac22-169ba3ad1a69
 
    Ressaltamos que há um prazo de replicação de até 1 hora para que a alteração seja efetivada, após a aprovação.
    {silva}
    {nome}
    {cargo}
    {hora}
    {data}
    Information Technology Department""",
    "\\re": "Obrigado pelo contato! O seu chamado foi registrado com sucesso."
}



class escutar:
    def __init__(self):
        self.temp = ""
        self.digitar = keyboard.Controller()
        self.gerencia_variaveis = variaveis_manege()

    def tecla_ler( self, tecla):
        try:

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

                if self.temp in GATILHOS:
                    texto_sub= GATILHOS[self.temp]

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


        pyperclip.copy(txt_formatado)

        self.digitar.press(keyboard.Key.ctrl)

        self.digitar.press('v')
        self.digitar.release('v')

        self.digitar.release(keyboard.Key.ctrl)
        time.sleep(0.02)
        pyperclip.copy("")
        print("area de transferencia limpa ")


                    


