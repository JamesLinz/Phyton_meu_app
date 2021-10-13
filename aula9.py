import shutil

def escrever_arquivo(texto):
    diretorio = 'C:/Users/jale/PycharmProjects/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.write('\nPrimeira linha')
    arquivo.write('\nSegunda linha')
    arquivo.write('\nTerceira linha')
    arquivo.close()

# def atualizar_arquivo(texto):
#     arquivo = open('teste.txt', 'a')
#     arquivo.write(texto)
#     arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        # print(x)
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media
        # print(sum(lista_notas))


def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Users/jale/PycharmProjects')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/jale/PycharmProjects/')


if __name__ == '__main__':
    move_arquivo('notas.txt')
    # copia_arquivo('notas.txt')
    #
    # lista_media = media_notas('notas.txt')
    # print(lista_media)
    #
    # escrever_arquivo('Primeira linha.\n')
    # aluno = 'Rafael, 10, 10, 5, 5'
    # aluno = '\nFelipe, 9, 10, 7, 5'
    # aluno = '\nPedro, 9, 10, 6, 8'
    # atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('teste.txt')