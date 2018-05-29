#EXERCICIO: 11 cifras foram obtidas, todas elas encriptadas com a mesma chave usando o
# One-Time Pad. Decifre-as todas. A tabela usada foi a ASCII.
# OBS: Você deve converter de hexadecimal para String. As frases estão em inglês.

# SOLUÇÃO:
# 1) CONVERSÃO DAS CIFRAS [HEXADECIMAIS] EM STRINGS USANDO DECODE["HEX"]:
c1 = "3d5a10187b1b544e634342544361184f43525d5f1647580d0b5a195840595b0c4c110602110f5202175b46".decode("hex")

c2 = "3b6134184106541017445a5c01540b0b175b54570b4c110d0c175c5f500b4c134c1e1102110859174d".decode("hex")

c3 = "3d5a101871005d06450a5b5e17581c451713574d175645100c591958405940105d55550e1c5a7234785b465b".decode("hex")

c4 = "247640185d06110d585e0f500d111c45004148480d5c5e17435655565c0b5c17505c5446535a01".decode("hex")

c5 = "3a7a341505555810174b0f7c06431247061e75591452500b07175a434a09410c5f4314171a13434751141b1d101e120604441c081b".decode("hex")

c6 = "2d5d55565b01110b5659471114580d43437e750d".decode("hex")

c7 = "281206505b0745435a4f5c4202561c".decode("hex")

c8 = "285e1857470111175f4f5d544d112d43064154181847545950175454400a54045d42550b171c5449".decode("hex")

c9 = "3a623b184701500d440a495e11112a5e014045510d4045100c591461560b58164c50010e1d1400295c011f1a42131446".decode("hex")

c10 = "3d5a1018703062435646485e11580d430e13584b5957500a065319585d5954437e541c14061f4c4777101c025f0a0c46".decode("hex")

c11 = "2a5d1b5f46144510160a765e1611114a1556115a0b5a5a1c0d175448131a5a075d1f".decode("hex")

# 2) PEGAMOS AS STRINGS RESULTANTES DA CONVERSÃO E CALCULAMOS O XOR ENTRE DUAS CIFRAS E A CHAVE
    #sendo que c1 ^ c2 = m1^k ^ m2^k = m1 ^ m2
def descriptografar(k,m,m2):
    z = zip(k,m,m2)
    aux = ""
    for (key,msg,msg2) in z:
        xr = ord(key) ^ ord(msg) ^ ord(msg2)
        aux = aux+chr(xr) 
    return aux

# 3) CHUTAMOS CARACTERES ATÉ QUE RETORNESSEM PALAVRAS VÁLIDAS QUE CORRESPONDAM A UMA DAS MENSAGENS 
    #[tendo duas msgs como parametro mais o chute, retornando assim a outra msg]
    # ATÉ ENCONTRAR A MAIOR MSG [c5]
print descriptografar(c5, c10,"SHA-1 is a Merkle-Damgard cryptographic hash function") 
'''
palavras mais usadas:
the
of
to
and
a
in
is
it
you
that
he
was
for
on
are
with
as
I
his
they
'''
#print otp(c5, c3,"THE") = Sha
#print otp(c5, c3,"Share") = THE

#print otp(c1, c3,"THE") = THE

#print otp(c10, c3,"CONG") = CONG
#print otp(c10, c3,"CONGRATULATIONS") = GIINBqk_

#print otp(c11, c1,"The One-Time-Pad") = Congrats! Yox ha
  
# 4) USAMOS A MAIOR MSG(c5) PARA ENCONTRAR A CHAVE E DESCOBRIR AS OUTRAS MENSAGENS
    # USAMOS NA FORMULA APRENDIDA EM AULA PARA DESCOBRIR A CHAVE:
def otp(k,m):
    z = zip(k,m)
    aux = ""
    for (key,msg) in z:
        xr = ord(key) ^ ord(msg)
        aux = aux+chr(xr)
    return aux
# CHAVE ENCONTRADA = i2u84u1c7*/1c1y+c318y51yc7913y5c81ugrz g9uhu0xghg0ugu
print otp("i2u84u1c7*/1c1y+c318y51yc7913y5c81ugrz g9uhu0xghg0ugu", c10)

# 5) MENSAGENS [CIFRAS DESCRIPTOGRAFADAS USANDO A CHAVE ENCONTRADA]:
##c1=The One-Time Pad algorithm is not secure.
##c2=RSA uses number theory to encrypt/decrypt
##c3=The Euler totient function is used in RSA
##c4=MD5 is not an encryption algorithm!!! !
##c5=SHA-1 is a Merkle-Damgard cryptographic hash function
##c6=Do not hash with MD5
##c7=A short message
##c8=Almost there. There are 3 messages left.
##c9=SPN stans for Substitution-Permutation Networks.
##c10=The DES algorithm is based in a Feistel Networkself.
##c11=Congrats! You have broken my code.

'''
RECAPITULANDO:

1) CONVERSÃO DAS CIFRAS [HEXADECIMAIS] EM STRINGS USANDO DECODE["HEX"]
2) PEGAMOS AS STRINGS RESULTANTES DA CONVERSÃO E CALCULAMOS O XOR ENTRE DUAS CIFRAS E A CHAVE
3) CHUTAMOS CARACTERES ATÉ QUE RETORNASSEM PALAVRAS VÁLIDAS QUE CORRESPONDAM A UMA DAS MENSAGENS 
    [tendo duas msgs como parametro mais o chute, retornando assim a outra msg] - ATÉ ENCONTRAR A MAIOR MSG [c5]
4) USAMOS A MAIOR MSG(c5) PARA ENCONTRAR A CHAVE E DESCOBRIR AS OUTRAS MENSAGENS
5) MENSAGENS DECRIPTADAS [CIFRAS DESCRIPTOGRAFADAS USANDO A CHAVE ENCONTRADA]
  

'''  
