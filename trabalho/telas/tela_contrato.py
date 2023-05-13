from trabalho.telas.tela import Tela
from trabalho.entidade.contrato import Contrato
from trabalho.entidade.transferencia import Transferencia
from trabalho.entidade.mud_cargo import MudancaCargo


class TelaContrato(Tela):

    def __init__(self):
        pass

    def mostra_opcoes(self):
        print('\nTELA DE MODIFICAÇÃO: CONTRATO\n'
              + '1) Mostrar contrato\n'
              + '2) Listar ocorrencias\n'
              + '0) Retornar\n')
        opcao = self.le_int_validos([0, 1, 2], 'Escolha uma opção: ')
        return opcao

    def listar_contrato(self, contrato: Contrato):
        print(f'''
        === CONTRATO NUM {contrato.id} ===
        Funcionario: {contrato.empregado.nome}
        CPF: {contrato.empregado.cpf}
        Empregador: {contrato.empregador.nome}
        CPF: {contrato.empregador.cpf}
        Cargo: {contrato.cargo.titulo}
        Filial: {contrato.filial.cep}
        Data de emissão: {contrato.data_inicio}
        Data de termino: {contrato.data_final}
        ''')

    def listar_transferencia(self, transf: Transferencia):
        print(f'\n=== Transferência ==='
              + f'Filial antiga: {transf.filial_antiga.cep}\n'
              + f'Filial atual: {transf.filial_nova.cep}\n'
              + f'Data: {transf.data}\n')

    def listar_mud_cargo(self, mud_cargo: MudancaCargo):
        print(f'\n=== Mudança de cargo ==='
              + f'Cargo antiga: {mud_cargo.cargo_antigo}\n'
              + f'Cargo atual: {mud_cargo.cargo_novo}\n'
              + f'Data: {mud_cargo.data}\n')
