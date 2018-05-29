#ler o arquivo e passar o nome dos alunos 
#com as medias para ver se passou ou nao

def calcularMedias():
    arq = open("alunos.dat", "r") #r = read
    arq2 = open("saida.dat", "w")  #w = write --> para cuspir os dados para o arq2
    linhas = arq.redlines()
    aux = ""
    
    #arq1:
    for l in linhas:
        semBarraN = l.rstrip() #ou print l.split("\n")[0] para tirar \n
        dados = semBarraN.split(',') # ['Vitor', '6', '7']
        media = (float(dados[1]) + float(dados[2]))/2
 
    #arq2:
    if media >= 6:
            aux = aux + dados[0] + " : " + str(media) + " PASSOU \n"
    else:
            aux = aux + dados[0] + " : " + str(media) + " P3 \n"

    arq2.write(aux)
    arq.close()
    arq2.close()    
        
        
        
calcularMedias()
    
    