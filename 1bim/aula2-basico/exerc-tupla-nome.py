
#exercicios usando listas - http://www.learnpython.org/en/Lists 

#EXERCICIO:

#1) Faça um programa que digite dois nomes, 
#de mesmo tamanho, e mosrte na tela 
#um array contendo tuplas de letras 
#de cada nome.
#Exemplo: "ANA " e "BOB"
#mostrará: [('A','B'),('N','O'),('A','B')]


#entendendo o exercicio...
# lendo o exemplo: uma lista com 3 tuplas dentro sendo q a tupla1 tem o elemento 0 do n1 e o elemento 0 do n2


n1 = raw_input("Digite o nome 1: ")
n2 = raw_input("Digite o nome 2: ")

aux = [] 
t = () #tupla q é imutavel

for i in range(len(n1))
    
    aux.append((n1[i],n2[i]))

print aux

'''    
------------------------------------------------------------------------- 
SOLUÇAO 2:


n1 = raw_input("Digite o nome 1: ")
n2 = raw_input("Digite o nome 2: ")

a = []
t = ()

for i in range(len(n1))
    t = (n1[i],n2[i])
    a.append(t)
    
print a

-------------------------------------------------------------------------
SOLUÇAO 3:
    
def somar(x,y):
    return x+y
    
def ex2(n1,n2):
    print zip(n1,n2)

        
print somar(3,4)
nome1 = raw_input("Digite um nome: ")
nome2 = raw_input("Digite outro nome: ")
ex2(nome1,nome2)

// zip: retorna array de tuplas

'''