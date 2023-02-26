# teste simples 
import pytest
import sys, os
sys.path.insert(0, os.path.abspath('../LolaBot'))
from core.menu import Menu


class TestMenu:

    def test_chat(self):
        assert type(Menu().chat('text','menu')) == str
        assert type(Menu().receita('pizza')) == dict
        assert Menu().chat('text','carro') == None
        assert Menu().chat('imagem','menu') == None

    def test_menu(self):
        assert Menu().menu('menu') == '\n\nsalgado\n\n/pao\n\n/pasta\n\n/pizza\n\ndoces\n\n/pudim\n\n/brigadeiro\n\n/cookies\n\nbebidas\n\n/cafe'
        assert Menu().menu('alguma coisa') == None

    def test_receita(self):
        assert Menu().receita('qualquer coisa') == None
        assert Menu().receita('pizza') == {
            'possao':8,
            'gasto':80.00,
            'custo':10.10,
            'ingredientes':[
                {'nome':'farinha','gramas':'400'},
                {'nome':'aguq','gramas':'300'},
                {'nome':'sal','gramas':'200'}
            ]
        }
