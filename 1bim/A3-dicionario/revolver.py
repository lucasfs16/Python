'''

Um revolver possui uma quantidade máxima de
munição. Ele pode atirar, uma bala por vez, ou
recarregar, uma por vez. Um revolver só atira
se houver munição e recarrega se a quantidade
de munição não for a máxima.
Implemente esta situação.

'''

class Revolver:
    qtMunic = 0
    qtMax = 0

    def __init__(self,qtMunic,qtMax):
        self.qtMunic = qtMunic
        self.qtMax = qtMax
        
    def atirar(self):
        if(self.qtMunic > 0):
            self.qtMunic = self.qtMunic - 1
            print "Munição: " + str(self.qtMunic)
        else:
            print "Recarregue!"
    
    def recarregar(self):
        if(self.qtMunic < self.qtMax):
            self.qtMunic = self.qtMunic + 1;
            print "Munição: " + str(self.qtMunic)
            else:
                print "Não é possível adicionar balas. Atire!"
    
    r = Revolver()
    
    r.qtMunic = 2
    
    r.qtMax = 5
    
    
    r.atirar()
    r.atirar()
    
    r.recarregar()
    
'''
#cod do prof:

class Revolver:
    qtMunicao = 0
    qtMaxima  = 0
    
    def __init__(self,qtMunicao,qtMaxima):
        self.qtMunicao = qtMunicao
        self.qtMaxima = qtMaxima
        
    def atirar(self):
        if self.qtMunicao > 0:
            self.qtMunicao = self.qtMunicao - 1
            print "Municao: " + str(self.qtMunicao)
        else:
            print "RECARREGUE"
    
    def recarregar(self):
        if self.qtMunicao < self.qtMaxima:
            self.qtMunicao = self.qtMunicao + 1
            print "Municao: " + str(self.qtMunicao)
        else:
            print "ATIRE!"
            
            

'''