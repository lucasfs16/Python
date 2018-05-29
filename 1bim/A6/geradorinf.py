#GERADOR
def g1():
    yield 1
    yield 2
    yield 3
    yield 4

def g2():
    i = 0
    #loop infinito
    while True:
        yield i
        i = i + 2

def g3(seed):
    x = []
    for n in seed:
        x.append(int(n))
    i = 0
    while True:
        #x[i+2]
        formula = x[i+3] ^ x[i]
        x.append(formula)
        yield formula
        i = i + 1
    
#  0110010001111010.    
#gerador sera um objeto da classe dos geradores
gerador = g3("0110")
print "Digite quantos numeros: "
n = int(raw_input())
for i in range(n):
    print gerador.next()