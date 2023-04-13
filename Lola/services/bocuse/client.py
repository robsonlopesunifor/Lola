import requests

from Lola.configs import settings

BOCUSE_SERVICE: str = f"http://{settings.BOCUSE_HOST}:{settings.BOCUSE_PORT}"


class BocuseClient:
    def getMenu(self):
        return requests.get(f"{BOCUSE_SERVICE}/cardapios/").json()

    def getReceita(self, receita_id):
        return requests.get(f"{BOCUSE_SERVICE}/receita/" + receita_id).json()
