
#para rodar programa: digita no bash [abaixo]: python nomedoarquivo.py 
# ou só clicar em "Run"
#python é bom para trabalhar com JSON

#vetor vazio:
v = []

#atribuir valor 
v.append(7);
v.append('A');
v.append(True);
v.append([8,7,3]);
v.append([]);


#intera nos elementos
#for para usar na busca de elementos
for e in v:
    print e;

# resultado do for de cima [7,'A', True, [8,7,3], []]

#for paracido com o do usado no JS:
#nesse caso o i q varia
# for para buscar pelo indice
for i in range(len(v)):
    print v[i];
    
#range - cria vetor
#range(len(v)) = 5
#range(5) = [0,1,2,3,4]

#percorrer vetor sem atingir indice
for i in range(len(v)):
    print str(i) + " -> " + str(v[i])





