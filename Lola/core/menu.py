import requests

from Lola.configs import settings

MENU_SERVICE: str = f"http://{settings.MENU_HOST}:{settings.MENU_PORT}"


class Menu:
    def __init__(self):
        pass

    def requisicao(self):
        requests.get("https://pokeapi.co/api/v2/pokemon/ditto").json()

    def chat(self, tipo_conteudo, mensagem):
        responta = None
        if tipo_conteudo == "text":
            if self.menu(mensagem):
                responta = self.menu(mensagem)
            if self.receita(mensagem):
                responta = self.receita(mensagem)
        return responta

    def menu(self, palavra_chave):
        if palavra_chave.upper() == "MENU":
            responta = requests.get(f"{MENU_SERVICE}/cardapios/").json()
            text = ""
            for categoria in responta:
                text += "\n\n" + categoria["name"]
                for receita in categoria["receitas"]:
                    text += "\n\n/" + receita["name"]
            return text
        return None

    def receita(self, nome):
        try:
            return requests.get(f"{MENU_SERVICE}/ficha_tecnica/" + nome).json()
        except requests.exceptions.RequestException:
            return "Receita não existe"
