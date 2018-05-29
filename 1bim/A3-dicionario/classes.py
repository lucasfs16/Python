#POO:

class Contador:
    qtPessoas = 0
    
    #construtor no py:
    def __init__(self,qtPessoas):
        self.qtPessoas = qtPessoas
     
    #metodo:
    def incrementar(self): #self = this
        self.qtPessoas = self.qtPessoas + 1
        
    def decrementar(self):
        self.qtPessoas = self.qtPessoas - 1
        
    def resetar(self):
        self.qtPessoas = 0
        
    def mostrar(self):
        print self.qtPessoas
 
    
k = Contador(4) #retorna 5
k.incrementar()
k.incrementar()
k.decrementar()
k.mostrar()    
    
    
    
    