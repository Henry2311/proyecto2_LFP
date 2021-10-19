from os import path
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
            #lexema = self.listaTokens[self.i].lexema.replace('"', '')
            #print(lexema)
            self.i+= 1
        elif self.listaTokens[self.i].tipo == 'entero' :
            #print(self.listaTokens[self.i].lexema)
            self.i += 1
        elif self.listaTokens[self.i].tipo == 'decimal' :
            #print(self.listaTokens[self.i].lexema)
            self.i += 1
        else: 
            pass

    def lista_val_reg2(self):
        if self.listaTokens[self.i].tipo == 'llavec' :
            pass
        elif self.listaTokens[self.i].tipo == 'coma' :
            self.i += 1
            self.val_reg()
            self.lista_val_reg2()

    def lista_val_reg(self):
        self.val_reg()
        self.lista_val_reg2()

    def registro(self):
        if self.listaTokens[self.i].tipo == 'llavea' :
            self.i += 1
            self.lista_val_reg()
            if self.listaTokens[self.i].tipo == 'llavec' :
                self.i += 1

    def lista_registros2(self):
        if self.listaTokens[self.i].tipo == 'corchetec' :
            pass
        else:
            self.registro()
            self.lista_registros2()
    
    def lista_registros(self):
        self.registro()
        self.lista_registros2()

    def ins_registros(self):
        if self.listaTokens[self.i].tipo == 'registros' :
            self.i += 1
            if self.listaTokens[self.i].tipo == 'igual' :
                self.i += 1
                if self.listaTokens[self.i].tipo == 'corchetea' :
                    self.i += 1
                    self.lista_registros()
                    if self.listaTokens[self.i].tipo == 'corchetec' :
                        self.i += 1

    def val_cls(self):
        if self.listaTokens[self.i].tipo == 'cadena' :
            lexema = self.listaTokens[self.i].lexema.replace('"', '')
            print(lexema)
            self.i+= 1
        else:
            pass

    def lista_claves2(self):
        if self.listaTokens[self.i].tipo == 'corchetec' :
            pass
        elif self.listaTokens[self.i].tipo == 'coma' :
            self.i += 1
            self.val_cls()
            self.lista_claves2()

    def lista_claves(self):
        self.val_cls()
        self.lista_claves2()

    def ins_claves(self):
        if self.listaTokens[self.i].tipo == 'claves' :
            self.i += 1
            if self.listaTokens[self.i].tipo == 'igual' :
                self.i += 1
                if self.listaTokens[self.i].tipo == 'corchetea' :
                    self.i += 1
                    self.lista_claves()
                    if self.listaTokens[self.i].tipo == 'corchetec' :
                        self.i += 1

    def ins_imprimir(self):
        if self.listaTokens[self.i].tipo == 'imprimir':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'cadena':
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'parentesisc':
                        self.i += 1
                        if self.listaTokens[self.i].tipo == 'puntocoma':
                            self.i += 1
    
    def ins_imprimirln(self):
        if self.listaTokens[self.i].tipo == 'imprimirln':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'cadena':
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'parentesisc':
                        self.i += 1
                        if self.listaTokens[self.i].tipo == 'puntocoma':
                            self.i += 1

    def ins_conteo(self):
        if self.listaTokens[self.i].tipo == 'conteo':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'parentesisc':
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'puntocoma':
                        self.i += 1

    def ins_promedio(self):
        if self.listaTokens[self.i].tipo == 'promedio':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'cadena':
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'parentesisc':
                        self.i += 1
                        if self.listaTokens[self.i].tipo == 'puntocoma':
                            self.i += 1

    def ins_contarsi(self):
        if self.listaTokens[self.i].tipo == 'contarsi':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'cadena':
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'coma':
                        self.i += 1
                        if self.listaTokens[self.i].tipo == 'entero':
                            self.i += 1
                            if self.listaTokens[self.i].tipo == 'parentesisc':
                                self.i += 1
                                if self.listaTokens[self.i].tipo == 'puntocoma':
                                    self.i += 1

    def ins_datos(self):
        if self.listaTokens[self.i].tipo == 'datos':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'parentesisc':
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'puntocoma':
                        self.i += 1

    def ins_sumar(self):
        if self.listaTokens[self.i].tipo == 'sumar':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'cadena':
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'parentesisc':
                        self.i += 1
                        if self.listaTokens[self.i].tipo == 'puntocoma':
                            self.i += 1

    def ins_max(self):
        if self.listaTokens[self.i].tipo == 'maximo':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'cadena':
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'parentesisc':
                        self.i += 1
                        if self.listaTokens[self.i].tipo == 'puntocoma':
                            self.i += 1

    def ins_min(self):
        if self.listaTokens[self.i].tipo == 'minimo':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'cadena':
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'parentesisc':
                        self.i += 1
                        if self.listaTokens[self.i].tipo == 'puntocoma':
                            self.i += 1

    def ins_reporte(self):
        if self.listaTokens[self.i].tipo == 'reporte':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'parentesisa':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'cadena':
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'parentesisc':
                        self.i += 1
                        if self.listaTokens[self.i].tipo == 'puntocoma':
                            self.i += 1

    def instruccion(self):
        if self.listaTokens[self.i].tipo == 'registros' :
            self.ins_registros()
        elif self.listaTokens[self.i].tipo == 'claves' :
            self.ins_claves()
        elif self.listaTokens[self.i].tipo == 'imprimir':
            self.ins_imprimir()
        elif self.listaTokens[self.i].tipo == 'imprimirln':
            self.ins_imprimirln()
        elif self.listaTokens[self.i].tipo == 'conteo':
            self.ins_conteo()
        elif self.listaTokens[self.i].tipo == 'promedio':
            self.ins_promedio()
        elif self.listaTokens[self.i].tipo == 'contarsi':
            self.ins_contarsi()
        elif self.listaTokens[self.i].tipo == 'datos':
            self.ins_datos()
        elif self.listaTokens[self.i].tipo == 'sumar':
            self.ins_sumar()
        elif self.listaTokens[self.i].tipo == 'maximo':
            self.ins_max()
        elif self.listaTokens[self.i].tipo == 'minimo':
            self.ins_min()
        elif self.listaTokens[self.i].tipo == 'reporte':
            self.ins_reporte()
        else:
            linea = self.listaTokens[self.i].linea
            columna = self.listaTokens[self.i].columna
            self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))   
            self.i+=1
            self.instruccion()
            self.lista_instrucciones2()
    
    def lista_instrucciones2(self):
        if self.listaTokens[self.i].tipo == 'registros' :
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'claves' :
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'imprimir':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'imprimirln':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'conteo':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'promedio':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'contarsi':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'datos':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'sumar':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'maximo':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'minimo':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'reporte':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'EOF' :
            print('analisis sintactico exitoso')
        else:
            linea = self.listaTokens[self.i].linea
            columna = self.listaTokens[self.i].columna
            self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna))
            self.instruccion()
            self.lista_instrucciones2()

    def lista_instrucciones(self):
        if self.listaTokens[self.i].tipo == 'registros' :
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'claves' :
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'imprimir':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'imprimirln':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'conteo':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'promedio':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'contarsi':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'datos':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'sumar':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'maximo':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'minimo':
            self.instruccion()
            self.lista_instrucciones2()
        elif self.listaTokens[self.i].tipo == 'reporte':
            self.instruccion()
            self.lista_instrucciones2()
        else:
            linea = self.listaTokens[self.i].linea
            columna = self.listaTokens[self.i].columna
            self.listaErrores.append(error(self.listaTokens[self.i].lexema,'Sintactico', linea, columna ))
            self.instruccion()
            self.lista_instrucciones2()
    
    def inicio(self):
        self.lista_instrucciones()

    def analizar(self, listaTokens,listaErrores):
        print()
        self.i = 0
        self.listaTokens = listaTokens
        self.listaErrores = listaErrores
        self.inicio()
        print()



if __name__ == '__main__':
    ruta="prueba.lfp"
    archivo=open(ruta,'r')
    file =archivo.read()
    archivo.close()
    a_lexico=analizador_lexico()
    a_lexico.analizar(file)
    a_sintactico=analizador_sintactico()
    a_sintactico.analizar(a_lexico.tokens,a_lexico.errores)
    a_lexico.html_E()

