from trabalho.entidade.contrato import Contrato
from trabalho.telas.tela_contrato import TelaContrato


class ControladorContrato:

    def __init__(self):
        self.__tela_contrato = TelaContrato()
        self.__contratos = []

    @property
    def tela_contrato(self):
        return self.__tela_contrato

    def inicializa_sistema(self, controlador_de_retorno, objeto):
        lista_opcoes = {1: self.listar_contrato, 2: self.listar_ocorrencias,
                        0: controlador_de_retorno.inicializa_sistema}

        while True:
            opcao_escolhida = self.__tela_contrato.mostra_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            if funcao_escolhida == lista_opcoes[1]:
                self.listar_contrato(objeto)
            if funcao_escolhida == lista_opcoes[2]:
                self.listar_ocorrencias(objeto)
            else:
                controlador_de_retorno.inicializa_sistema()

    def incluir_contrato(self, dados_contrato):
        dados_contrato = dados_contrato
        id = self.gera_id()
        dados_contrato['empregado'].atividade = True

        novo_contrato = Contrato(id, dados_contrato['data_inicio'], dados_contrato['cargo'],
                                 dados_contrato['empregado'], dados_contrato['filial'],
                                 dados_contrato['empregador'])
        self.__contratos.append(novo_contrato)
        dados_contrato['empregador'].add_contrato(novo_contrato)

    def listar_contrato(self, objeto):
        cpf = objeto.cpf
        contrato = self.pega_contrato_por_cpf_auto(cpf)
        self.__tela_contrato.listar_contrato(contrato)

    def listar_ocorrencias(self, funcionario):
        cpf = funcionario.cpf
        contrato = self.pega_contrato_por_cpf_auto(cpf)
        if len(contrato.transferencias) > 0:
            for transf in contrato.transferencias:
                self.__tela_contrato.listar_transferencia(transf)
        if len(contrato.mud_cargos) > 0:
            for mud in contrato.mud_cargos:
                self.__tela_contrato.listar_mud_cargo(mud)
        else:
            self.__tela_contrato.mostra_mensagem('Lista vazia.')

    def pega_contrato_por_cpf_auto(self, cpf):
        for contrato in self.__contratos:
            if contrato.empregado.cpf == cpf:
                return contrato

    def gera_id(self):
        if len(self.__contratos) > 0:
            return self.__contratos[-1].id + 1
        else:
            return 0
