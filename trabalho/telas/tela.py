from abc import ABC, abstractmethod
from trabalho.exception.negativeValueException import NegativeValueException


class Tela(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def mostra_opcoes(self):
        pass

    @abstractmethod
    def mostra_mensagem(self, msg):
        print(msg)

    def le_int_validos(self, int_validos: list, msg_input):
        while True:
            variavel = input(msg_input)
            try:
                opcao = int(variavel)
                if opcao not in int_validos:
                    raise ValueError
                return opcao
            except ValueError:
                print('Digite um valor válido.')

    def le_int_positivo(self, msg_input):
        while True:
            variavel = input(msg_input)
            try:
                variavel_int = int(variavel)
                if variavel_int < 0:
                    raise NegativeValueException
                return variavel_int
            except ValueError:
                print('Esse valor deve ser um inteiro.')
            except NegativeValueException:
                print('Esse valor deve ser positivo.')
