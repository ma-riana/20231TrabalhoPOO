from trabalho.telas.tela_filial import TelaFilial
from trabalho.entidade.filial import Filial
from trabalho.controladores.controlador_sistema import ControladorSistema
from trabalho.controladores.controlador_gerente import ControladorGerente
from trabalho.controladores.controlador_fun_comum import ControladorFunComum



class ControladorFilial:

    def __init__(self, controlador_sistema: ControladorSistema, filial: Filial):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_gerente = ControladorGerente(self)
        self.__controlador_fun_comum = ControladorFunComum(self)
        self.__filial = filial
        self.__tela_filial = TelaFilial()

    def inicializa_sistema(self):
        lista_opcoes = {1: self.controlador_funcomum, 2: self.controlador_gerente,
                        3: self.modificar_dados, 4: self.registro_ocorrencias,
                        5: self.listar_por_atv, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_filial.mostra_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def controlador_funcomum(self):
        pass

    def controlador_gerente(self):
        pass

    def modificar_dados(self):
        pass

    def registro_ocorrencias(self):
        pass

    def listar_por_atv(self):
        pass

    def retornar(self):
        pass
