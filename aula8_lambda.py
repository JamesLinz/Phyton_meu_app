contador_letras = lambda lista: [len(x) for x in lista]
lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))



soma = lambda a, b: a + b
print(soma(5, 10))

subtracao = lambda a, b: a - b
print(subtracao(10, 5))

multiplicacao = lambda a, b: a * b
print(multiplicacao(10, 5))

divisao = lambda a, b: a / b
print(divisao(10, 5))



calculadora = {
    'soma': lambda a,b: a + b,
    'subtracao': lambda a,b: a - b,
    'multiplicacao': lambda a,b: a * b,
    'divisao': lambda a,b: a / b,
}

print(type(calculadora))
soma = calculadora['soma']
subtracao = calculadora['subtracao']
multiplicacao = calculadora['multiplicacao']
divisao = calculadora['divisao']

print('A soma é: {}'.format(soma(5, 10)))
print('A subtracao é: {}'.format(subtracao(10, 5)))
print('A multiplicao é: {}'.format(multiplicacao(10, 5)))
print('A divisao é: {}'.format(divisao(10, 5)))

