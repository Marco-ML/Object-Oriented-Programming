#Autor: Marco Aurélio Araújo da Costa

from funcionario import Funcionario

class TrabalhadorAssalariado(Funcionario):
    '''
    Classe que cria um trabalhador assalariado.
    '''
    def __init__(self, nome: str, cpf: str, salario: float):
        '''
        Atributos:
            nome: nome do trabalhador assalariado(str).
            cpf: cpf do trabalhador assalariado(str).
            salario: salario do trabalhador assalariado(float).
        '''
        super().__init__(nome, cpf)
        self.__salario = salario

    @property   
    def definirSalario(self):
        '''
        Método que retorna o salário do trabalhador assalariado.
	Retorna:
		salario: O novo salário do trabalhador assalariado.
        '''
        return self.__salario
     
    @definirSalario.setter    
    def definirSalario(self, salario: float) :
        '''
        Método que reajusta o salário do trabalhador assalariado.
        Atributos:
            salario: Novo salário(float).
        '''
        self.__salario = salario