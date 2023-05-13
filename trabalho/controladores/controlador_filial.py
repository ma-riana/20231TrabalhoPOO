from trabalho.telas.tela_filial import TelaFilial
from trabalho.entidade.filial import Filial
from trabalho.controladores.controlador_gerente_esp import ControladorGerenteEsp
from trabalho.controladores.controlador_fun_comum_esp import ControladorFunComumEsp


class ControladorFilial:

    def __init__(self, controlador_sistema, controlador_contrato, filial: Filial):
        self.__controlador_contrato = controlador_contrato
        self.__controlador_sistema = controlador_sistema
        self.__filial = filial
        self.__tela_filial = TelaFilial()

    @property
    def filial(self):
        return self.__filial

    def inicializa_sistema(self):
        lista_opcoes = {1: self.controlador_funcomum, 2: self.controlador_gerente,
                        3: self.modificar_dados, 4: self.registro_ocorrencias,
                        5: self.listar_por_atv, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_filial.mostra_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def controlador_funcomum(self):
        ControladorFunComumEsp(self, self.__controlador_contrato, self.__controlador_sistema,
                               self.__filial.funcionarios).inicializa_sistema()

    def controlador_gerente(self):
        ControladorGerenteEsp(self, self.__controlador_contrato, self.__controlador_sistema,
                              self.__filial.gerente).inicializa_sistema()

    def modificar_dados(self):
        opcao = self.__tela_filial.menu_modificacao()
        if opcao == 1:
            while True:
                cep_novo = self.__tela_filial.le_cep("Digite o cep novo: ")
                if self.__controlador_sistema.checagem_repeticao_cep(cep_novo):
                    break
            self.__filial.cep = cep_novo

        elif opcao == 2:
            while True:
                cidade_nova = self.__tela_filial.pega_input("Digite a cidade nova: ")
                if self.__controlador_sistema.checagem_repeticao_cidade(cidade_nova):
                    break
            self.__filial.cidade = cidade_nova
        elif opcao == 0:
            return

    def registro_ocorrencias(self):
        pass

    def listar_por_atv(self):

        lista_fun = self.__filial.funcionarios
        if len(lista_fun) > 0:
            for fun in lista_fun:
                self.__tela_filial.listagem(fun.nome, fun.cpf, fun.data_nasc)
        else:
            self.__tela_filial.mostra_mensagem('Lista vazia.')

    def retornar(self):
        self.__controlador_sistema.inicializa_sistema()
