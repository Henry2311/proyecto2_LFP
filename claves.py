class claves:
    def __init__(self,id):
        self.id = id #nombre de la clave
        self.valores = [] #lista 

    def setValores(self,valor):
        self.valores.append(valor)

    def getValores(self):
        print('--------------')
        print(self.id)
        for v in self.valores:
            print('     ->'+v)
    
        