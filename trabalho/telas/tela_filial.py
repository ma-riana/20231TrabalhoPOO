from trabalho.telas.tela import Tela

class TelaFilial(Tela):

    def __init__(self, cep):
        self.__cep = cep
        # self.__controlador_filial = ControladorFilial
        pass

    def abre_menu(self):
        opcao = input("TELA DE MODIFICAÇÃO: FILIAL POR CEP"
                      + "O que deseja fazer?"
                      + "1) Listar funcionários por atividade"
                      + "2) Acessar histórico de mudanças"
                      + "3) Acessar opções de funcionário comum"
                      + "4) Acessar opçoes de gerencia"
                      + "5) Retornar")



