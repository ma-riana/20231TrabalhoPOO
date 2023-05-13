from trabalho.entidade.cargo import Cargo
from trabalho.entidade.funcionario import Funcionario
from datetime import date


class MudancaCargo:

    def __init__(self, cargo_novo: Cargo,
                 cargo_antigo: Cargo,
                 funcionario: Funcionario,
                 data: date):
        self.__cargo_novo = cargo_novo
        self.__cargo_antigo = cargo_antigo
        self.__funcionario = funcionario
        self.__data = data

    @property
    def cargo_novo(self):
        return self.__cargo_novo

    @property
    def cargo_antigo(self):
        return self.__cargo_antigo

    @property
    def funcionario(self):
        return self.__funcionario

    @property
    def data(self):
        return self.__data

    @cargo_novo.setter
    def cargo_novo(self, cargo_novo: Cargo):
        if isinstance(cargo_novo, Cargo):
            self.__cargo_novo = cargo_novo

    @cargo_antigo.setter
    def cargo_antigo(self, cargo_antigo: Cargo):
        if isinstance(cargo_antigo, Cargo):
            self.__cargo_antigo = cargo_antigo

    @funcionario.setter
    def funcionario(self, funcionario: Funcionario):
        if isinstance(funcionario, Funcionario):
            self.__funcionario = funcionario

    @data.setter
    def data(self, data: date):
        if isinstance(data, str):
            self.__data = data
