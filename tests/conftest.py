import pytest


@pytest.fixture
def cardapio_salgado():
    return {
        "id": "1lEx-eFWpAhzA2HokOMQIkcVza8Dg6ERq",
        "name": "salgado",
        "receitas": [
            {
                "id": "1CgUth3LFXfM6g7ra5ObRJ2ylr1w_mPejx004WN9j75o",
                "name": "macarrão pappardelle",
            },
            {
                "id": "19TYBsa9Vc6xACUVHz0sNse1AZyK5xsEUtB0R2dBd4BQ",
                "name": "pizza de calabresa",
            },
        ],
    }


@pytest.fixture
def cardapio_doce():
    return {
        "id": "1XE_4rSji7k9-Xe9Fsy2Xkg9rp26iJ8vC",
        "name": "doces",
        "receitas": [
            {
                "id": "1bPHL0LwEQMVSe5CPYX39E2rCpbRpSjo-XJMykK7my80",
                "name": "teste_bolo",
            },
        ],
    }


@pytest.fixture
def cardapio_bebida():
    return {
        "id": "1P_qzVBsmCiWH3iM3T3XhG5yh_d4xQSXq",
        "name": "bebidas",
        "receitas": [],
    }


@pytest.fixture
def menu(cardapio_salgado, cardapio_doce, cardapio_bebida):
    return [cardapio_salgado, cardapio_doce, cardapio_bebida]


@pytest.fixture
def receita():
    return {
        "equipamentos": [
            {"nome": "forno", "necessario": True},
            {"nome": "fogão", "necessario": True},
            {"nome": "micro-ondas", "necessario": True},
            {"nome": "termo circulado", "necessario": False},
            {"nome": "geladeira", "necessario": False},
            {"nome": "frise", "necessario": False},
            {"nome": "liquidificador", "necessario": False},
            {"nome": "mixer", "necessario": False},
            {"nome": "processador", "necessario": False},
            {"nome": "batedeira", "necessario": False},
        ],
        "ingredientes": [
            {
                "etapa": "bolo",
                "ingredientes": [
                    {
                        "nome": "farinha de trigo",
                        "quantidade": "400",
                        "medida": "gm",
                    },
                    {
                        "nome": "açucar",
                        "quantidade": "2",
                        "medida": "xicara",
                    },
                    {
                        "nome": "bicarbonato de sódio",
                        "quantidade": "4",
                        "medida": "sopa",
                    },
                    {
                        "nome": "fermento químico",
                        "quantidade": "3",
                        "medida": "sobremesa",
                    },
                    {
                        "nome": "sal",
                        "quantidade": "2",
                        "medida": "cha",
                    },
                    {
                        "nome": "baunilha",
                        "quantidade": "1",
                        "medida": "cafe",
                    },
                ],
            },
            {
                "etapa": "cobertura",
                "ingredientes": [
                    {
                        "nome": "creme de leite",
                        "quantidade": "100",
                        "medida": "ml",
                    },
                    {
                        "nome": "chocolate ",
                        "quantidade": "50",
                        "medida": "gm",
                    },
                ],
            },
        ],
        "informacoes": {
            "rendimento": "562",
            "porcao": "100",
            "unidades": "5,62",
            "custo": "0",
        },
        "preparos": [
            {
                "etapa": "mistura",
                "passos": [
                    {"descricao": "misture os secos", "tipo": ""},
                    {"descricao": "misture os liquidos", "tipo": ""},
                    {"descricao": "misture os scos e os liquidos", "tipo": "obs"},
                ],
            },
            {
                "etapa": "assar",
                "passos": [
                    {"descricao": "leve ao forno a 180 graus por 1h", "tipo": ""},
                ],
            },
        ],
    }
