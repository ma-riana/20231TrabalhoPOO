class ValorInvalido(Exception):
    def __init__(self, variavel, tipo_correto):
        super().__init__(f"Variavel '{variavel}' não suporta esse valor. "
                         + f"Repita o cadastro usando {tipo_correto}.")