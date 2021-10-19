class token:
    def __init__(self, lexema, tipo,  linea, columna):
        self.lexema = lexema
        self.tipo = tipo
        self.columna = columna 
        self.linea = linea 
        
        if self.tipo == 'claves' or self.tipo == 'registros' or self.tipo == 'imprimir' or self.tipo == 'imprimirln' or self.tipo == 'conteo' or self.tipo == 'promedio' or self.tipo == 'contarsi' or self.tipo == 'datos' or self.tipo == 'sumar' or self.tipo == 'maximo' or self.tipo == 'minimo' or self.tipo == 'reporte':
            self.color = '#002DFF' #azul
        elif self.tipo == 'llavea' or self.tipo == 'llavec' or self.tipo == 'corchetea' or self.tipo == 'corchetec' or self.tipo == 'parentesisa' or self.tipo == 'parentesisc' or self.tipo == 'puntocoma' or self.tipo == 'coma' or self.tipo == 'igual':
            self.color = '#8AD8E0' #turquesa
        elif self.tipo == 'cadena' or self.tipo =='EOF':
            self.color = '#00FF03' #verde
        elif self.tipo == 'entero' or self.tipo == 'decimal':
            self.color = '#F8FF00' #amarillo
        elif self.tipo == 'error':
            self.color = '#FF0000' #rojo

    def Rtokens(self):
        contenido=''
        contenido+="<td  style=\"color:"+self.color+'">'+self.lexema+"</td>\n"
        contenido+="<td  style=\"color:"+self.color+'">'+self.tipo+"</td>\n"
        contenido+="<td  style=\"color:"+self.color+'">'+str(self.linea)+"</td>\n"
        contenido+="<td  style=\"color:"+self.color+'">'+str(self.columna)+"</td>\n"
        return contenido