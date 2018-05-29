def calcularMedias():
    arq = open("alunos.dat","r")
    arq2 = open("saida.dat","w")
    linhas = arq.readlines()
    aux = ""
    for l in linhas:
        semBarraN = l.rstrip() #elimina o \n
        dados = semBarraN.split(',') # ['Vitor', '6', '7']
        media = (float(dados[1]) + float(dados[2]))/2
        
        if media >= 6:
            aux = aux + dados[0] + " : " + str(media) + " PASSOU \n"
        else:
            aux = aux + dados[0] + " : " + str(media) + " P3 \n"

    arq2.write(aux)
    arq.close()
    arq2.close()
        
calcularMedias()