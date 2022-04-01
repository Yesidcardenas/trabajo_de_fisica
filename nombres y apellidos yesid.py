# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 23:06:17 2022

@author: usuario
"""

nombres = []
apellidos = []


for x in range(1):
    nom = input("por favor ingrese el nombre: ")
    nombres.append(nom)
    
    apellido1 = input("por favor ingrese primer apellido: ")
    apellido2 = input("por favor ingrese segundo apellido: ")
    apellidos.append([apellido1,apellido2])
    
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")


for x in range(1):
    print(" el nombre completo que ingreso es:", nombres[x],apellidos[x][0],apellidos[x][1]) 
    
    
    
    