#mostrar e inserir elemento:

def dicionario():
    d = {} #dicionario vazio
    d["ALGO"] = 7
    d[9] = 7.5
    d[7.5] = True
    d[True] = 'W'
    d[(2,3,4,"Q")] = [3,4,5]
    d[1] = [7,8.1,"iSOSIOS"]
    obj = {"nome":"alguem","idade":19}
    print d
    print obj

#nao pode ter array como indice do dicionario 

dicionario() 
#resultado: {7.5: True, 9: 7.5, 'ALGO': 7, (2, 3, 4, 'Q'): [3, 4, 5], True: [7, 8.1, 'iSOSIOS']}
#{'idade': 19, 'nome': 'alguem'}

''' 
#outro dic:

def dicionario(dic):
    for i in dic:
        print str(i) + " -> " + str(dic[i])


dicionario({"indice":"valor",
            7:"Algo",
            True:3,
            1.1:(3,4)
           })

''' 