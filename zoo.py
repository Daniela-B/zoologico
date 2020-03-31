# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
lista = []
class Animal:
    def __init__(self):
        num = int(input("¿Cuantos animales quieres?: "))
        for i in range (0,num):
            self.nombre=input("Dime el nombre del animal: ")
            lista.append(self.nombre)
            self.tipo =input("Dime el tipo de animal: ")
            print("Nuevo animal creado")
        print (lista)
        ID= int(input("Dime un id, 0 es el primero en la lista: "))
        dato =lista[ID]
        print ("El nombre de este animal es "+ dato)
        self.set_nuevotipo()
        
    def set_nuevotipo(self):
        self.tipo= input("Dime el nuevo tipo: ")
        print ("El nuevo tipo es "+ self.tipo)

animal = Animal ()



