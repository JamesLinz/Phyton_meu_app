from aula7_televisao import Televisao
from aula7_televisao import Calculadora
from aula8_contador_letras import contador_letras, teste


if __name__ == '__main__' :
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora()
    print(calculadora.soma(10, 2))
    print(calculadora.subtracao(5, 3))
    print(calculadora.multiplicacao(100, 2))
    print(calculadora.divisao(10, 5))

    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print('Total de letras por palavra na lista: {}'.format(total_letras))
    print(teste())

