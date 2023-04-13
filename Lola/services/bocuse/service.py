from Lola.services.bocuse.client import BocuseClient
from Lola.services.bocuse.mappers import BocuseCardapioMapper
from Lola.services.bocuse.mappers import BocuseEquipamentosMapper
from Lola.services.bocuse.mappers import BocuseInformacoesMapper
from Lola.services.bocuse.mappers import BocuseIngredientesMapper
from Lola.services.bocuse.mappers import BocuseMenuMapper
from Lola.services.bocuse.mappers import BocusePreparosMapper


class BocuseService:
    def menu(self):
        menu = BocuseClient().getMenu()
        return BocuseMenuMapper.to_dto(menu)

    def cardapio(self, cardapio_name):
        menu = BocuseClient().getMenu()
        cardapio = next(item for item in menu if item["name"] == cardapio_name)
        return BocuseCardapioMapper.to_dto(cardapio)

    def ingredientes(self, receita_id):
        receita = BocuseClient().getReceita(receita_id)
        return BocuseIngredientesMapper.to_text(receita)

    def equipamentos(self, receita_id):
        receita = BocuseClient().getReceita(receita_id)
        return BocuseEquipamentosMapper.to_text(receita)

    def preparos(self, receita_id):
        receita = BocuseClient().getReceita(receita_id)
        return BocusePreparosMapper.to_text(receita)

    def informacoes(self, receita_id):
        receita = BocuseClient().getReceita(receita_id)
        return BocuseInformacoesMapper.to_text(receita)
