class Cargo:
    def __init__(self, titulo, salario):
        self.__titulo = titulo
        self.__salario = salario

    @property
    def titulo(self):
        return self.__titulo

    @property
    def salario(self):
        return self.__salario

    @titulo.setter
    def titulo(self, titulo: str):
        if isinstance(titulo, str):
            self.__titulo = titulo

    @salario.setter
    def salario(self, salario: float):
        if isinstance(salario, float):
            self.__salario = salario