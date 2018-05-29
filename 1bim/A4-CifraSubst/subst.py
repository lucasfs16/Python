# Encriptacao E(k,m)
# m -> String
# k [chave] -> dicionario (ou funcao, mas é mais dificil usando funcao)

#dicionario é uma função que varia, a função é mais fixa

def encriptar(k,m):
    # TEXTO CIFRADO
    aux = ""
    for letra in m:
        aux = aux + k[letra] #k[letra]: olha na tabela para substituir
    return aux
    
    def montarDicionario(gama1,gama2):
        if len(gama1) != len(gama2):
            return {}
        else:
            dic = {}
            z = zip(gama1,gama2) #zip PEGA UM ARRAY DE TUPLAS E PEGA O PRIMEIRO COM PRIMEIRO, SEGUNDO COM SEGUNDO,...
            for (x,y) in z:
                dic[x] = y
            return dic
            
chave = montarDicionario(" ABCDEFGHIJKLMNOPQRSTUVWYZ",  
                         "DP JSQBTKCIYHOVARZULENGXWMF")
                         
print encriptar(chave, "JAVA")
print encriptar(chave, "OLA MUNDO")
print encriptar(chave, "PHP")
print encriptar(chave, "PYTHON")



