from funcionario import Funcionario

class TrabalhadorHorista(Funcionario):
    '''
    Classe que cria um trabalhador horista.
    '''
    def __init__(self, nome: str, cpf: str, valorHora: float, horasTrabalhadasMes: float):
        '''
        Atributos:
            nome: Nome do trabalhador horista(str).
            cpf: cpf do trabalhador horista(str).
            valorHora: Valor cobrado por hora pelo trabalhador horista(float).
            horasTrabalhadasMes: Horas trabalhadas no mês(float).
        '''
        super().__init__(nome, cpf)
        self.__valorHora = valorHora
        self.__horasTrabalhadasMes = horasTrabalhadasMes
        
    @property    
    def calcularPagamento(self):
        '''
        Método responsável por retornar o cálculo do salário do trabalhador horista.
        Retorna:
            A multiplicação do valor da hora pelas horas trabalhadas no mês(float).
        '''
        if (self.__valorHora > 0) and (self.__horasTrabalhadasMes > 0):
            return self.__valorHora * self.__horasTrabalhadasMes
    
    @calcularPagamento.setter
    def calcularPagamento(self):
        '''
        Método que calcula o salário do trablhador horista dado as horas trabalhadas e o valor da hora.
        '''
        if (self.__valorHora > 0) and (self.__horasTrabalhadasMes > 0):
            self.__salario = self.__valorHora * self.__horasTrabalhadasMes
