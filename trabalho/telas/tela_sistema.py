from trabalho.telas.tela import Tela
from trabalho.controladores.controlador_gerente import ControladorGerente


class TelaSistema(Tela):

    def __init__(self):
        super().__init__()
        self.__controlador_gerente = ControladorGerente()

    def mostra_opcoes(self):
        print("Seja bem vindo ao sistema de controle de filiais.\n"
              + "O que deseja fazer?\n"
              + "1) Adicionar uma filial\n"
              + "2) Excluir uma filial\n"
              + "3) Modificar uma filial\n"
              + "4) Listar filiais por atividade\n"
              + "0) Sair\n")
        opcao = super().le_int_validos([0, 1, 2, 3, 4], "Escolha uma opção: ")
        return opcao

    def pega_dados_cadastro(self):
        print("TELA DE CADASTRO: FILIAL")
        cep = super().le_int_positivo("Informe o CEP: ")
        cidade = input("Informe a cidade: ")
        gerente = self.__controlador_gerente.add_gerente()
        nova_filial = {"cep": cep, "cidade": cidade, "gerente": gerente}
        return nova_filial

    def pega_cep(self):
        cep = self.le_int_positivo("Informe o CEP: ")
        return cep

    def listagem(self, cep, cidade):
        print(f"CEP: {cep}\nCidade: {cidade}\n")

    def mostra_mensagem(self, msg):
        return super().mostra_mensagem(msg)
