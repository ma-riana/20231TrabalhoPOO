from trabalho.telas.tela import Tela


class TelaFuncionario(Tela):

    def __init__(self):
        super().__init__()

    def mostra_opcoes(self):
        pass

    def menu_modificacao(self):
        print("O que deseja modificar?\n"
              + "1) Nome\n"
              + "2) CPF\n"
              + "3) Data de nascimento\n"
              + "0) Retornar\n")
        opcao = super().le_int_validos([1, 2, 3, 0], "Escolha uma opçao: ")
        return opcao

    def pega_dados_cadastro(self):
        nome = input("Nome: ")
        cpf = input("CPF: ")
        data_nasc = input("Data de nascimento: ")
        novo_funcionario = {'nome': nome, 'CPF': cpf, "data_nasc": data_nasc}
        return novo_funcionario





