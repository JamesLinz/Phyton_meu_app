a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
print(type(a))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

print('Soma: {soma}. \nSubtração: {subtracao}. '
      '\nMultiplicação: {multiplicacao}'
      '\nDivisão: {divisao}'
      '\nResto: {resto}'.format(soma=soma,
                                subtracao=subtracao,
                                multiplicacao=multiplicacao,
                                divisao=divisao,
                                resto=resto))

# print('soma: ' + str(soma))
# print('subtracao: ' + str(subtracao))
# print('multiplicacao: ' + str(multiplicacao))
# print('int(divisao): ' + str(int(divisao)))
# print('divisao: ' + str(divisao))
# print('resto: ' + str(resto))

# x = '1'
# soma2 = int(x) + 1
# print(soma2)