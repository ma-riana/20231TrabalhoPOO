from trabalho.telas.tela_gerente import TelaGerente
from trabalho.entidade.gerente import Gerente
from trabalho.exception.repeticao import Repeticao


class ControladorGerente:

    def __init__(self):
        self.__tela_gerente = TelaGerente()
        self.__gerentes = [Gerente("Lucas", "999", "01012000")]

    def add_gerente(self):
        self.__tela_gerente.mostra_mensagem("=== Cadastro de gerente ===")
        while True:
            novo_gerente = self.__tela_gerente.pega_dados_cadastro()
            if self.checagem_repeticao(novo_gerente['CPF']):
                break
            self.__tela_gerente.mostra_mensagem('CPF já cadastrado.')
        self.__gerentes.append(Gerente(novo_gerente['nome'], novo_gerente['CPF'], novo_gerente['data_nasc']))
        return self.__gerentes[-1]

    def checagem_repeticao(self, cpf):
        while True:
            try:
                for _ in self.__gerentes:
                    if _.cpf == cpf:
                        raise Repeticao('CPF', cpf)
                return True
            except Repeticao:
                return False
