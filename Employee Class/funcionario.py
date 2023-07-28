class Funcionario:
    '''
    Classe que cria um funcionário.
    '''
    
    def __init__(self, nome: str, cpf: str):
        '''
        Atributos:
            nome: nome do funcionário(str).
            cpf: cpf do funcionário(str).
        '''
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = 0
   
    def getNome(self) -> str:
        '''
        Método que retorna o nome do funcionário.
        '''
        return self.__nome
