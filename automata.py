from arbol import *
from Token import token
from Error import error
import re

class analizador_lexico:
    def __init__(self):
        self.tokens = []
        self.errores = []

    def analizar(self,codigo):
        self.tokens = []
        self.errores = []

        linea = 1
        columna = 1
        buffer = ''
        centinel = '$'
        estado = 0
        codigo += centinel

        i = 0
        while i< len(codigo):
            c = codigo[i]
            
            if estado == 0:
                if c == '=':
                    buffer += c
                    self.tokens.append(token(buffer, 'igual', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '{':
                    buffer += c
                    self.tokens.append(token(buffer, 'llavea', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '}':
                    buffer += c
                    self.tokens.append(token(buffer, 'llavec', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ';':
                    buffer += c
                    self.tokens.append(token(buffer, 'puntocoma', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ',':
                    buffer += c
                    self.tokens.append(token(buffer, 'coma', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '[':
                    buffer += c
                    self.tokens.append(token(buffer, 'corchetea', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ']':
                    buffer += c
                    self.tokens.append(token(buffer, 'corchetec', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '(':
                    buffer += c
                    self.tokens.append(token(buffer, 'parentesisa', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ')':
                    buffer += c
                    self.tokens.append(token(buffer, 'parentesisc', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '"':
                    buffer += c
                    columna += 1
                    estado = 1
                elif re.search('\d', c):
                    buffer += c
                    columna += 1
                    estado = 2
                elif re.search('[a-zA-Z]', c):
                    buffer += c
                    columna += 1
                    estado = 3
                elif c == '#':
                    columna += 1
                    estado = 4
                elif c == "'":
                    columna += 1
                    estado = 4
                elif c == '\n':
                    linea += 1
                    columna = 1
                elif c == '\t':
                    columna += 1
                elif c == ' ':
                    columna += 1
                elif c == '\r':
                    pass
                elif c == centinel:
                    self.tokens.append(token(c,'EOF',linea,columna))
                    break
                else:
                    buffer += c
                    self.tokens.append(token(buffer, 'error',linea,columna))
                    self.errores.append(error(buffer , 'Lexico', linea, columna))
                    buffer = ''
                    columna += 1
            elif estado == 1:
                if  c == '"':
                    buffer += c
                    self.tokens.append(token(buffer, 'cadena', linea, columna))
                    buffer = ''
                    columna += 1
                    estado = 0
                elif c == '\n':
                    buffer += c
                    linea += 1
                    columna = 1
                elif c == '\r':
                    buffer += c
                else:
                    buffer += c
                    columna += 1
            elif estado == 2:
                if re.search('\d', c):
                    buffer += c
                    columna += 1
                elif c == '.':
                    buffer += c
                    columna += 1
                else:
                    if buffer.find('.')!=-1:
                        self.tokens.append(token(buffer,'decimal',linea,columna))
                        buffer = ''
                        i -= 1
                        estado = 0
                    else:
                        self.tokens.append(token(buffer, 'entero', linea, columna))
                        buffer = ''
                        i -= 1
                        estado = 0
            elif estado == 3:
                if re.search('[a-zA-Z]', c):
                    buffer += c
                    columna += 1
                else:
                    if buffer == 'Claves':
                        self.tokens.append(token(buffer, 'claves', linea, columna))
                    elif buffer == 'Registros':
                        self.tokens.append(token(buffer, 'registros', linea, columna))
                    elif buffer == 'imprimir':
                        self.tokens.append(token(buffer, 'imprimir', linea, columna))
                    elif buffer == 'imprimirln':
                        self.tokens.append(token(buffer, 'imprimirln', linea, columna))
                    elif buffer == 'conteo':
                        self.tokens.append(token(buffer, 'conteo', linea, columna))
                    elif buffer == 'promedio':
                        self.tokens.append(token(buffer, 'promedio', linea, columna))
                    elif buffer == 'contarsi':
                        self.tokens.append(token(buffer, 'contarsi', linea, columna))
                    elif buffer == 'datos':
                        self.tokens.append(token(buffer, 'datos',linea,columna))
                    elif buffer == 'sumar':
                        self.tokens.append(token(buffer, 'sumar',linea,columna))
                    elif buffer == 'max':
                        self.tokens.append(token(buffer, 'maximo',linea,columna))
                    elif buffer == 'min':
                        self.tokens.append(token(buffer, 'minimo',linea,columna))
                    elif buffer == 'exportarReporte':
                        self.tokens.append(token(buffer, 'reporte',linea,columna))
                    else:
                        self.tokens.append(token(buffer, 'error',linea,columna))
                        self.errores.append(error(buffer,'Lexico',linea,columna))
                    buffer = ''
                    i -= 1
                    estado = 0

            elif estado == 4:
                if re.search('[a-zA-Z0-9_]',c):
                    columna += 1
                else:
                    i -= 1
                    estado = 0

            i += 1

    def del_from_token(self):
        aux=tuple(self.tokens)
        for e in range(len(self.errores)):
            for t in range(len(aux)): 
                if self.errores[e].caracter == aux[t].lexema and self.errores[e].tipo == 'Lexico':
                    self.tokens.pop(t)
              
    def html_T(self):
        file = open('Reporte_Tokens.html','w')
        content='''
                    <!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                <link rel="stylesheet" href="style.css">
                                <title>Reporte</title>
                            </head>
                            <body>
                            <div class="container-table">
                            <div class="table__title1">
                                Reporte de Tokens
                            </div></div>
        '''
        content+="""<div id="main-container">
                            <table>
                            <thead>
				            <tr>
					        <th style="border-top-left-radius: 20px;">Token</th><th>Lexema</th><th>Fila</th><th style="border-top-right-radius: 20px;">Columna</th>
				            </tr>
			</thead>
                            """   
        for t in self.tokens:
            print(t.lexema)
            content+='<tr>'
            content+=t.Rtokens()
            content+='</tr>'

        content+='</table>'
        content+="</div>\n"
        content+='</body>\n</html>'
        file.write(content)
        file.close()

    def html_E(self):
        file = open('Reporte_Errores.html','w')
        content='''
                <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <meta http-equiv="X-UA-Compatible" content="IE=edge">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <link rel="stylesheet" href="style.css">
                            <title>Reporte</title>
                        </head>
                        <body>
                            <div class="container-table">
                            <div class="table__title1">
                                Reporte de Errores
                            </div></div>
                '''

        if len(self.errores) == 0:
            content+='''<div class="container-table">
                            <div class="table__title1">
                                No hubieron errores
                            </div></div>'''
        else:
            
            content+="""<div id="main-container">
                            <table>
                            <thead>
				            <tr>
					        <th style="border-top-left-radius: 20px;">Caracter</th><th>Tipo de Error</th><th>Fila</th><th style="border-top-right-radius: 20px;">Columna</th>
				            </tr>
			                </thead>
                            """   
            for e in self.errores:
                #print(e.caracter)
                content+='<tr>'
                content+=e.Rerror()
                content+='</tr>'

            content+='</table>'
            content+="</div>\n"

        content+='</body>\n</html>'
        file.write(content)
        file.close()


class analizador_sintactico:
    def __init__(self):
        self.tokens = []
        self.errores = []
        self.i = 0

    def val_reg(self):
        if self.listaTokens[self.i].tipo == 'cadena' :
            lexema = self.listaTokens[self.i].lexema.replace('"', '')
            ex = expresion('cadena',lexema)
            self.i+= 1 #retorna un valor individual
            return ex
        elif self.listaTokens[self.i].tipo == 'entero' :
            ex = expresion('entero',self.listaTokens[self.i].lexema)
            self.i += 1
            return ex
        elif self.listaTokens[self.i].tipo == 'decimal' :
            ex = expresion('decimal',self.listaTokens[self.i].lexema)
            self.i += 1
            return ex

    def lista_val_reg2(self):
        if self.listaTokens[self.i].tipo == 'llavec' :
            pass
        elif self.listaTokens[self.i].tipo == 'coma' :
            self.i += 1
            val_reg = self.val_reg() #lo añade a una lista
            lista2 = self.lista_val_reg2()
            return ListaValReg2(val_reg,lista2)

    def lista_val_reg(self):
        val_reg = self.val_reg()
        lista = self.lista_val_reg2()
        return ListaValReg(val_reg,lista)

    def registro(self):
        if self.listaTokens[self.i].tipo == 'llavea' :
            self.i += 1
            lista_registros = self.lista_val_reg()
            if self.listaTokens[self.i].tipo == 'llavec' :
                self.i += 1
                return lista_registros

    def lista_registros2(self):
        if self.listaTokens[self.i].tipo == 'corchetec' :
            pass
        else:
            r = self.registro()
            lista = self.lista_registros2()
            return ListaRegistros2(r,lista)
    
    def lista_registros(self):
        r = self.registro()
        lista = self.lista_registros2()
        return ListaRegistros(r,lista)

    def ins_registros(self):
        if self.listaTokens[self.i].tipo == 'registros' :
            self.i += 1
            if self.listaTokens[self.i].tipo == 'igual' :
                self.i += 1
                if self.listaTokens[self.i].tipo == 'corchetea' :
                    self.i += 1
                    lista = self.lista_registros()
                    if self.listaTokens[self.i].tipo == 'corchetec' :
                        self.i += 1
                        return IntruccionRegistros(lista)
                    else:
                        linea = self.listaTokens[self.i].linea
                        columna = self.listaTokens[self.i].columna
                        self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                 
                else:
                    linea = self.listaTokens[self.i].linea
                    columna = self.listaTokens[self.i].columna
                    self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
          
            else:
                linea = self.listaTokens[self.i].linea
                columna = self.listaTokens[self.i].columna
                self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
    
        else:
            linea = self.listaTokens[self.i].linea
            columna = self.listaTokens[self.i].columna
            self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
 
    def val_cls(self):
        if self.listaTokens[self.i].tipo == 'cadena' :
            lexema = self.listaTokens[self.i].lexema.replace('"', '')
            print(lexema)
            ex = expresion('cadena',lexema)
            self.i+= 1
            return ex

    def lista_claves2(self):
        if self.listaTokens[self.i].tipo == 'corchetec' :
            pass
        elif self.listaTokens[self.i].tipo == 'coma' :
            self.i += 1
            ex = self.val_cls()
            lista2 = self.lista_claves2()
            return ListaClaves2(ex,lista2)

    def lista_claves(self):
        ex = self.val_cls()
        lista = self.lista_claves2()
        return ListaClaves(ex,lista)

    def ins_claves(self): 
        if self.listaTokens[self.i].tipo == 'claves' :
            self.i += 1
            if self.listaTokens[self.i].tipo == 'igual' :
                self.i += 1
                if self.listaTokens[self.i].tipo == 'corchetea' :
                    self.i += 1
                    lista = self.lista_claves()
                    if self.listaTokens[self.i].tipo == 'corchetec' :
                        self.i += 1
                        return IntruccionClaves(lista)
                    else:
                        linea = self.listaTokens[self.i].linea
                        columna = self.listaTokens[self.i].columna
                        self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                     
                else:
                    linea = self.listaTokens[self.i].linea
                    columna = self.listaTokens[self.i].columna
                    self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
               
            else:
                linea = self.listaTokens[self.i].linea
                columna = self.listaTokens[self.i].columna
                self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
             
        else:
            linea = self.listaTokens[self.i].linea
            columna = self.listaTokens[self.i].columna
            self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
        
    def ins_imprimir(self):
        if self.listaTokens[self.i].tipo == 'imprimir':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'cadena':
                    c = expresion('cadena',self.listaTokens[self.i].lexema.replace('"',''))
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'parentesisc':
                        self.i += 1
                        if self.listaTokens[self.i].tipo == 'puntocoma':
                            self.i += 1
                            return IntruccionImprimir(c)
                        else:
                            linea = self.listaTokens[self.i].linea
                            columna = self.listaTokens[self.i].columna
                            self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                        
                    else:
                        linea = self.listaTokens[self.i].linea
                        columna = self.listaTokens[self.i].columna
                        self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
               
                else:
                    linea = self.listaTokens[self.i].linea
                    columna = self.listaTokens[self.i].columna
                    self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
             
            else:
                linea = self.listaTokens[self.i].linea
                columna = self.listaTokens[self.i].columna
                self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
             
        else:
            linea = self.listaTokens[self.i].linea
            columna = self.listaTokens[self.i].columna
            self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
            
    def ins_imprimirln(self):
        if self.listaTokens[self.i].tipo == 'imprimirln':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'cadena':
                    c = expresion('cadena',self.listaTokens[self.i].lexema.replace('"',''))
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'parentesisc':
                        self.i += 1
                        if self.listaTokens[self.i].tipo == 'puntocoma':
                            self.i += 1
                            return IntruccionImprimirln(c)
                        else:
                            linea = self.listaTokens[self.i].linea
                            columna = self.listaTokens[self.i].columna
                            self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                          
                    else:
                        linea = self.listaTokens[self.i].linea
                        columna = self.listaTokens[self.i].columna
                        self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                     
                else:
                    linea = self.listaTokens[self.i].linea
                    columna = self.listaTokens[self.i].columna
                    self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
               
            else:
                linea = self.listaTokens[self.i].linea
                columna = self.listaTokens[self.i].columna
                self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                 
        else:
            linea = self.listaTokens[self.i].linea
            columna = self.listaTokens[self.i].columna
            self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                                                
    def ins_conteo(self):
        if self.listaTokens[self.i].tipo == 'conteo':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'parentesisc':
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'puntocoma':
                        self.i += 1
                        return IntruccionConteo()
                    else:
                        linea = self.listaTokens[self.i].linea
                        columna = self.listaTokens[self.i].columna
                        self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                     
                else:
                    linea = self.listaTokens[self.i].linea
                    columna = self.listaTokens[self.i].columna
                    self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                    
            else:
                linea = self.listaTokens[self.i].linea
                columna = self.listaTokens[self.i].columna
                self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                  
        else:
            linea = self.listaTokens[self.i].linea
            columna = self.listaTokens[self.i].columna
            self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
            
    def ins_promedio(self):
        if self.listaTokens[self.i].tipo == 'promedio':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'cadena':
                    c = expresion('cadena',self.listaTokens[self.i].lexema.replace('"',''))
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'parentesisc':
                        self.i += 1
                        if self.listaTokens[self.i].tipo == 'puntocoma':
                            self.i += 1
                            return IntruccionPromedio(c)
                        else:
                            linea = self.listaTokens[self.i].linea
                            columna = self.listaTokens[self.i].columna
                            self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                          
                    else:
                        linea = self.listaTokens[self.i].linea
                        columna = self.listaTokens[self.i].columna
                        self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                     
                else:
                    linea = self.listaTokens[self.i].linea
                    columna = self.listaTokens[self.i].columna
                    self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                    
            else:
                linea = self.listaTokens[self.i].linea
                columna = self.listaTokens[self.i].columna
                self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                 
        else:
            linea = self.listaTokens[self.i].linea
            columna = self.listaTokens[self.i].columna
            self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
         
    def ins_contarsi(self):
        if self.listaTokens[self.i].tipo == 'contarsi':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'cadena':
                    c = expresion('cadena',self.listaTokens[self.i].lexema.replace('"',''))
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'coma':
                        self.i += 1
                        if self.listaTokens[self.i].tipo == 'entero':
                            n = int(self.listaTokens[self.i].lexema.replace('"',''))
                            self.i += 1
                            if self.listaTokens[self.i].tipo == 'parentesisc':
                                self.i += 1
                                if self.listaTokens[self.i].tipo == 'puntocoma':
                                    self.i += 1
                                    return IntruccionContarsi(c,n)
                                else:
                                    linea = self.listaTokens[self.i].linea
                                    columna = self.listaTokens[self.i].columna
                                    self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                                 
                            else:
                                linea = self.listaTokens[self.i].linea
                                columna = self.listaTokens[self.i].columna
                                self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                       
                        else:
                            linea = self.listaTokens[self.i].linea
                            columna = self.listaTokens[self.i].columna
                            self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                           
                    else:
                        linea = self.listaTokens[self.i].linea
                        columna = self.listaTokens[self.i].columna
                        self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                       
                else:
                    linea = self.listaTokens[self.i].linea
                    columna = self.listaTokens[self.i].columna
                    self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                   
            else:
                linea = self.listaTokens[self.i].linea
                columna = self.listaTokens[self.i].columna
                self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                  
        else:
            linea = self.listaTokens[self.i].linea
            columna = self.listaTokens[self.i].columna
            self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
         
    def ins_datos(self):
        if self.listaTokens[self.i].tipo == 'datos':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'parentesisc':
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'puntocoma':
                        self.i += 1
                        return IntruccionDatos()
                    else:
                        linea = self.listaTokens[self.i].linea
                        columna = self.listaTokens[self.i].columna
                        self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                  
                else:
                    linea = self.listaTokens[self.i].linea
                    columna = self.listaTokens[self.i].columna
                    self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
             
            else:
                linea = self.listaTokens[self.i].linea
                columna = self.listaTokens[self.i].columna
                self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
             
        else:
            linea = self.listaTokens[self.i].linea
            columna = self.listaTokens[self.i].columna
            self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   

    def ins_sumar(self):
        if self.listaTokens[self.i].tipo == 'sumar':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'cadena':
                    c = expresion('cadena',self.listaTokens[self.i].lexema.replace('"',''))
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'parentesisc':
                        self.i += 1
                        if self.listaTokens[self.i].tipo == 'puntocoma':
                            self.i += 1
                            return IntruccionSumar(c)
                        else:
                            linea = self.listaTokens[self.i].linea
                            columna = self.listaTokens[self.i].columna
                            self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
               
                    else:
                        linea = self.listaTokens[self.i].linea
                        columna = self.listaTokens[self.i].columna
                        self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                   
                else:
                    linea = self.listaTokens[self.i].linea
                    columna = self.listaTokens[self.i].columna
                    self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                 
            else:
                linea = self.listaTokens[self.i].linea
                columna = self.listaTokens[self.i].columna
                self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
              
        else:
            linea = self.listaTokens[self.i].linea
            columna = self.listaTokens[self.i].columna
            self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                              
    def ins_max(self):
        if self.listaTokens[self.i].tipo == 'maximo':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'cadena':
                    c = expresion('cadena',self.listaTokens[self.i].lexema.replace('"',''))
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'parentesisc':
                        self.i += 1
                        if self.listaTokens[self.i].tipo == 'puntocoma':
                            self.i += 1
                            return IntruccionMax(c)
                        else:
                            linea = self.listaTokens[self.i].linea
                            columna = self.listaTokens[self.i].columna
                            self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                           
                    else:
                        linea = self.listaTokens[self.i].linea
                        columna = self.listaTokens[self.i].columna
                        self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                       
                else:
                    linea = self.listaTokens[self.i].linea
                    columna = self.listaTokens[self.i].columna
                    self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                    
            else:
                linea = self.listaTokens[self.i].linea
                columna = self.listaTokens[self.i].columna
                self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                   
        else:
            linea = self.listaTokens[self.i].linea
            columna = self.listaTokens[self.i].columna
            self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
            
    def ins_min(self):
        if self.listaTokens[self.i].tipo == 'minimo':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'cadena':
                    c = expresion('cadena',self.listaTokens[self.i].lexema.replace('"',''))
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'parentesisc':
                        self.i += 1
                        if self.listaTokens[self.i].tipo == 'puntocoma':
                            self.i += 1
                            return IntruccionMin(c)
                        else:
                            linea = self.listaTokens[self.i].linea
                            columna = self.listaTokens[self.i].columna
                            self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                            
                    else:
                        linea = self.listaTokens[self.i].linea
                        columna = self.listaTokens[self.i].columna
                        self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                      
                else:
                    linea = self.listaTokens[self.i].linea
                    columna = self.listaTokens[self.i].columna
                    self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                   
            else:
                linea = self.listaTokens[self.i].linea
                columna = self.listaTokens[self.i].columna
                self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                   
        else:
            linea = self.listaTokens[self.i].linea
            columna = self.listaTokens[self.i].columna
            self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
            
    def ins_reporte(self):
        if self.listaTokens[self.i].tipo == 'reporte':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'cadena':
                    c = expresion('cadena',self.listaTokens[self.i].lexema.replace('"',''))
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'parentesisc':
                        self.i += 1
                        if self.listaTokens[self.i].tipo == 'puntocoma':
                            self.i += 1
                            return IntruccionReporte(c)
                        else:
                            linea = self.listaTokens[self.i].linea
                            columna = self.listaTokens[self.i].columna
                            self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                           
                    else:
                        linea = self.listaTokens[self.i].linea
                        columna = self.listaTokens[self.i].columna
                        self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                        
                else:
                    linea = self.listaTokens[self.i].linea
                    columna = self.listaTokens[self.i].columna
                    self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                   
            else:
                linea = self.listaTokens[self.i].linea
                columna = self.listaTokens[self.i].columna
                self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
                  
        else:
            linea = self.listaTokens[self.i].linea
            columna = self.listaTokens[self.i].columna
            self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
            
    def instruccion(self):
        if self.listaTokens[self.i].tipo == 'registros' :
            i = self.ins_registros()
            return Instruccion(i)
        elif self.listaTokens[self.i].tipo == 'claves' :
            i = self.ins_claves()
            return Instruccion(i)
        elif self.listaTokens[self.i].tipo == 'imprimir':
            i = self.ins_imprimir()
            return Instruccion(i)
        elif self.listaTokens[self.i].tipo == 'imprimirln':
            i = self.ins_imprimirln()
            return Instruccion(i)
        elif self.listaTokens[self.i].tipo == 'conteo':
            i = self.ins_conteo()
            return Instruccion(i)
        elif self.listaTokens[self.i].tipo == 'promedio':
            i = self.ins_promedio()
            return Instruccion(i)
        elif self.listaTokens[self.i].tipo == 'contarsi':
            i = self.ins_contarsi()
            return Instruccion(i)
        elif self.listaTokens[self.i].tipo == 'datos':
            i = self.ins_datos()
            return Instruccion(i)
        elif self.listaTokens[self.i].tipo == 'sumar':
            i = self.ins_sumar()
            return Instruccion(i)
        elif self.listaTokens[self.i].tipo == 'maximo':
            i = self.ins_max()
            return Instruccion(i)
        elif self.listaTokens[self.i].tipo == 'minimo':
            i = self.ins_min()
            return Instruccion(i)
        elif self.listaTokens[self.i].tipo == 'reporte':
            i = self.ins_reporte()
            return Instruccion(i)
        else:
            linea = self.listaTokens[self.i].linea
            columna = self.listaTokens[self.i].columna
            self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
            self.i+=1
            
    def ins_eof(self):
        return InstruccionEOF()

    def lista_instrucciones2(self):
        if self.listaTokens[self.i].tipo == 'EOF' :
            print('analisis sintactico exitoso')
            eof=self.ins_eof()
            return ListaInstrucciones2(eof,[])
        else:
            i = self.instruccion()
            lista2 = self.lista_instrucciones2()
            return ListaInstrucciones2(i,lista2)

    def lista_instrucciones(self):
        i = self.instruccion()
        lista2 = self.lista_instrucciones2()
        return ListaInstrucciones(i,lista2)
          
    def inicio(self):
        lista = self.lista_instrucciones()
        return Inicio(lista)

    def analizar(self, listaTokens,listaErrores):
        print()
        self.i = 0
        self.listaTokens = listaTokens
        self.listaErrores = listaErrores
        arbol = self.inicio()
        if len(self.listaErrores)==0: 
            arbol.ejecutar({})
            arbol.getNodos()
        else:
            global consola
            for e in self.listaErrores:
                consola+='Error: '+e.tipo+' de: '+e.caracter+' En linea: '+str(e.linea)+' Columna: '+str(e.columna)+'\n'
            print(consola)
        print()
