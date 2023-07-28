#Autor: Marco Aurélio Araújo da Costa
class Ponto:
    '''
    Classe que cria um ponto no plano cartersiano.
    '''
    
    def __init__(self, x: float, y: float):
        '''
        Atributos:
            x: valor para o ponto x(float).
            y: valor para o ponto y(float).
        '''
        self.x = x
        self.y = y
    
    
    def __str__(self):
        return f'({self.x}, {self.y})'
        
    def __add__(self, outro):
        return (self.x + outro.x, self.y + outro.y)
    
    def __sub__(self, outro):
        return (self.x - outro.x, self.y - outro.y)
    
    def __mul__(self, outro):
        return self.x * outro.x + self.y * outro.y
    
    def __rmul__(self, n):
        return Ponto(n * self.x , n * self.y)