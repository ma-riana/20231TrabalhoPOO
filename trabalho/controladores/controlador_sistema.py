from trabalho.entidade.filial import Filial
from trabalho.entidade.gerente import Gerente
from trabalho.telas.tela_sistema import TelaSistema
from trabalho.exception.repeticao import Repeticao
from trabalho.exception.naoExistencia import NaoExistencia


class ControladorSistema:

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__lista_filiais = [Filial(222, "Floripa", Gerente("oi", "00000", "09092000"))]

    def inicializa_sistema(self):
        lista_opcoes = {1: self.adicionar_filial, 2: self.excluir_filial,
                        3: self.modificar_filial, 4: self.listar_por_atv,
                        0: self.sair}

        while True:
            opcao_escolhida = self.__tela_sistema.mostra_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def adicionar_filial(self):
        while True:
            dados_nova_filial = self.__tela_sistema.pega_dados_cadastro()
            # Checagem de repetição
            if self.checagem_repeticao(dados_nova_filial['cep'], dados_nova_filial['cidade']):
                break
        self.__lista_filiais.append(Filial(dados_nova_filial['cep'], dados_nova_filial['cidade'], dados_nova_filial['gerente']))
        print('Filial cadastrada com sucesso.')

    def excluir_filial(self):
        self.__tela_sistema.mostra_mensagem('=== EXCLUSÃO DE FILIAIS ===\nRealize a busca.')
        filial = self.busca_por_cep()
        self.__lista_filiais.remove(filial)
        self.__tela_sistema.mostra_mensagem('Filial excluída com sucesso.')

    def modificar_filial(self):
        pass

    def listar_por_atv(self):
        self.__tela_sistema.mostra_mensagem("=== Listagem de filiais ===\n")
        for _ in self.__lista_filiais:
            self.__tela_sistema.listagem(_.cep, _.cidade)

    # Método de checagem de repetição
    def checagem_repeticao(self, cep, cidade):
        try:
            for _ in self.__lista_filiais:
                if _.cep == cep:
                    raise Repeticao('CEP', cep)
                if _.cidade == cidade:
                    raise Repeticao('Cidade', cidade)
            return True
        except Repeticao:
            return False

    def busca_por_cep(self):
        while True:
            cep_buscado = self.__tela_sistema.pega_cep()
            try:
                for _ in self.__lista_filiais:
                    if _.cep == cep_buscado:
                        return _
                raise NaoExistencia
            except NaoExistencia:
                print('Filial não encontrada. Tente novamente.')

    def sair(self):
        exit(0)

