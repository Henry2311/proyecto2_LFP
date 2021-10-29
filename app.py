from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QFileDialog
from automata import *
from os import startfile

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 675)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 30, 171, 61))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.read_file)

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 120, 531, 521))
        self.plainTextEdit.setObjectName("plainTextEdit")
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(18)
        self.plainTextEdit.setFont(font)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(570, 120, 620, 521))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setWordWrapMode(QtGui.QTextOption.NoWrap)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(18)
        self.textBrowser.setFont(font)

        self.archivo=''
        self.lexico = analizador_lexico()
        self.sintactico = analizador_sintactico()

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(790, 30, 171, 61))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.analizar)

        self.pushButton_3 = QtWidgets.QComboBox(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(980, 30, 210, 61))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        items=["   Reportes","Reporte de Tokens","Reporte de Errores","Arbol de Derivacion"]
        self.pushButton_3.addItems(items)
        self.pushButton_3.activated.connect(self.reportes)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 381, 61))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "CARGAR ARCHIVO"))
        self.pushButton_2.setText(_translate("MainWindow", "ANALIZAR"))
        self.label.setText(_translate("MainWindow", "PROYECTO 2 - LFP"))

    def read_file(self):
        buscar = QFileDialog.getOpenFileName()
        extension=buscar[0].split('.')
        
        if extension[1] == 'lfp':
            file=open(buscar[0],'r')
            content=file.read()
            file.close()

            msj = QMessageBox()
            msj.setWindowTitle('Información')
            msj.setText('Archivo cargado correctamente')
            msj.exec()
            self.archivo = content
            self.plainTextEdit.setPlainText(self.archivo)
        else:
            msj = QMessageBox()
            msj.setWindowTitle('Error')
            msj.setText('Formato de archivo incorrecto')
            msj.exec()

    def analizar(self):
        archivo = self.plainTextEdit.toPlainText()
        if archivo == '':
            msj = QMessageBox()
            msj.setWindowTitle('Error')
            msj.setText('No se ha cargado el archivo')
            msj.exec()
        else:
            self.lexico.analizar(archivo)
            self.sintactico.analizar(self.lexico.tokens,self.lexico.errores)
            from arbol import consola
            self.textBrowser.setPlainText(consola)
            self.lexico.del_from_token()
            self.lexico.html_T()
            self.lexico.html_E()
            
    def reportes(self):
        archivo = self.plainTextEdit.toPlainText()
        if archivo == '':
            msj = QMessageBox()
            msj.setWindowTitle('Error')
            msj.setText('No se ha cargado el archivo')
            msj.exec()
        else:
            if self.pushButton_3.currentText() == 'Reporte de Tokens':
                startfile('Reporte_Tokens.html')
            elif self.pushButton_3.currentText() == 'Reporte de Errores':
                startfile('Reporte_Errores.html')
            elif self.pushButton_3.currentText() == 'Arbol de Derivacion':
                startfile('arbol.gv.pdf')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
