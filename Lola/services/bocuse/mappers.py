from Lola.core.mapper import Mapper


class BocuseMenuMapper(Mapper):
    def to_dto(menu):
        for cardapio in menu:
            del cardapio["receitas"]
        return menu


class BocuseCardapioMapper(Mapper):
    def to_dto(categoria):
        return categoria["receitas"]


class BocuseIngredientesMapper(Mapper):
    def to_text(receita):
        etapas = receita["ingredientes"]
        text = ""
        for etapa in etapas:
            etapa_name = etapa["etapa"]
            text += f"\n\n{etapa_name}"
            for ingrediente in etapa["ingredientes"]:
                name = ingrediente["nome"]
                quantidade = ingrediente["quantidade"]
                medida = ingrediente["medida"]
                text += f"\n    {name}: {quantidade} {medida}"
        return text


class BocuseEquipamentosMapper(Mapper):
    def to_text(receita):
        equipamentos = receita["equipamentos"]
        text = "\n\nequipamentos"
        for equipamento in equipamentos:
            if equipamento["necessario"]:
                name = equipamento["nome"]
                text += f"\n    {name}"
        return text


class BocusePreparosMapper(Mapper):
    def to_text(receita):
        preparos = receita["preparos"]
        text = ""
        for preparo in preparos:
            etapa = preparo["etapa"]
            passos = preparo["passos"]
            text += f"\n\n{etapa}"
            for passo in passos:
                descricao = passo["descricao"]
                text += f"\n    {descricao}"
        return text


class BocuseInformacoesMapper(Mapper):
    def to_text(receita):
        infomecoes = receita["informacoes"]
        redimento = infomecoes["rendimento"]
        porcao = infomecoes["porcao"]
        unidades = infomecoes["unidades"]
        text = (
            f"\n\ninformações"
            f"\n    redimento: {redimento}"
            f"\n    porcao: {porcao}"
            f"\n    unidades: {unidades}"
        )
        return text
