'''
3) Faça uma função que receba duas palavras
e retorne um dicionario contendo:
"Sol" "Lua"
{'S':'L','o':'u','l':'a'}

pode retornar desordenado

traduzindo o exercicio...

pegar os elementos das duas palavras digitadas, do ultimo ate o primeiro e
imprimir na tela

elementos:
    {'indice0 de p1' : 'indice0 de p2',
    'indice1 de p1' : 'indice1 de p2',
    ...
    }

'''

def dicio(p1,p2):
    d = {}
    z = zip(p1,p2) #[('S','L'),('o','u'),('l','a')]
    for x in z:
        d[x[0]] = x[1]
    
    return d

palavra1 = raw_input("Digite a palavra 1: ")
palavra2 = raw_input("Digite a palavra 2: ")


dicio(palavra1,palavra2)

'''
outra solução:

def ex3(p1,p2):
    d = {}
    z = zip(p1,p2) #[('S','L'),('o','u'),('l','a')]
    for (x,y) in z:
        d[x] = y
    
    return d

palavra1 = raw_input("Digie uma palavra: ")
palavra2 = raw_input("Digie outra palavra: ")
print ex3(palavra1,palavra2)

'''