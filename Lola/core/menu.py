import requests

from Lola.configs import settings

BOCUSE_SERVICE: str = f"http://{settings.BOCUSE_HOST}:{settings.BOCUSE_PORT}"


class Menu:
    def __init__(self):
        pass

    def chat(self, tipo_conteudo, mensagem):
        responta = None
        if tipo_conteudo == "text":
            if not responta and self.menu(mensagem):
                responta = self.menu(mensagem)
            if not responta and self.receita(mensagem):
                responta = self.receita(mensagem)
        return responta

    def menu(self, palavra_chave):
        if palavra_chave.upper() == "MENU":
            responta = requests.get(f"{BOCUSE_SERVICE}/cardapios/").json()
            text = ""
            for categoria in responta:
                text += "\n\n" + categoria["name"]
                for receita in categoria["receitas"]:
                    text += "\n\n/" + (receita["name"])
            return text
        return None

    def receita(self, nome):
        try:
            return requests.get(f"{BOCUSE_SERVICE}/receita/" + nome).json()
        except requests.exceptions.RequestException:
            return None
