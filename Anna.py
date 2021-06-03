# -*- coding: utf-8 -*-
"""
Created on Wed May 19 22:48:08 2021
@author: Sophia
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import logos
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.uic import loadUi
import cv2
import numpy as np
from PyQt5.QtWidgets import QMessageBox
import ntpath
global chan
import os 
#application_path = os.path.dirname(sys.executable)


#Variables
imagen = ''
hsv = ''
amarillo_bajos = ''
amarillo_altos = ''
rojo_bajos1 = ''
rojo_altos1 = ''
rojo_bajos2 = ''
rojo_altos2 = ''
cian_bajos = ''
cian_altos = ''
verde_bajos = ''
verde_altos = ''

cafe_bajos = ''
cafe_altos = ''
rosa_bajos = ''
rosa_altos = ''
violeta_bajos = ''
violeta_altos = ''
naranja_bajos = ''
naranja_altos = ''
azul_bajos = ''
azul_altos = ''
blanco_bajos = ''
blanco_altos = ''
negro_bajos = ''
negro_altos = ''
grises_bajos = ''
grises_altos = ''
mascara_verde = ''
mascara_rojo1 = ''
mascara_rojo2 = ''
mascara_azul = ''
mascara_cian = ''
mascara_anaranjado = ''
mascara_amarillo = ''
mascara_violeta = ''
mascara_rosa = ''
mascara_negro = ''
mascara_gris = ''
mascara_blancos = ''
mascara_cafe = ''
mask = ''
col1 = ''
col2 = ''
col3 = ''
col4 = ''
col5 = ''
col6 = ''
col7 = ''
col8 = ''
col9 = ''
col10 = ''
col11 = ''

def cambiarglobal(x):
        global chan
        chan = x
        return chan
        
class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('ana.ui', self)
        self.botbyn.clicked.connect(self.abrirventanabyn)
        self.botori.clicked.connect(self.abrirventanacolor)
        self.botinfoprin.clicked.connect(self.abririnfop)
        
    def abrirventanabyn(self):
        self.hide()
        otraventana = Ventanabyn(self)
        otraventana.show()
    
    def abrirventanacolor(self):
        self.hide()
        otraventana = Ventanacolor(self)
        otraventana.show()
     
    def abririnfop(self):
        otraventana = Ventanainfop(self)
        otraventana.show()

class Ventanainfop(QMainWindow):
    def __init__(self, parent=None):
        super(Ventanainfop, self).__init__(parent)
        loadUi('infprin.ui', self)
         

        
class Ventanabyn(QMainWindow):
    def __init__(self, parent=None):
        super(Ventanabyn, self).__init__(parent)
        loadUi('VBYN.ui', self)
        self.regresar.clicked.connect(self.abrirVentanaPrincipal) 
        self.infobyn.clicked.connect(self.abririnf1)
        self.verrojo.clicked.connect(self.showroj)
        self.saverojo.clicked.connect(self.saveroj)
        
        self.ververde.clicked.connect(self.showve)
        self.saveverde.clicked.connect(self.saveve)
        
        self.veramarillo.clicked.connect(self.showam)
        self.saveamarillo.clicked.connect(self.saveam)
        
        self.vercian.clicked.connect(self.showci)
        self.savecian.clicked.connect(self.saveci)
        
        self.vercafe.clicked.connect(self.showcaf)
        self.savecafe.clicked.connect(self.savecaf)
        
        self.vervioleta.clicked.connect(self.showvi)
        self.savevioleta.clicked.connect(self.savevi)
        
        self.verrosa.clicked.connect(self.showros)
        self.saverosa.clicked.connect(self.saveros)
        
        self.vernaranja.clicked.connect(self.showan)
        self.savenaranja.clicked.connect(self.savean)
        
        self.verblanco.clicked.connect(self.showblan)
        self.saveblanco.clicked.connect(self.saveblan)
        
        self.vernegro.clicked.connect(self.showneg)
        self.savenegro.clicked.connect(self.saveneg)
        
        self.vergris.clicked.connect(self.showgri)
        self.savegris.clicked.connect(self.savegri)
        
        self.verazul.clicked.connect(self.showaz)
        self.saveazul.clicked.connect(self.saveaz)
        
        self.select.clicked.connect(self.seleccionar_archivo)
        
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()  

    def abririnf1(self):
        otraventana = Ventanainf1(self)
        otraventana.show()
    

    def seleccionar_archivo(self):
        archivo, ok = QFileDialog.getOpenFileName(self, 'Select image file ...', 'C:\\Users', 'Image files (*.jpg *.png)')
        if ok:
            self.lblimg.setPixmap(QPixmap(archivo))
            self.lblimg.setScaledContents(True)
            #cambiarglobal(ntpath.basename(archivo))
            z = archivo
            cambiarglobal(z)
            #print (z)
            accionDeTodo(z)
            

#Definir Funciones para botones de Mostrar
    def showroj(self): 
        cv2.imshow('Final red', mask)
    
    def showve(self):
        cv2.imshow('Final green', mascara_verde)
    
    def showaz(self):
        cv2.imshow('Final blue', mascara_azul)
    
    def showci(self):
        cv2.imshow('Final cyan', mascara_cian)
    
    def showan(self):
        cv2.imshow('Final orange', mascara_anaranjado)
    
    def showam(self):
        cv2.imshow('Final Yellow', mascara_amarillo)
    
    def showvi(self):
        cv2.imshow('Final violet', mascara_violeta)
    
    def showros(self):
        cv2.imshow('Final pink', mascara_rosa)
    
    def showcaf(self):
       cv2.imshow('Final brown', mascara_cafe)
    
    def showblan(self):
        cv2.imshow('Final white', mascara_blancos)

    def showneg(self):
        cv2.imshow('Final black', mascara_negro)
    
    def showgri(self):
        cv2.imshow('Final gray', mascara_gris)    

#Definir Funciones para botones de Guardar
    def saveroj(self):
        save, ok = QFileDialog.getSaveFileName(self, 'Save in...', 'C:\\Users', '(*.png)')
        if ok:
            cv2.imwrite(save,mask)
            QMessageBox.about(self,"Saved successfully","Red color analysis saved successfully")
    
    def saveve(self):
        save, ok = QFileDialog.getSaveFileName(self, 'Save in...', 'C:\\Users', '(*.png)')
        if ok:
            cv2.imwrite(save,mascara_verde)
            QMessageBox.about(self, "Saved successfully","Green color analysis saved successfully")
        
    def saveaz(self):
        save, ok = QFileDialog.getSaveFileName(self, 'Save in...', 'C:\\Users', '(*.png)')
        if ok:
            cv2.imwrite(save,mascara_azul)
            QMessageBox.about(self, "Saved successfully","Blue color analysis saved successfully")
            
    def saveci(self):
        save, ok = QFileDialog.getSaveFileName(self, 'Save in...', 'C:\\Users', '(*.png)')
        if ok:
            cv2.imwrite(save,mascara_cian)
            QMessageBox.about(self, "Saved successfully","Cyan color analysis saved successfully")
                
    def savean(self):
        save, ok = QFileDialog.getSaveFileName(self, 'Save in...', 'C:\\Users', '(*.png)')
        if ok:
            cv2.imwrite(save,mascara_anaranjado)
            QMessageBox.about(self, "Saved successfully","Orange color analysis saved successfully")
    
    def saveam(self):
        save, ok = QFileDialog.getSaveFileName(self, 'Save in...', 'C:\\Users', '(*.png)')
        if ok:
            cv2.imwrite(save,mascara_amarillo)
            QMessageBox.about(self,"Saved successfully","Yellow color analysis saved successfully")
    
    def savevi(self):
        save, ok = QFileDialog.getSaveFileName(self, 'Save in...', 'C:\\Users', '(*.png)')
        if ok:
            cv2.imwrite(save,mascara_violeta)
            QMessageBox.about(self, "Saved successfully","Violet color analysis saved successfully")
    
    def saveros(self):
        save, ok = QFileDialog.getSaveFileName(self, 'Save in...', 'C:\\Users', '(*.png)')
        if ok:
            cv2.imwrite(save,mascara_rosa)
            QMessageBox.about(self, "Saved successfully","Pink color analysis saved successfully")

    def savecaf(self):
        save, ok = QFileDialog.getSaveFileName(self, 'Save in...', 'C:\\Users', '(*.png)')
        if ok:
            cv2.imwrite(save,mascara_cafe)
            QMessageBox.about(self, "Saved successfully","Brown color analysis saved successfully")

    def saveblan(self):
        save, ok = QFileDialog.getSaveFileName(self, 'Save in...', 'C:\\Users', '(*.png)')
        if ok:
            cv2.imwrite(save,mascara_blancos)
            QMessageBox.about(self, "Saved successfully","White color analysis saved successfully")
        
    def saveneg(self):
        save, ok = QFileDialog.getSaveFileName(self, 'Save in...', 'C:\\Users', '(*.png)')
        if ok:
            cv2.imwrite(save,mascara_negro)
            QMessageBox.about(self, "Saved successfully","Black color analysis saved successfully")

    def savegri(self):
        save, ok = QFileDialog.getSaveFileName(self, 'Save in...', 'C:\\Users', '(*.png)')
        if ok:
            cv2.imwrite(save,mascara_gris)
            QMessageBox.about(self, "Saved successfully","Gray color analysis saved successfully")

    def cambiarglobal(x):
        global chan
        chan = x
        return chan
    
class Ventanacolor(QMainWindow):
    
            
    def __init__(self, parent=None):
        super(Ventanacolor, self).__init__(parent)
        loadUi('VCOLOR.ui', self)
        self.regreso.clicked.connect(self.abrirVentanaPrincipal)
        self.inforiginal.clicked.connect(self.abririnf2)
        
        self.showrojo.clicked.connect(self.mosroj)
        self.savrojo.clicked.connect(self.guarroj)
        
        self.showverde.clicked.connect(self.mosver)
        self.savverde.clicked.connect(self.guarve)
        
        self.showamarillo.clicked.connect(self.mosama)
        self.savamarillo.clicked.connect(self.guaram)
        
        self.showcian.clicked.connect(self.moscia)
        self.savcian.clicked.connect(self.guarci)
        
        self.showcafe.clicked.connect(self.moscaf)
        self.savcafe.clicked.connect(self.guarcaf)
        
        self.showvioleta.clicked.connect(self.mosvio)
        self.savvioleta.clicked.connect(self.guarvi)
        
        self.showrosa.clicked.connect(self.mosros)
        self.savrosa.clicked.connect(self.guarros)
        
        self.shownaranja.clicked.connect(self.mosana)
        self.savnaranja.clicked.connect(self.guaran)
        
        self.showblanco.clicked.connect(self.mosblan)
        self.savblanco.clicked.connect(self.guarblan)
        
        self.shownegro.clicked.connect(self.mosneg)
        self.savnegro.clicked.connect(self.guarneg)
        
        self.showgris.clicked.connect(self.mosgri)
        self.savgris.clicked.connect(self.guargri)
        
        self.showazul.clicked.connect(self.mosazu)
        self.savazul.clicked.connect(self.guaraz)
        
        self.seleccionar.clicked.connect(self.select_archivo)
        
    def abrirVentanaPrincipal(self):
        self.parent().show()
        self.close()   
        
        
    def select_archivo(self):
        archivo, ok = QFileDialog.getOpenFileName(self, 'Select image file...', 'C:\\Users', 'Image files (*.jpg *.png)')
        if ok:
            self.lblim.setPixmap(QPixmap(archivo))
            self.lblim.setScaledContents(True)
            z = archivo
            cambiarglobal(z)
            #print (z)
            #print(chan)
            accionDeTodo(z)
            
    #Mostrar los colores detectados
    def mosroj(self):
        cv2.imshow('Red spectrum detected ', col3)

    def mosver(self):
        cv2.imshow('Green spectrum detected ', col1)    

    def mosazu(self):
        cv2.imshow('Blue spectrum detected ', col4)

    def moscia(self):
        cv2.imshow('Cyan spectrum detected ', col5)

    def mosana(self):
        cv2.imshow('Orange spectrum detected ', col2)

    def mosama(self):
        cv2.imshow('Yellow spectrum detected ', col6)

    def mosros(self):
        cv2.imshow('Pink spectrum detected ', col7)
        
    def mosvio(self):
        cv2.imshow('Violet spectrum detected ', col8)
    
    def mosblan(self):
        cv2.imshow('White spectrum detected ', col11)
    
    def mosneg(self):
        cv2.imshow('Black spectrum detected ', mascara_negro)
    
    def moscaf(self):
        cv2.imshow('Brown spectrum detected ', col9)
    
    def mosgri(self):
        cv2.imshow('Gray spectrum detected ', col10)
#Definir Funciones para botones de Guardar
    def guarroj(self): 
        save, ok = QFileDialog.getSaveFileName(self, 'Save in...', 'C:\\Users', '(*.png)')
        if ok:
            cv2.imwrite(save,col3)
            QMessageBox.about(self, "Saved successfully","Red color analysis saved successfully")
    
    def guarve(self):
        save, ok = QFileDialog.getSaveFileName(self, 'Save in...', 'C:\\Users', '(*.png)')
        if ok:
            cv2.imwrite(save,col1)
            QMessageBox.about(self, "Saved successfully","Green color analysis saved successfully")
    
    def guaraz(self):
        save, ok = QFileDialog.getSaveFileName(self, 'Save in...', 'C:\\Users', '(*.png)')
        if ok:
            cv2.imwrite(save,col4)
            QMessageBox.about(self, "Saved successfully","Blue color analysis saved successfully")
    
    def guarci(self):
        save, ok = QFileDialog.getSaveFileName(self, 'Save in...', 'C:\\Users', '(*.png)')
        if ok:
            cv2.imwrite(save,col5)
            QMessageBox.about(self, "Saved successfully","Cyan color analysis saved successfully")
    
    def guaran(self):
        save, ok = QFileDialog.getSaveFileName(self, 'Save in...', 'C:\\Users', '(*.png)')
        if ok:
            cv2.imwrite(save,col2)
            QMessageBox.about(self, "Saved successfully","Orange color analysis saved successfully")
    
    def guaram(self):
        save, ok = QFileDialog.getSaveFileName(self, 'Save in...', 'C:\\Users', '(*.png)')
        if ok:
            cv2.imwrite(save,col6)
            QMessageBox.about(self, "Saved successfully","Yellow color analysis saved successfully")
    
    def guarvi(self):
        save, ok = QFileDialog.getSaveFileName(self, 'Save in...', 'C:\\Users', '(*.png)')
        if ok:
            cv2.imwrite(save,col8)
            QMessageBox.about(self, "Saved successfully","Violet color analysis saved successfully")
    
    def guarros(self):
        save, ok = QFileDialog.getSaveFileName(self, 'Save in...', 'C:\\Users', '(*.png)')
        if ok:
            cv2.imwrite(save,col7)
            QMessageBox.about(self, "Saved successfully","Pink color analysis saved successfully")
    
    def guarcaf(self):
        save, ok = QFileDialog.getSaveFileName(self, 'Save in...', 'C:\\Users', '(*.png)')
        if ok:
            cv2.imwrite(save,col9)
            QMessageBox.about(self, "Saved successfully","Brown color analysis saved successfully")

    def guarblan(self):
        save, ok = QFileDialog.getSaveFileName(self, 'Save in...', 'C:\\Users', '(*.png)')
        if ok:
            cv2.imwrite(save,col11)
            QMessageBox.about(self, "Saved successfully","White color analysis saved successfully")
        
    def guarneg(self):
        save, ok = QFileDialog.getSaveFileName(self, 'Save in...', 'C:\\Users', '(*.png)')
        if ok:
            cv2.imwrite(save,mascara_negro)
            QMessageBox.about(self, "Saved successfully","Black color analysis saved successfully")

    def guargri(self):
        save, ok = QFileDialog.getSaveFileName(self, 'Save in...', 'C:\\Users', '(*.png)')
        if ok:
            cv2.imwrite(save,col10)
            QMessageBox.about(self, "Saved successfully","Gray color analysis saved successfully")
 
        
        
    def abririnf2(self):
        otraventana = Ventanainf2(self)
        otraventana.show()
        
    #Comienza OpenCv
    

def accionDeTodo(nombreArchivo):
    global imagen
    global hsv
    global amarillo_bajos
    global amarillo_altos
    global rojo_bajos1
    global rojo_altos1
    global rojo_bajos2
    global rojo_altos2
    global cian_bajos
    global cian_altos
    global verde_bajos
    global verde_altos    
    global cafe_bajos
    global cafe_altos
    global rosa_bajos
    global rosa_altos
    global violeta_bajos
    global violeta_altos
    global naranja_bajos
    global naranja_altos
    global azul_bajos
    global azul_altos
    global blanco_bajos
    global blanco_altos
    global negro_bajos
    global negro_altos
    global grises_bajos
    global grises_altos
    global mascara_verde
    global mascara_rojo1
    global mascara_rojo2
    global mascara_azul
    global mascara_cian
    global mascara_anaranjado
    global mascara_amarillo
    global mascara_violeta
    global mascara_rosa
    global mascara_negro
    global mascara_gris
    global mascara_blancos
    global mascara_cafe
    global mask
    global col1
    global col2
    global col3
    global col4
    global col5
    global col6
    global col7
    global col8
    global col9
    global col10
    global col11
    imagen = cv2.imread(nombreArchivo)
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    #Grupo de primarios de luz
    #Amarillo:
    amarillo_bajos = np.array([20,25,230], dtype=np.uint8)
    amarillo_altos = np.array([32,255,255], dtype=np.uint8)
    #Rojos:
    rojo_bajos1 = np.array([0,25,82], dtype=np.uint8)
    rojo_altos1 = np.array([5,255,255], dtype=np.uint8)
    rojo_bajos2 = np.array([170,25,135], dtype=np.uint8)
    rojo_altos2 = np.array([179,255,255], dtype=np.uint8)
    #Cian:
    cian_bajos = np.array([78,25,127], dtype=np.uint8)
    cian_altos = np.array([86,255,255], dtype=np.uint8)
    #Verdes:
    verde_bajos = np.array([33,63,51], dtype=np.uint8)
    verde_altos = np.array([77,255,255], dtype=np.uint8)
    
    #Grupo de secundarios de luz
    #Café:
    cafe_bajos = np.array([8,30,76], dtype=np.uint8)
    cafe_altos = np.array([30,211,179], dtype=np.uint8)
    #Rosa:
    rosa_bajos = np.array([145,25,204], dtype=np.uint8)
    rosa_altos = np.array([169,255,255], dtype=np.uint8)
    #Violeta:
    violeta_bajos = np.array([131,25,76], dtype=np.uint8)
    violeta_altos = np.array([144,255,255], dtype=np.uint8)
    #Anaranjado:
    naranja_bajos = np.array([6,25,178], dtype=np.uint8)
    naranja_altos = np.array([19,255,255], dtype=np.uint8) 
    #Azules:
    azul_bajos = np.array([87,25,178], dtype=np.uint8)
    azul_altos = np.array([130,255,255], dtype=np.uint8)
    
    #grupo de Neutros
    #Blanco:
    blanco_bajos = np.array([0,0,209], dtype=np.uint8)
    blanco_altos = np.array([179,25,255], dtype=np.uint8)
    #Negro:
    negro_bajos = np.array([0,0,0], dtype=np.uint8)
    negro_altos = np.array([159,63,51], dtype=np.uint8)
    #gris:
    grises_bajos = np.array([0,0,40], dtype=np.uint8)
    grises_altos = np.array([179,38,217], dtype=np.uint8)
    
    
    #Crear las mascaras
    mascara_verde = cv2.inRange(hsv, verde_bajos, verde_altos)
    mascara_rojo1 = cv2.inRange(hsv, rojo_bajos1, rojo_altos1)
    mascara_rojo2 = cv2.inRange(hsv, rojo_bajos2, rojo_altos2)
    mascara_azul = cv2.inRange(hsv, azul_bajos, azul_altos)
    mascara_cian = cv2.inRange(hsv, cian_bajos, cian_altos)
    mascara_anaranjado = cv2.inRange(hsv, naranja_bajos, naranja_altos)
    mascara_amarillo = cv2.inRange(hsv, amarillo_bajos, amarillo_altos)
    mascara_violeta = cv2.inRange(hsv, violeta_bajos, violeta_altos)
    mascara_rosa = cv2.inRange(hsv, rosa_bajos, rosa_altos)
    
    #Crear mascaras 2
    mascara_negro = cv2.inRange(hsv, negro_bajos, negro_altos)
    mascara_gris = cv2.inRange(hsv, grises_bajos, grises_altos)
    mascara_blancos = cv2.inRange(hsv, blanco_bajos, blanco_altos)
    mascara_cafe = cv2.inRange(hsv, cafe_bajos, cafe_altos)
    #Juntar mascara
    mask = cv2.add(mascara_rojo1, mascara_rojo2)
    
    #Mostrar colores detectados
    col1 = cv2.bitwise_and(imagen,imagen, mask= mascara_verde)
    col2 = cv2.bitwise_and(imagen,imagen, mask= mascara_anaranjado)
    col3 = cv2.bitwise_and(imagen,imagen, mask= mask)
    col4 = cv2.bitwise_and(imagen,imagen, mask= mascara_azul)
    col5 = cv2.bitwise_and(imagen,imagen, mask= mascara_cian)
    col6 = cv2.bitwise_and(imagen,imagen, mask= mascara_amarillo)
    col7 = cv2.bitwise_and(imagen,imagen, mask= mascara_rosa)
    col8 = cv2.bitwise_and(imagen,imagen, mask= mascara_violeta)
    col9 = cv2.bitwise_and(imagen,imagen, mask= mascara_cafe)
    col10 = cv2.bitwise_and(imagen,imagen, mask= mascara_gris)
    col11 = cv2.bitwise_and(imagen,imagen, mask= mascara_blancos)

class Ventanainf1(QMainWindow):
    def __init__(self, parent=None):
        super(Ventanainf1, self).__init__(parent)
        loadUi('inf1.ui', self)
        
class Ventanainf2(QMainWindow):
    def __init__(self, parent=None):
        super(Ventanainf2, self).__init__(parent)
        loadUi('inf2.ui', self)


app = QApplication(sys.argv)
main = VentanaPrincipal()
accionDeTodo('logo.png')
main.show()


sys.exit(app.exec_())
