#Autor: Marco Aurélio Araújo da Costa
class Relogio:
    '''
    Classe que cria uma relógio contendo hora, minuto e segundo.
    '''
    
    def __init__(self, hora: int, minuto: int, segundo: int):
        '''
        Atributos:
            hora: valor da hora(int) | de 0 até 23.
            minuto: valor do minuto(int) | de 0 até 59. 
            segundo: valor do segundo(int) | de 0 até 59.
        '''
        if segundo > 59:
            for i in range(1, segundo//60 + 1):
                minuto += 1
                segundo -= 60
        if minuto > 59:
            for i in range(1, minuto//60 + 1):
                hora += 1
                minuto -= 60
        if hora > 23:
            for i in range(1, hora//24 + 1):
                hora-=24
    
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
        
    def __str__(self):
        return f'{self.hora}:{self.minuto}:{self.segundo}'

    def __add__(self, outro):
        h = self.hora + outro.hora
        m = self.minuto + outro.minuto
        s = self.segundo + outro.segundo
        if s > 59:
            for i in range(1, s//60 + 1):
                m += 1
                s -= 60
        if m > 59:
            for i in range(1, m//60 + 1):
                h += 1
                m -= 60
        if h > 23:
            for i in range(1, h//24 + 1):
                h-=24
        return Relogio(h, m, s)
    
    def __sub__(self, outro):
        if (self.hora > outro.hora):
            h = self.hora - outro.hora
            m = self.minuto - outro.minuto
            s = self.segundo - outro.segundo
            if s < 0:
                s += 60
                m -= 1
            if m < 0:
                m += 60
                h -= 1
            return Relogio(h, m, s)
        
        elif (self.hora == outro.hora) and (self.minuto > outro.minuto):
            h = self.hora - outro.hora
            m = self.minuto - outro.minuto
            s = self.segundo - outro.segundo
            if s < 0:
                s+=60
                m-=1
            return Relogio(h, m, s)
        elif (self.hora == outro.hora) and (self.minuto == outro.minuto) and (self.segundo > outro.segundo):
            h = self.hora - outro.hora
            m = self.minuto - outro.minuto
            s = self.segundo - outro.segundo
            return Relogio(h, m, s)
        else:
            print('O primeiro horário deve ser maior do que o segundo horário.')
    
    def __eq__(self, outro):
        if (self.hora == outro.hora) and (self.minuto == outro.minuto) and (self.segundo == outro.segundo):
            return True
        else:
            return False
        
    def __gt__(self, outro):
        if self.hora > outro.hora:
            return True
        elif (self.hora == outro.hora) and (self.minuto > outro.minuto):
            return True
        elif (self.hora == outro.hora) and (self.minuto == outro.minuto) and (self.segundo > outro.segundo):
            return True
        else:
            return False
        
    def __it__(self):
        if self.hora < outro.hora:
            return True
        elif (self.hora == outro.hora) and (self.minuto < outro.minuto):
            return True
        elif (self.hora == outro.hora) and (self.minuto == outro.minuto) and (self.segundo < outro.segundo):
            return True
        else:
            return False