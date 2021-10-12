
# def soma(a, b):
#     return a + b
#
# def subtracao(a, b):
#     return a - b
#
# def multiplicacao(a, b):
#     return a * b
#
# def divisao(a, b):
#     return a / b
#
# print(soma(1, 2))
# print(soma(3, 4))
#
# print(subtracao(10, 2))
#
# print(multiplicacao(10, 2))
#
# print(divisao(10, 2))


class Calculadora:

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b


if __name__ == '__main__' :
    calculadora = Calculadora()
    print(calculadora.soma(10, 2))
    print(calculadora.subtracao(5, 3))
    print(calculadora.multiplicacao(100, 2))
    print(calculadora.divisao(10, 5))


class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1



# televisao = Televisao()
# print('Televisão está ligada: {}'.format(televisao.ligada))
# televisao.power()
# print('Televisão está ligada: {}'.format(televisao.ligada))
# televisao.power()
# print('Televisão está ligada: {}'.format(televisao.ligada))
#
# print('Canal: {}'.format(televisao.canal))
# televisao.power()
# print('Televisão está ligada: {}'.format(televisao.ligada))
# televisao.aumenta_canal()
# televisao.aumenta_canal()
# print('Canal: {}'.format(televisao.canal))
# televisao.diminui_canal()
# print('Canal: {}'.format(televisao.canal))



if __name__ == '__main__' :
    televisao = Televisao()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))

    print('Canal: {}'.format(televisao.canal))
    televisao.power()
    print('Televisão está ligada: {}'.format(televisao.ligada))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.diminui_canal()
    print('Canal: {}'.format(televisao.canal))
