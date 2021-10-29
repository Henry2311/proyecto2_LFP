from os import startfile
from claves import claves
from graphviz import Graph
clvs = []
regs = []
consola = ''

dot = Graph('arbol', 'png')
dot.format = 'pdf'
dot.attr(splines = 'false')
dot.node_attr.update(shape = 'circle')
dot.edge_attr.update(color = 'black')
i = 0
def start():
    global i
    i += 1
    return i

class expresion:
    def __init__(self, tipo, valor) :
        self.tipo = tipo
        self.valor = valor

    def getValor(self, entorno):
        return self.valor

    def getNodos(self):
        global dot
        idnodo = str(start())
        dot.node(idnodo, 'expresion')
        
        idlit = str(start())
        dot.node(idlit, 'literal')

        idexp = str(start())
        dot.node(idexp, self.valor)

        dot.edge(idlit, idexp)
        dot.edge(idnodo, idlit)

        return idnodo

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

    def getNodos(self):
        global dot
        idnodo = str(start())
        dot.node(idnodo, "INS_PROMEDIO")

        idclaves = str(start())
        dot.node(idclaves, "promedio")

        idparentesis = str(start())
        dot.node(idparentesis, "(")
        
        hijo = self.expresion.getNodos()

        idparentesisc = str(start())
        dot.node(idparentesisc, ")")

        idpuntocoma = str(start())
        dot.node(idpuntocoma, ";")        

        dot.edge(idnodo, idclaves)
        dot.edge(idnodo, idparentesis)
        dot.edge(idnodo,hijo)
        dot.edge(idnodo, idparentesisc)
        dot.edge(idnodo, idpuntocoma)

        return idnodo   

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

    def getNodos(self):
        global dot
        idnodo = str(start())
        dot.node(idnodo, "INS_CONTARSI")

        idclaves = str(start())
        dot.node(idclaves, "contarsi")

        idparentesis = str(start())
        dot.node(idparentesis, "(")
        
        hijo = self.expresion.getNodos()

        idcoma =str(start())
        dot.node(idcoma,",")

        idindice = str(start())
        dot.node(idindice,str(self.indice))

        idparentesisc = str(start())
        dot.node(idparentesisc, ")")

        idpuntocoma = str(start())
        dot.node(idpuntocoma, ";")        

        dot.edge(idnodo, idclaves)
        dot.edge(idnodo, idparentesis)
        dot.edge(idnodo,hijo)
        dot.edge(idnodo,idcoma)
        dot.edge(idnodo,idindice)
        dot.edge(idnodo, idparentesisc)
        dot.edge(idnodo, idpuntocoma)

        return idnodo

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

    def getNodos(self):
        global dot
        idnodo = str(start())
        dot.node(idnodo, "INS_DATOS")

        idclaves = str(start())
        dot.node(idclaves, "datos")

        idparentesis = str(start())
        dot.node(idparentesis, "(")
        
        idparentesisc = str(start())
        dot.node(idparentesisc, ")")

        idpuntocoma = str(start())
        dot.node(idpuntocoma, ";")        

        dot.edge(idnodo, idclaves)
        dot.edge(idnodo, idparentesis)
        dot.edge(idnodo, idparentesisc)
        dot.edge(idnodo, idpuntocoma)

        return idnodo

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

    def getNodos(self):
        global dot
        idnodo = str(start())
        dot.node(idnodo, "INS_SUMAR")

        idclaves = str(start())
        dot.node(idclaves, "sumar")

        idparentesis = str(start())
        dot.node(idparentesis, "(")
        
        hijo = self.expresion.getNodos()

        idparentesisc = str(start())
        dot.node(idparentesisc, ")")

        idpuntocoma = str(start())
        dot.node(idpuntocoma, ";")        

        dot.edge(idnodo, idclaves)
        dot.edge(idnodo, idparentesis)
        dot.edge(idnodo,hijo)
        dot.edge(idnodo, idparentesisc)
        dot.edge(idnodo, idpuntocoma)

        return idnodo

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

    def getNodos(self):
        global dot
        idnodo = str(start())
        dot.node(idnodo, "INS_MAX")

        idclaves = str(start())
        dot.node(idclaves, "maximo")

        idparentesis = str(start())
        dot.node(idparentesis, "(")
        
        hijo = self.expresion.getNodos()

        idparentesisc = str(start())
        dot.node(idparentesisc, ")")

        idpuntocoma = str(start())
        dot.node(idpuntocoma, ";")        

        dot.edge(idnodo, idclaves)
        dot.edge(idnodo, idparentesis)
        dot.edge(idnodo,hijo)
        dot.edge(idnodo, idparentesisc)
        dot.edge(idnodo, idpuntocoma)

        return idnodo 

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

    def getNodos(self):
        global dot
        idnodo = str(start())
        dot.node(idnodo, "INS_MIN")

        idclaves = str(start())
        dot.node(idclaves, "minimo")

        idparentesis = str(start())
        dot.node(idparentesis, "(")
        
        hijo = self.expresion.getNodos()

        idparentesisc = str(start())
        dot.node(idparentesisc, ")")

        idpuntocoma = str(start())
        dot.node(idpuntocoma, ";")        

        dot.edge(idnodo, idclaves)
        dot.edge(idnodo, idparentesis)
        dot.edge(idnodo,hijo)
        dot.edge(idnodo, idparentesisc)
        dot.edge(idnodo, idpuntocoma)

        return idnodo

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
        startfile(name+'.html')

    def getNodos(self):
        global dot
        idnodo = str(start())
        dot.node(idnodo, "INS_REPORTE")

        idclaves = str(start())
        dot.node(idclaves, "reporte")

        idparentesis = str(start())
        dot.node(idparentesis, "(")
        
        hijo = self.expresion.getNodos()

        idparentesisc = str(start())
        dot.node(idparentesisc, ")")

        idpuntocoma = str(start())
        dot.node(idpuntocoma, ";")        

        dot.edge(idnodo, idclaves)
        dot.edge(idnodo, idparentesis)
        dot.edge(idnodo,hijo)
        dot.edge(idnodo, idparentesisc)
        dot.edge(idnodo, idpuntocoma)

        return idnodo

class IntruccionConteo() :
    def __init__(self) :
        self.expresion = expresion('entero',0)

    def ejecutar(self, entorno):
        global regs
        global consola
        valor = self.expresion.getValor(entorno)+len(regs)
        print(valor)
        consola+='\n'+str(valor)+'\n'

    def getNodos(self):
        global dot
        idnodo = str(start())
        dot.node(idnodo, "INS_CONTEO")

        idclaves = str(start())
        dot.node(idclaves, "conteo")

        idparentesis = str(start())
        dot.node(idparentesis, "(")
        
        idparentesisc = str(start())
        dot.node(idparentesisc, ")")

        idpuntocoma = str(start())
        dot.node(idpuntocoma, ";")        

        dot.edge(idnodo, idclaves)
        dot.edge(idnodo, idparentesis)
        dot.edge(idnodo, idparentesisc)
        dot.edge(idnodo, idpuntocoma)

        return idnodo

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
    
    def getNodos(self):
        global dot
        idnodo = str(start())
        dot.node(idnodo, "INS_CLAVES")

        idclaves = str(start())
        dot.node(idclaves, "Claves")

        idigual = str(start())
        dot.node(idigual, "=")
        
        idcorchetea = str(start())
        dot.node(idcorchetea, "[")

        hijo = self.expresion.getNodos()

        idcorchetec = str(start())
        dot.node(idcorchetec, "]")        

        dot.edge(idnodo, idclaves)
        dot.edge(idnodo, idcorchetea)
        dot.edge(idnodo, hijo)
        dot.edge(idnodo, idcorchetec)

        return idnodo

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

    def getNodos(self):
        global dot
        idnodo = str(start())
        dot.node(idnodo, "LISTA_CLAVES2")

        if self.expresion:
            ex = self.expresion.getNodos()

            coma=str(start())
            dot.node(coma,',')
    
            dot.edge(idnodo,ex)
            dot.edge(idnodo,coma)
            if self.lista:
                hijo = self.lista.getNodos()
                dot.edge(idnodo,hijo)

        return idnodo

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

    def getNodos(self):
        global dot
        idnodo = str(start())
        dot.node(idnodo, "LISTA_CLAVES")

        if self.expresion:
            ex = self.expresion.getNodos()

            coma=str(start())
            dot.node(coma,',')
    
            dot.edge(idnodo,ex)
            dot.edge(idnodo,coma)
            if self.lista:
                hijo = self.lista.getNodos()
                dot.edge(idnodo,hijo)

        return idnodo

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

    def getNodos(self):
        global dot
        idnodo = str(start())
        dot.node(idnodo, "LISTA_VAL_REG2")

        if self.expresion:
            ex = self.expresion.getNodos()

            coma=str(start())
            dot.node(coma,',')
    
            dot.edge(idnodo,ex)
            dot.edge(idnodo,coma)
            if self.lista:
                hijo = self.lista.getNodos()
                dot.edge(idnodo,hijo)

        return idnodo

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

    def getNodos(self):
        global dot
        idnodo = str(start())
        dot.node(idnodo, "LISTA_VAL_REG")

        if self.expresion:
            idllavea=str(start())
            dot.node(idllavea,'{')

            ex = self.expresion.getNodos()

            coma=str(start())
            dot.node(coma,',')
            
            dot.edge(idnodo,idllavea)
            dot.edge(idnodo,ex)
            dot.edge(idnodo,coma)
            if self.lista:
                hijo = self.lista.getNodos()
                dot.edge(idnodo,hijo)

        idllavec=str(start())
        dot.node(idllavec,'}')
        dot.edge(idnodo,idllavec)
        return idnodo

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

    def getNodos(self):
        global dot
        idnodo = str(start())
        dot.node(idnodo, "LISTA_REGISTROS2")

        if self.expresion:
            val_reg=self.expresion.getNodos()
            dot.edge(idnodo,val_reg)

            if self.lista:
                hijo = self.lista.getNodos()
                dot.edge(idnodo,hijo)

        return idnodo

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

    def getNodos(self):
        global dot
        idnodo = str(start())
        dot.node(idnodo, "LISTA_REGISTROS")

        if self.expresion:
            val_reg=self.expresion.getNodos()
            dot.edge(idnodo,val_reg)

            if self.lista:
                hijo = self.lista.getNodos()
                dot.edge(idnodo,hijo)

        return idnodo
    
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

    def getNodos(self):
        global dot
        idnodo = str(start())
        dot.node(idnodo, "INS_REGISTROS")

        idreg = str(start())
        dot.node(idreg, "registros")

        idigual = str(start())
        dot.node(idigual, "=")

        idcorchetea = str(start())
        dot.node(idcorchetea, "[")

        hijo = self.expresion.getNodos()

        idcorchetec = str(start())
        dot.node(idcorchetec, "]")     

        dot.edge(idnodo, idreg)
        dot.edge(idnodo, idcorchetea)
        dot.edge(idnodo, hijo)
        dot.edge(idnodo, idcorchetec)

        return idnodo

class IntruccionImprimirln() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        global consola
        valor = self.expresion.getValor(entorno)
        print(valor)
        consola+=str(valor)+'\n'
    
    def getNodos(self):
        global dot
        idnodo = str(start())
        dot.node(idnodo, "INS_IMPRIMIRLN")

        idconsole = str(start())
        dot.node(idconsole, "imprimirln")

        idpara = str(start())
        dot.node(idpara, "(")

        hijo = self.expresion.getNodos()

        idparc = str(start())
        dot.node(idparc, ")")

        idpuntocoma = str(start())
        dot.node(idpuntocoma, ";")        

        dot.edge(idnodo, idconsole)
        dot.edge(idnodo, idpara)
        dot.edge(idnodo, hijo)
        dot.edge(idnodo, idparc)
        dot.edge(idnodo, idpuntocoma)
        return idnodo

class IntruccionImprimir() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        global consola
        valor = self.expresion.getValor(entorno)
        print(valor, end=' ')
        consola+=str(valor)

    def getNodos(self):
        global dot
        idnodo = str(start())
        dot.node(idnodo, "INS_IMPRIMIR")

        idconsole = str(start())
        dot.node(idconsole, "imprimir")

        idpara = str(start())
        dot.node(idpara, "(")

        hijo = self.expresion.getNodos()

        idparc = str(start())
        dot.node(idparc, ")")

        idpuntocoma = str(start())
        dot.node(idpuntocoma, ";")        

        dot.edge(idnodo, idconsole)
        dot.edge(idnodo, idpara)
        dot.edge(idnodo, hijo)
        dot.edge(idnodo, idparc)
        dot.edge(idnodo, idpuntocoma)
        return idnodo

class Instruccion() :
    def __init__(self, instruccion) :
        self.instruccion = instruccion

    def ejecutar(self, entorno):
        self.instruccion.ejecutar(entorno)

    def getNodos(self):
        global dot
        idnodo = str(start())
        dot.node(idnodo, "INSTRUCCION")

        hijo = self.instruccion.getNodos()

        dot.edge(idnodo, hijo)
        return idnodo

class ListaInstrucciones2() :
    def __init__(self, instruccion, lista) :
        self.instruccion = instruccion
        self.lista = lista

    def ejecutar(self, entorno):
        if self.instruccion:
            self.instruccion.ejecutar(entorno)
            if self.lista:
                self.lista.ejecutar(entorno)

    def getNodos(self):
        global dot
        idnodo = str(start())
        dot.node(idnodo, "LISTA_INSTRUCCIONES2")
        if self.instruccion:
            hijo = self.instruccion.getNodos()
            dot.edge(idnodo, hijo)
            if self.lista:
                hijo2 = self.lista.getNodos()
                dot.edge(idnodo, hijo2)
        return idnodo

class ListaInstrucciones() :
    def __init__(self, instruccion, lista) :
        self.instruccion = instruccion
        self.lista = lista

    def ejecutar(self, entorno):
        if self.instruccion:
            self.instruccion.ejecutar(entorno)
            if self.lista:
                self.lista.ejecutar(entorno)

    def getNodos(self):
        global dot
        idnodo = str(start())
        dot.node(idnodo, "LISTA_INSTRUCCIONES")
        if self.instruccion:
            hijo = self.instruccion.getNodos()
            dot.edge(idnodo, hijo)
            if self.lista:
                hijo2 = self.lista.getNodos()
                dot.edge(idnodo, hijo2)
        return idnodo

class InstruccionEOF():
    def __init__(self):
        pass

    def ejecutar(self, entorno):
        pass

    def getNodos(self):
        global dot

        idnodo = str(start())
        dot.node(idnodo, '$')

        return idnodo

class Inicio() :
    def __init__(self,lista) :
        self.lista = lista

    def ejecutar(self, entorno):
        self.lista.ejecutar(entorno)
    
    def getNodos(self):
        global dot
        idnodo = str(start())
        dot.node(idnodo,'INICIO')
        hijo = self.lista.getNodos()
        dot.edge(idnodo, hijo)
        dot.render()
        return idnodo