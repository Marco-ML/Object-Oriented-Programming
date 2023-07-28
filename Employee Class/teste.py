#Autor: Marco Aurélio Araújo da Costa

from funcionario import Funcionario
from trabalhadorassalariado import TrabalhadorAssalariado
from trabalhadorhorista import TrabalhadorHorista


if __name__ == '__main__':
    TA1 = TrabalhadorAssalariado('José', '1348509284', 2000)
    TA1.definirSalario = 2500
    s1 = TA1.definirSalario
    TH1 = TrabalhadorHorista('Allan', '1358509283', 100, 34)
    s2 = TH1.calcularPagamento
    TA2 = TrabalhadorAssalariado('Carol', '1248519280', 3000)
    TA2.definirSalario = 2500
    s3 = TA2.definirSalario
    TH2 = TrabalhadorHorista('Roberto', '0358509282', 50, 45)
    s4 = TH2.calcularPagamento
    TA3 = TrabalhadorAssalariado('Luan', '1248510280', 4000)
    TA3.definirSalario = 2500
    s5 = TA3.definirSalario
    TH3 = TrabalhadorHorista('Livia', '2358509262', 56, 23)
    s6 = TH3.calcularPagamento
    funcionarios = [TA1, TH1, TA2, TH2, TA3, TH3]
    salarios = [s1, s2, s3, s4, s5, s6]
    for i, j in zip(funcionarios, salarios):
        print('Nome: ', i.getNome(),'|', 'Pagamento: ', j)