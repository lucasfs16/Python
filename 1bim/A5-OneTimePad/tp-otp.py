'''
c1=3d5a10187b1b544e634342544361184f43525d5f1647580d0b5a195840595b0c4c110602110f5202175b46
c2=3b6134184106541017445a5c01540b0b175b54570b4c110d0c175c5f500b4c134c1e1102110859174d
c3=3d5a101871005d06450a5b5e17581c451713574d175645100c591958405940105d55550e1c5a7234785b465b
c4=247640185d06110d585e0f500d111c45004148480d5c5e17435655565c0b5c17505c5446535a01
c5=3a7a341505555810174b0f7c06431247061e75591452500b07175a434a09410c5f4314171a13434751141b1d101e120604441c081b
c6=2d5d55565b01110b5659471114580d43437e750d
c7=281206505b0745435a4f5c4202561c
c8=285e1857470111175f4f5d544d112d43064154181847545950175454400a54045d42550b171c5449
c9=3a623b184701500d440a495e11112a5e014045510d4045100c591461560b58164c50010e1d1400295c011f1a42131446
c10=3d5a1018703062435646485e11580d430e13584b5957500a065319585d5954437e541c14061f4c4777101c025f0a0c46
c11=2a5d1b5f46144510160a765e1611114a1556115a0b5a5a1c0d175448131a5a075d1f

# outras cifras:
c1 = "253a077715010b5e30011f68265302553f1f100d5f01511c50750e255d70003115432c04566c291c1c3646490c061a681d3054022524510c2b1f15144f0e00206b3b160a413f".decode("hex")
#print 'Decoded C1 :', c1

c2 = "283d17770a011b4575435b786b42090735095e17101a1754413d1c6d4138072415432103466c2a16192718491a12052d5b".decode("hex")
#print 'Decoded C2 :', c2

c3 = "392b1238041a01452c4d4b06241e4c1c224b43435e1a05581521112840354831140678025c6c231c00264a061c530b3e1c3955".decode("hex")
#print 'Decoded C3 :', c3

c4 = "3f37143215480d58360012383f121b1c2204100c5e105c005c381c6d42310c70110a2c0413382c164f310b040b53052d0c7b".decode("hex")
#print 'Decoded C4 :', c4

c5 = "283d17770f091e53751119292859091176014943531a15111b7530391523482309432b0d576d".decode("hex")
#print  'Decoded C4 :', c5

c6 = "253a07771001065830004b272d125e45675810145f071d1015360c3d1227013c0a433a09130d36140a2c1e0000124f".decode("hex")
#print 'Decoded C6 :', c6
'''





c1 = "3d5a10187b1b544e634342544361184f43525d5f1647580d0b5a195840595b0c4c110602110f5202175b46".decode("hex")
#print 'Decoded C1 :', c1

c2 = "3b6134184106541017445a5c01540b0b175b54570b4c110d0c175c5f500b4c134c1e1102110859174d".decode("hex")
#print 'Decoded C2 :', c2

c3 = "3d5a101871005d06450a5b5e17581c451713574d175645100c591958405940105d55550e1c5a7234785b465b".decode("hex")
#print 'Decoded C3 :', c3

c4 = "247640185d06110d585e0f500d111c45004148480d5c5e17435655565c0b5c17505c5446535a01".decode("hex")
#print 'Decoded C4 :', c4

c5 = "3a7a341505555810174b0f7c06431247061e75591452500b07175a434a09410c5f4314171a13434751141b1d101e120604441c081b".decode("hex")
#print  'Decoded C4 :', c5

c6 = "2d5d55565b01110b5659471114580d43437e750d".decode("hex")
#print 'Decoded C6 :', c6


c11 ="%:w_QPu%]p1C,Vl)6FI&SU?h0T%$Q+Ok;A?"

c22 ="(=wuC[xkB5^TA=mA8$C!Fl*'I-["

c33="9+8E,MK$L'KCC^X!(@5H1x\l#&JS>9U"    #9+8E,MK$L"KCC^X!(@5H1x\l#&JS

c44= "X68??72H\\8mB1p,8,O1S-{"           #X68?\\8mB1p,8,O1S-{ 
#X68?ded C4 : ?72H\\8mB1p,8,O1S-{

c55="(=wSu)(YvICS09#H#C+"                #WmcodedC5:(=wSu)(YvICS09#H#C+
#WmwSu)(YvICS09#H#C+

c66="%:wX0K'-^EgX_6='<6:,O"


def otp (k,m,m2):
    z = zip(k,m,m2)
    aux = ""
    for (key,msg,msg2) in z:
        xr = ord(key) ^ ord(msg) ^ ord(msg2)
        aux = aux+chr(xr)
    return aux #aux = ^OQ-<4ssr"&Crpkf1`[4`kq~%n o-#!om62xbi

#print otp("(=wuC[xkB5^TA=mA8$C!Fl*'I-[", "X68?ded:?72H\\8mB1p,8,O1S-{","pOJ'>Q}lToj#dV")

print otp(c3, c5,"You Have cracked my code. It's so sad .")
#msg = HypoCrisy? No, it's not, there are no!