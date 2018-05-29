

c1 = "3d5a10187b1b544e634342544361184f43525d5f1647580d0b5a195840595b0c4c110602110f5202175b46".decode("hex")
##print 'Decoded1 :', c1
c2 = "3b6134184106541017445a5c01540b0b175b54570b4c110d0c175c5f500b4c134c1e1102110859174d".decode("hex")
##print 'Decoded2 :', c2
c3 = "3d5a101871005d06450a5b5e17581c451713574d175645100c591958405940105d55550e1c5a7234785b465b".decode("hex")
##print 'Decoded3 :', c3
c4 = "247640185d06110d585e0f500d111c45004148480d5c5e17435655565c0b5c17505c5446535a01".decode("hex")
##print 'Decoded4 :', c4
c5 = "3a7a341505555810174b0f7c06431247061e75591452500b07175a434a09410c5f4314171a13434751141b1d101e120604441c081b".decode("hex")
##print 'Decoded 5:', c5
c6 = "2d5d55565b01110b5659471114580d43437e750d".decode("hex")
##print 'Decoded6 :', c6
c7 = "281206505b0745435a4f5c4202561c".decode("hex")
##print 'Decoded7 :', c7
c8 = "285e1857470111175f4f5d544d112d43064154181847545950175454400a54045d42550b171c5449".decode("hex")
##print 'Decoded8 :', c8
c9= "3a623b184701500d440a495e11112a5e014045510d4045100c591461560b58164c50010e1d1400295c011f1a42131446".decode("hex")
##print 'Decoded 9:', c9
c10="3d5a1018703062435646485e11580d430e13584b5957500a065319585d5954437e541c14061f4c4777101c025f0a0c46".decode("hex")
##print 'Decoded 10:', c10
c11="2a5d1b5f46144510160a765e1611114a1556115a0b5a5a1c0d175448131a5a075d1f".decode("hex")
##print 'Decoded11 :', c11

def otp (k,m,m2):
    z = zip(k,m,m2)
    aux = ""
    for (key,msg,msg2) in z:
        xr = ord(key) ^ ord(msg) ^ ord(msg2)
        aux = aux+chr(xr)
    return aux

    #print otp(c5, c3,"THE") = Sha
#print otp(c5, c3,"Shall") = THEa
#print otp(c5, c3,"Shadow") = THEi
#print otp(c5, c3,"Sha ") = THE-
    #print otp(c5, c3,"Sha") = THE
    #print otp(c5, c3,"Share") = THE
    
#print otp(c5, c3,"Share ") = THEu
#print otp(c5, c3,"Share the") = THEuq~7
#print otp(c5, c3,"Share it") = THEulb
#print otp(c5, c3,"Share that") = THEuq~35
#print otp(c5, c3,"that") = sHEy
#print otp(c5, c3,"That") = SHEy
#print otp(c5, c3,"That ") = SHEyT
#print otp(c5, c3,"and") = fN@
#print otp(c5, c3,"or") = hR
#print otp(c5, c3,"show") = tHKz

#print otp(c5, c3,"THE BOOK") = Sha-6J]
#print otp(c5, c3,"THE HOUSE") = Sha-<PE
#print otp(c5, c3,"THE CODE") = Sha-7AS
#print otp(c5, c3,"you") = ~OQ
#print otp(c5, c3,"YOU") = ^oq
#print otp(c5, c3,"You") = ^OQ
#print otp(c5, c3,"THE CAR") = Sha-7W
#print otp(c5, c3,"AND") = Fn`
#print otp(c5, c3,"THE ") = Sha-
#print otp(c5, c3,"THERE") = Sha_1
    #print otp(c5, c3,"Tha") = SHE
#print otp(c5, c3,"SHE IS") = Tha-=
#print otp(c5, c3,"SHEET") = ThaH
#print otp(c5, c3,"SHELF") = ThaA2
#print otp(c5, c3,"SHELTER") = ThaA W
#print otp(c5, c3,"SHE HAS") = Tha-<V
#print otp(c5, c3,"SHE WAS") = Tha-#V
#c10 e c3 =
    #print otp(c10, c3,"Sha") = Sha
#print otp(c10, c3,"Share") = Shard
#print otp(c10, c3,"Share the") = ShardK-v
#print otp(c10, c3,"Sharp") = Sharq
#print otp(c10, c3,"Shark") = Sharj
#print otp(c10, c3,"Share ") = Shard
#para confirmar:
    #print otp(c1, c3,"Sha") = Sha
#print otp(c10, c9,"Sha") = TPJ
#print otp(c9, c10,"Sha") = TPJ
#print otp(c9, c10,"The") = SPN
#print otp(c9, c10,"the") = sPN
#print otp(c9, c10,"and") = fVO
#print otp(c9, c10,"for") = aWY

#print otp(c3, c6,"THERE") = DOo

    #print otp(c3, c6,"THER") = DO

#para confirmar :
    #print otp(c10, c3,"THEY") =THEY
    
    #print otp(c11, c3,"THEY") = CON
    
#print otp(c10, c3,"CONGRATULATIONS") = GIINBqk_

#para confirmar:
#print otp(c10, c3,"CONG") = CONG
 

#print otp(c1, c2,"THE") = Rsa
    #print otp(c1, c2,"R") = T
    
    #print otp(c1, c3,"THE") = THE
    
#print otp(c11, c1,"The One-Time-Pad") = Congrats! Yox ha

#print otp(c11, c1,"Congrats! You have ")



#key = Congrats! You have broken my code.
#c11 = The One-Time Pad algorithm is not secure
#c2 = RSA uses number theory to encrypt/...
# c3 = The Euler totient function is used...
# c4 =
#c5 = 
#c6
#c7
#c8 = 
#c9 = SPN stans for Substitution-Permuta
#c10 = The DES algorithm is based in a Fe
#c11
#print otp(c5, c1,"SHA-1 is a Merkle-Damgard cryptographic ")

#transforma a chave em hexadecimal [para testar no decodificador]:
#c0="i2u84u1c7*/1c1y+c318y51yc7913y5c81ugrz g9uhu0xghg0ugu".encode("hex")
#print c0
#chave em hexadecimal = 6932753834753163372a2f316331792b6333313879353179633739313379356338317567727a206739756875307867686730756775

#TESTE NO OTP DECODER [USANDO UMA CIFRA E A CHAVE EM HEXA]: https://www.mobilefish.com/services/one_time_pad/one_time_pad.php#one_time_pad_output
    #cifra c5 = 3a7a341505555810174b0f7c06431247061e75591452500b07175a434a09410c5f4314171a13434751141b1d101e120604441c081b
    #chave em hexa = 6932753834753163372a2f316331792b6333313879353179633739313379356338317567727a206739756875307867686730756775



    