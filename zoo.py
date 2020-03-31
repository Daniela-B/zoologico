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
            self.set_clasificacion()
            print("Nuevo animal creado")
        print (lista)
        self.get_posicion()
        self.set_nuevotipo()
        self.get_nuevotipo()
    
    
    
    
    def set_nuevotipo(self):
        self.tipo= input("Dime el nuevo tipo: ")
        print ("El nuevo tipo es "+ self.tipo)
    def set_clasificacion(self):
        self.clasificacion = input("Dime la clasificacin del animal: ")
    def get_posicion (self):
        ID= int(input("Dime un id, 0 es el primero en la lista: "))
        self.name = lista[ID]
        print("El nombre de este animal es: " + self.name)    
    def get_nuevotipo(self):
        print ("El nombre del animal es " + self.name)
        print ("El tipo actual del animal es "+ self.tipo)
    
        
animal = Animal ()




