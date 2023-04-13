import pytest

from Lola.services.bocuse.mappers import BocuseCardapioMapper
from Lola.services.bocuse.mappers import BocuseEquipamentosMapper
from Lola.services.bocuse.mappers import BocuseInformacoesMapper
from Lola.services.bocuse.mappers import BocuseIngredientesMapper
from Lola.services.bocuse.mappers import BocuseMenuMapper
from Lola.services.bocuse.mappers import BocusePreparosMapper


@pytest.mark.usefixtures("menu")
def test_BocuseMenuMapper(menu):
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
    assert expected == BocuseMenuMapper.to_dto(menu)


@pytest.mark.usefixtures("cardapio_salgado")
def test_BocuseCardapioMapper(cardapio_salgado):
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
    assert expected == BocuseCardapioMapper.to_dto(cardapio_salgado)


@pytest.mark.usefixtures("receita")
def test_BocuseIngredientesMapper(receita):
    expected = (
        "\n\nbolo"
        "\n    farinha de trigo: 400 gm"
        "\n    açucar: 2 xicara"
        "\n    bicarbonato de sódio: 4 sopa"
        "\n    fermento químico: 3 sobremesa\n    sal: 2 cha"
        "\n    baunilha: 1 cafe"
        "\n\ncobertura"
        "\n    creme de leite: 100 ml"
        "\n    chocolate : 50 gm"
    )
    assert expected == BocuseIngredientesMapper.to_text(receita)


@pytest.mark.usefixtures("receita")
def test_BocuseEquipamentosMapper(receita):
    expected = "\n\nequipamentos" "\n    forno" "\n    fogão" "\n    micro-ondas"
    assert expected == BocuseEquipamentosMapper.to_text(receita)


@pytest.mark.usefixtures("receita")
def test_BocusePreparosMapper(receita):
    expected = (
        "\n\nmistura"
        "\n    misture os secos"
        "\n    misture os liquidos"
        "\n    misture os scos e os liquidos"
        "\n\nassar"
        "\n    leve ao forno a 180 graus por 1h"
    )
    assert expected == BocusePreparosMapper.to_text(receita)


@pytest.mark.usefixtures("receita")
def test_BocuseInformacoesMapper(receita):
    expected = (
        "\n\ninformações"
        "\n    redimento: 562"
        "\n    porcao: 100"
        "\n    unidades: 5,62"
    )
    assert expected == BocuseInformacoesMapper.to_text(receita)
