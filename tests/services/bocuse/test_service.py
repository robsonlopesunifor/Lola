from unittest.mock import patch

import pytest

from Lola.services.bocuse.service import BocuseService


class TestBocuseService:
    @pytest.mark.usefixtures("menu")
    @patch("Lola.services.bocuse.client.BocuseClient.getMenu")
    def test_menu(self, get_menu, menu):
        get_menu.return_value = menu
        expected = [
            {
                "id": "1lEx-eFWpAhzA2HokOMQIkcVza8Dg6ERq",
                "name": "salgado",
            },
            {
                "id": "1XE_4rSji7k9-Xe9Fsy2Xkg9rp26iJ8vC",
                "name": "doces",
            },
            {
                "id": "1P_qzVBsmCiWH3iM3T3XhG5yh_d4xQSXq",
                "name": "bebidas",
            },
        ]
        assert expected == BocuseService().menu()
        get_menu.assert_called()

    @pytest.mark.usefixtures("menu")
    @patch("Lola.services.bocuse.client.BocuseClient.getMenu")
    def test_cardapio(self, get_menu, menu):
        get_menu.return_value = menu
        expected = [
            {
                "id": "1CgUth3LFXfM6g7ra5ObRJ2ylr1w_mPejx004WN9j75o",
                "name": "macarrão pappardelle",
            },
            {
                "id": "19TYBsa9Vc6xACUVHz0sNse1AZyK5xsEUtB0R2dBd4BQ",
                "name": "pizza de calabresa",
            },
        ]
        assert expected == BocuseService().cardapio("salgado")
        get_menu.assert_called()

    @pytest.mark.usefixtures("receita")
    @patch("Lola.services.bocuse.client.BocuseClient.getReceita")
    @patch("Lola.services.bocuse.mappers.BocuseIngredientesMapper.to_text")
    def test_ingredientes(self, get_menu, to_text, receita):
        get_menu.return_value = receita
        BocuseService().ingredientes("1bPHL0LwEQMVSe5CPYX39E2rCpbRpSjo-XJMykK7my80")
        get_menu.assert_called()
        to_text.assert_called()

    @pytest.mark.usefixtures("receita")
    @patch("Lola.services.bocuse.client.BocuseClient.getReceita")
    @patch("Lola.services.bocuse.mappers.BocuseEquipamentosMapper.to_text")
    def test_equipamentos(self, get_menu, to_text, receita):
        get_menu.return_value = receita
        BocuseService().equipamentos("1bPHL0LwEQMVSe5CPYX39E2rCpbRpSjo-XJMykK7my80")
        get_menu.assert_called()
        to_text.assert_called()

    @pytest.mark.usefixtures("receita")
    @patch("Lola.services.bocuse.client.BocuseClient.getReceita")
    @patch("Lola.services.bocuse.mappers.BocusePreparosMapper.to_text")
    def test_preparos(self, get_menu, to_text, receita):
        get_menu.return_value = receita
        BocuseService().preparos("1bPHL0LwEQMVSe5CPYX39E2rCpbRpSjo-XJMykK7my80")
        get_menu.assert_called()
        to_text.assert_called()

    @pytest.mark.usefixtures("receita")
    @patch("Lola.services.bocuse.client.BocuseClient.getReceita")
    @patch("Lola.services.bocuse.mappers.BocuseInformacoesMapper.to_text")
    def test_informacoes(self, get_menu, to_text, receita):
        get_menu.return_value = receita
        BocuseService().informacoes("1bPHL0LwEQMVSe5CPYX39E2rCpbRpSjo-XJMykK7my80")
        get_menu.assert_called()
        to_text.assert_called()
