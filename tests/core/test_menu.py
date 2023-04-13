import requests
import vcr

from pactman import Consumer
from pactman import Pact
from pactman import Provider

from Lola.configs import settings
from Lola.core.menu import Menu

PACT_MOCK_HOST = settings.BOCUSE_HOST
PACT_MOCK_PORT = settings.BOCUSE_PORT
PACT_DIR = str(settings.PACT_DIR)
BOCUSE_SERVICE: str = f"http://{settings.BOCUSE_HOST}:{settings.BOCUSE_PORT}"


pact: Pact = Consumer("Consumer-Lola").has_pact_with(
    Provider("Provider-Menu"),
    host_name=PACT_MOCK_HOST,
    port=PACT_MOCK_PORT,
    pact_dir=PACT_DIR,
)


class TestMenu:
    def test_requisicao(self):
        expected = [
            {
                "id": "1lEx-eFWpAhzA2HokOMQIkcVza8Dg6ERq",
                "name": "salgado",
                "receitas": [
                    {
                        "id": "19TYBsa9Vc6xACUVHz0sNse1AZyK5xsEUtB0R2dBd4BQ",
                        "name": "teste_pizza",
                    }
                ],
            },
            {
                "id": "1XE_4rSji7k9-Xe9Fsy2Xkg9rp26iJ8vC",
                "name": "doces",
                "receitas": [
                    {
                        "id": "1bPHL0LwEQMVSe5CPYX39E2rCpbRpSjo-XJMykK7my80",
                        "name": "teste_bolo",
                    }
                ],
            },
            {
                "id": "1P_qzVBsmCiWH3iM3T3XhG5yh_d4xQSXq",
                "name": "bebidas",
                "receitas": [
                    {
                        "id": "1v2l5IL_WZbmkX3aVuIWcvhRlbpm149haVyj73OkhQ3A",
                        "name": "teste_cafe",
                    }
                ],
            },
        ]

        (
            pact.given("UserA exists and is not an administrator")
            .upon_receiving("a request for UserA")
            .with_request("GET", "/cardapios/")
            .will_respond_with(200, body=expected)
        )

        with pact:
            result = requests.get(f"{BOCUSE_SERVICE}/cardapios/").json()

        assert result == expected

    def _test_chat(self):
        assert type(Menu().chat("text", "menu")) == str
        assert type(Menu().receita("pizza")) == dict
        assert Menu().chat("text", "carro") is None
        assert Menu().chat("imagem", "menu") is None

    def _test_menu(self):
        assert (
            Menu().menu("menu")
            == "\n\nsalgado\n\n/pao\n\n/pasta\n\n/pizza\n\ndoces\n\n"
            "/pudim\n\n/brigadeiro\n\n/cookies\n\nbebidas\n\n/cafe"
        )
        assert Menu().menu("alguma coisa") is None

    @vcr.use_cassette("tests/fixtures/vcr_cassettes/receita.yml")
    def _test_receita(self):
        receita = Menu().receita("teste_bolo")
        assert "informacoes" in list(receita.keys())
        assert "ingredientes" in list(receita.keys())

    @vcr.use_cassette("tests/fixtures/vcr_cassettes/receita_does_not_exist.yml")
    def _test_receita_does_not_exist(self):
        receita = Menu().receita("does_not_exist")
        assert "informacoes" in list(receita.keys())
        assert "ingredientes" in list(receita.keys())
