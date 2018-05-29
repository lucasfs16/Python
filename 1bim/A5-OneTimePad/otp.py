def otp(k,m):
    z=zip(k,m) # zip = Make an iterator that aggregates elements from each of the iterables.
        #Returns an iterator of tuples. Ex.: k1 e m1, k2 e m2,...
    aux = ""
    for (key,msg) in z:
        xr = ord(key) ^ ord(msg)
        aux = aux + chr(xr) # chr() Return the string representing a character whose Unicode code point is the integer i. 
        #For example, chr(97) returns the string 'a', while chr(8364) returns the string '€'. This is the inverse of ord().
    return aux.encode("hex")

print otp("!@ABB","FATEC")

# resp (cifra em hex): 6701150701
