from trabalho.telas.tela_gerente import TelaGerente
from trabalho.entidade.gerente import Gerente
from trabalho.exception.repeticao import Repeticao


class ControladorGerente:

    def __init__(self, controlador_filial):
        self.__controlador_filial = controlador_filial
        self.__tela_gerente = TelaGerente()
        self.__gerentes = [Gerente("Lucas", "999", "01012000")]

    def inicializa_sistema(self):
        lista_opcoes = {1: self.modificar_dados, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_gerente.mostra_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def modificar_dados(self):
        self.__tela_gerente.mostra_mensagem('=== Modificação de dados ===')
        opcao = self.__tela_gerente.menu_modificacao()
        if opcao == 1:
            pass
        if opcao == 2:
            pass
        if opcao == 3:
            pass
        if opcao == 0:
            return

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
