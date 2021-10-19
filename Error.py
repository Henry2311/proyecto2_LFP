class error:
    def __init__(self, caracter, tipo, linea, columna):
        self.caracter = caracter
        self.tipo = tipo
        self.linea = linea
        self.columna = columna

    def Rerror(self):
        contenido=''
        contenido+='<td  style="color: red; font-size: 1.2rem;">'+self.caracter+'</td>\n'
        contenido+='<td  style="color: red; font-size: 1.2rem;">'+self.tipo+'</td>\n'
        contenido+='<td  style="color: red; font-size: 1.2rem;">'+str(self.linea)+'</td>\n'
        contenido+='<td  style="color: red; font-size: 1.2rem;">'+str(self.columna)+'</td>\n'
        return contenido