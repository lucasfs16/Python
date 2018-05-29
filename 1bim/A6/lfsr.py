
'''
#GERADOR
def g1():
    yield 1
    yield 2
    yield 3
    yield 4

        
#gerador sera um objeto da classe dos geradores
gerador = g1()
print gerador.next()
print gerador.next()
print gerador.next()
print gerador.next()
#print gerador.next() ISSO daria erro porque so vai ate o 4


#gerador infinito:

def g2():
    i = 0
    #loop infinito
    while True:
        yield i
        i = i + 2
        
#gerador sera um objeto da classe dos geradores
gerador = g2()
print gerador.next()
print gerador.next()
print gerador.next()
print gerador.next()
print gerador.next()

'''

def g3(seed):
    x = []
    for n in seed:
        x.append(int(n))
    i = 0
    while True:
        #x[i+2]
        formula = x[i+1] ^ x[i]
        x.append(formula)
        yield formula
        i = i + 1
    
#gerador sera um objeto da classe dos geradores
gerador = g3("11")

for i in range(10):
    print gerador.next()
    
