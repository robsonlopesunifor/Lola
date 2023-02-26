# mostrar a arvore de opçoes de receitas 
import requests


class Menu:
    def __init__(self):
        pass

    def chat(self, tipo_conteudo, mensagem):
        responta = None
        if tipo_conteudo == 'text':
            if self.menu(mensagem): responta = self.menu(mensagem)
            if self.receita(mensagem): responta = self.receita(mensagem)
        return responta

    def menu(self, palavra_chave):
        if palavra_chave.upper() == "MENU":
            responta = requests.get("http://localhost:8000/cardapios/").json()
            text = ''
            for categoria in responta:
                text += '\n\n'+categoria['name']
                for receita in categoria['receitas']:
                    text += '\n\n/'+receita['name']
            return text
        return None

    def receita(self, nome):
        try:
            return requests.get("http://localhost:8000/receita/"+nome).json()
        except:
            return f'An error occurred: {error}'