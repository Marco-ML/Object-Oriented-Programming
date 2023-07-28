#Autor: Marco Aurélio Araújo da Costa

from relogio import Relogio

if __name__ == '__main__':
    r = Relogio(23, 23, 1)
    r1 = Relogio(23,23, 1)
    print(r + r1)
    print(r - r1)
    print(r1 - r)
    print(r == r1)
    print(r > r1)
    print(r < r1)