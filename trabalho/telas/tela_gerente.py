from trabalho.telas.tela_funcionarios import TelaFuncionario


class TelaGerente(TelaFuncionario):

    def __init__(self):
        super().__init__()

    def mostra_mensagem(self, msg):
        super().mostra_mensagem(msg)

    def mostra_opcoes(self):
        opcao = input("TELA DE MODIFICAÇÃO: GERENTE"
                      + "O que deseja fazer?"
                      + "1) Listar informações do gerente atual"
                        "2) Listar contratos realizados"
                      + "3) Modificar informações do gerente atual"
                      + "4) Demitir gerente"
                        "6) Mudar cargo do gerente"
                      + "7) Transferir gerente")

    def menu_modificacao(self):
        return super().menu_modificacao()

    def pega_dados_cadastro(self):
        return super().pega_dados_cadastro()

    def menu_nova_gerencia(self):
        op_novo_gerente = input("Informe o próximo gerente:"
                                + "1) Promover funcionário"
                                + "2) Cadastrar novo gerente")
        return op_novo_gerente



