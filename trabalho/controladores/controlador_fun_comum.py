from trabalho.telas.tela_fun_comum import TelaFuncomum
from trabalho.exception.repeticao import Repeticao

class ControladorFunComum:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_fun_comum = TelaFuncomum()
        self.__fun_comuns = []

    @property
    def fun_comuns(self):
        return self.__fun_comuns

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
