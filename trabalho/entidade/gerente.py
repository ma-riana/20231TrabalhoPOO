from trabalho.entidade.funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome: str, cpf: str, data_nasc: str):
        super().__init__(nome, cpf, data_nasc)
        self.__contratos = []

    @property
    def contratos(self):
        return self.__contratos

    def add_contrato(self, contrato):
        self.__contratos.append(contrato)

    def rem_contrato(self, contrato):
        self.__contratos.remove(contrato)