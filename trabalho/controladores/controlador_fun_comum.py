from trabalho.telas.tela_fun_comum import TelaFuncomum
from trabalho.exception.repeticao import Repeticao
from trabalho.entidade.cargo import Cargo


class ControladorFunComum:

    def __init__(self):
        self.__tela_fun_comum = TelaFuncomum()
        self.__fun_comuns = []
        self.__fun_comuns_cargos = [Cargo('Atendente', 2500),
                                    Cargo('Limpeza', 1800)]

    @property
    def fun_comuns(self):
        return self.__fun_comuns

    @property
    def fun_comuns_cargos(self):
        return self.__fun_comuns_cargos

    def add_fun_comum(self, fun_comum):
        self.__fun_comuns.append(fun_comum)

    def checagem_repeticao(self, cpf):
        while True:
            try:
                for _ in self.__fun_comuns:
                    if _.cpf == cpf:
                        raise Repeticao('CPF', cpf)
                return True
            except Repeticao:
                return False
