from claves import claves

clvs = []
regs = []
consola = ''

class expresion:
    def __init__(self, tipo, valor) :
        self.tipo = tipo
        self.valor = valor

    def getValor(self, entorno):
        return self.valor

class IntruccionPromedio() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        global clvs
        global consola
        valor = self.expresion.getValor(entorno)
        
        promedio=0
        for i in range(len(clvs)):
            if clvs[i].id == valor:
                for j in range(len(clvs[i].valores)):
                    promedio+=float(clvs[i].valores[j])
                
                promedio=round(promedio/len(clvs[i].valores),2)
        
        print(str(promedio))
        consola+='\n'+str(promedio)+'\n'      

class IntruccionContarsi() :
    def __init__(self, expresion,indice) :
        self.expresion = expresion
        self.indice = indice

    def ejecutar(self, entorno):
        global clvs
        global consola
        valor = self.expresion.getValor(entorno)
        contar=''
        for i in range(len(clvs)):
            if clvs[i].id == valor:
                contar+=clvs[i].valores[self.indice]
                break

        print(contar)
        consola+='\n'+str(contar)+'\n'

class IntruccionDatos() :
    def __init__(self) :
        self.expresion = expresion('entero',0)

    def ejecutar(self, entorno):
        global consola
        valor = self.expresion.getValor(entorno)
        tabla = self.tabla_datos()
        print(tabla)
        consola+='\n'+tabla+'\n'

    def tabla_datos(self):
        global clvs
        global regs
        tabla=''

        for c in clvs:
            tabla+="{:<25}"
            tabla = tabla.format(c.id)    
        
        tabla+='\n'
        tabla+='-'*len(tabla)+'\n'
        aux=len(clvs)
        i=0
        for r in regs:
            tabla+="{:<25}"
            tabla = tabla.format(r)
            i+=1
            if i==aux:
                tabla+='\n'
                i=0
        
        return tabla

class IntruccionSumar() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        global clvs
        global consola
        valor = self.expresion.getValor(entorno)
        
        suma=0
        for i in range(len(clvs)):
            if clvs[i].id == valor:
                for j in range(len(clvs[i].valores)):
                    suma+=float(clvs[i].valores[j])
        
        print(str(suma)) 
        consola+='\n'+str(suma)+'\n' 

class IntruccionMax() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        global clvs
        global consola
        valor = self.expresion.getValor(entorno)
        
        max=0
        for i in range(len(clvs)):
            if clvs[i].id == valor:
                max=sorted(clvs[i].valores,reverse=True)
        
        print(str(max[0]))
        consola+='\n'+str(max[0])+'\n'  

class IntruccionMin() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        global clvs
        global consola
        valor = self.expresion.getValor(entorno)
        
        min=0
        for i in range(len(clvs)):
            if clvs[i].id == valor:
                min=sorted(clvs[i].valores)
        
        print(str(min[0]))
        consola+='\n'+str(min[0])+'\n'

class IntruccionReporte() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        global clvs
        global regs
        global consola
        valor = self.expresion.getValor(entorno)
        self.html(valor,clvs,regs)
        print('Reporte Generado')
        consola+='\nReporte Generado\n'

    def html(self,name,claves,registros):
        file = open(name+'.html','w')
        content='''
                    <!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                <link rel="stylesheet" href="style2.css">
                                <title>Reporte</title>
                            </head>
                            <body>
                            <div class="container-table">
                            <div class="table__title1">
                                {}
                            </div></div>
        '''
        content = content.format(name)

        content += ''' <div id="main-container">
                            <table>
                            <thead>
                            <tr>'''

        for c in claves:
            if claves.index(c) == 0:
                content+='<th style="border-top-left-radius: 20px;">'+c.id+'</th>'
            elif claves.index(c) == len(claves)-1:
                content+='<th style="border-top-right-radius: 20px;">'+c.id+'</th>'
            else:
                content+='<th>'+c.id+'</th>'
        content+='''
                    </tr>
                    </thead>
                    '''

        aux=len(claves)-1
        i=0
        for r in registros:
            if i==0:
                content+='<tr>'
                content+='<td>'+r+'</td>'
                i+=1
            elif i==aux:
                content+='<td>'+r+'</td>'  
                content+='</tr>'
                i=0
            else:
                content+='<td>'+r+'</td>'
                i+=1

        content+='</table>'
        content+="</div>\n"
        content+='</body>\n</html>'
        file.write(content)
        file.close()

class IntruccionConteo() :
    def __init__(self) :
        self.expresion = expresion('entero',0)

    def ejecutar(self, entorno):
        global regs
        global consola
        valor = self.expresion.getValor(entorno)+len(regs)
        print(valor)
        consola+='\n'+str(valor)+'\n'

class IntruccionClaves() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        global clvs
        valor = self.expresion.ejecutar(entorno)
        
        print(valor)
        print('-----------------------')
        for c in clvs:
            print(c.id)

class ListaClaves2() :
    def __init__(self, expresion, lista) :
        self.expresion = expresion
        self.lista = lista

    def ejecutar(self, entorno):
        global clvs
        if self.expresion:
            #print(self.expresion.getValor(entorno),'xx')
            clvs.append(claves(self.expresion.getValor(entorno)))
            if self.lista:
                self.lista.ejecutar(entorno)

class ListaClaves() :
    def __init__(self, expresion, lista) :
        self.expresion = expresion
        self.lista = lista

    def ejecutar(self, entorno):
        global clvs
        if self.expresion:
            #print(self.expresion.getValor(entorno),'x')
            clvs.append(claves(self.expresion.getValor(entorno)))
            if self.lista:
                self.lista.ejecutar(entorno)

class ListaValReg2() :
    def __init__(self, expresion, lista) :
        self.expresion = expresion
        self.lista = lista

    def ejecutar(self, entorno):
        global regs
        if self.expresion:
            print(self.expresion.getValor(entorno),'xx')
            regs.append(self.expresion.getValor(entorno))
            if self.lista:
                self.lista.ejecutar(entorno)

class ListaValReg() :
    def __init__(self, expresion, lista) :
        self.expresion = expresion
        self.lista = lista

    def ejecutar(self, entorno):
        global regs
        if self.expresion:
            print(self.expresion.getValor(entorno),'x')
            regs.append(self.expresion.getValor(entorno))
            if self.lista:
                self.lista.ejecutar(entorno)

class ListaRegistros2() :
    def __init__(self, expresion, lista) :
        self.expresion = expresion
        self.lista = lista

    def ejecutar(self, entorno):
        global clvs
        if self.expresion:
            self.expresion.ejecutar(entorno)
            #clvs.append(claves(self.expresion.getValor(entorno)))
            if self.lista:
                self.lista.ejecutar(entorno)

class ListaRegistros() :
    def __init__(self, expresion, lista) :
        self.expresion = expresion
        self.lista = lista

    def ejecutar(self, entorno):
        global clvs
        if self.expresion:
            self.expresion.ejecutar(entorno)
            #clvs.append(claves(self.expresion.getValor(entorno)))
            if self.lista:
                self.lista.ejecutar(entorno)

class IntruccionRegistros() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        global clvs
        global regs
        valor = self.expresion.ejecutar(entorno)

        
        clvs = self.datos(clvs,regs)

        for c in clvs:
            c.getValores()

    def datos(self, claves, registros):
        c = len(claves) #5
        r = len(registros) #20
        
        for i in range(c):
            aux=r/c 
            n=i
            for j in range(r):
                if aux>0:
                    claves[i].valores.append(registros[j+n])
                    n+=(c-1)
                    aux-=1
        return claves

class IntruccionImprimirln() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        global consola
        valor = self.expresion.getValor(entorno)
        print(valor)
        consola+=str(valor)+'\n'

class IntruccionImprimir() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        global consola
        valor = self.expresion.getValor(entorno)
        print(valor, end=' ')
        consola+=str(valor)

class Instruccion() :
    def __init__(self, instruccion) :
        self.instruccion = instruccion

    def ejecutar(self, entorno):
        self.instruccion.ejecutar(entorno)

class ListaInstrucciones2() :
    def __init__(self, instruccion, lista) :
        self.instruccion = instruccion
        self.lista = lista

    def ejecutar(self, entorno):
        if self.instruccion:
            self.instruccion.ejecutar(entorno)
            if self.lista:
                self.lista.ejecutar(entorno)

class ListaInstrucciones() :
    def __init__(self, instruccion, lista) :
        self.instruccion = instruccion
        self.lista = lista

    def ejecutar(self, entorno):
        if self.instruccion:
            self.instruccion.ejecutar(entorno)
            if self.lista:
                self.lista.ejecutar(entorno)

class Inicio() :
    def __init__(self,lista) :
        self.lista = lista

    def ejecutar(self, entorno):
        self.lista.ejecutar(entorno)