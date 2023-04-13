import vcr

from Lola.services.bocuse.client import BocuseClient


class TestBocuseClient:
    @vcr.use_cassette("tests/fixtures/vcr_cassettes/cardapio.yml")
    def test_getMenu(self):
        response = BocuseClient().getMenu()
        assert isinstance(response, list)
        assert response[0]["name"] in ["salgado", "doce", "bebida"]

    @vcr.use_cassette("tests/fixtures/vcr_cassettes/receita.yml")
    def test_getReceita(self):
        response = BocuseClient().getReceita(
            "1bPHL0LwEQMVSe5CPYX39E2rCpbRpSjo-XJMykK7my80"
        )
        assert isinstance(response, dict)
        assert isinstance(response["ingredientes"], list)

    @vcr.use_cassette("tests/fixtures/vcr_cassettes/receita_does_not_exist.yml")
    def test_receita_not_found(self):
        response = BocuseClient().getReceita("error")
        assert response == {"detail": "FichaTecnica Not found"}
