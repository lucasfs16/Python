
# def é função - elas nao tem retorno

def somar(x,y):
    return x+y

#solução do exerc-tupla-nome.py com verificação do tamanho dos nomes:    
def ex2(n1,n2):
    if len(n1) == len(n2):
        aux = []
        for i in range(len(n1)):
            aux.append((n1[i],n2[i]))
        
        print aux
    else:
        print "ERRO"
        

print somar(3,4)
nome1 = raw_input("Digite um nome: ")
nome2 = raw_input("Digite outro nome: ")
ex2(nome1,nome2)

