##SI
import os
import sys
##NO
import sys, os
##Sin embargo, es correcto decir:
from subprocess import Popen, PIPE
from tkinter import E


# Alineado con el paréntesis que abre la función
def function_ex1(
                var1, var2, var3,
                var4):
    print(var1)



# Más indentación para distinguirla del resto de las líneas
fun = function_ex1(1, 2,3, 4)



# La línea de continuación no se distingue del contenido de la función
def function_ex2( 
    var1, var2, var3,
    var4):
    print(var1)
# Argumentos en la primera línea cuando no se está haciendo uso de la alineación vertical
fun = function_ex2(1, 2,
    4, 3)


var1=1
var2=1
var3=1
var4=1

if var1 > var2 and var3 > var4 \
    or var1 > var4:
    print(var1)
    
    
    
   
def funcion1():
    pass


def funcion2():
    pass


variable1 = 0
variable2 = 1


class Clase1():
    """clase Clase1"""
    varclase1 = "variable de clase1"

    def metodo1(self, var1):
        self.var1 = var1

    def metodo2(self):
        self.var1 += 1        
list=[]
data={}
def ejemplo(list,data):
    pass
##SI
ejemplo(list[1], {data: 2})
##NO
ejemplo( list[ 1 ], { data: 2 } )    
x=3
y=5

## Inmediatamente antes de una coma, un punto y coma o dos puntos:
##SI
if x == 4: print(x, y); x, y = y, x
##NO
if x == 4 : print(x , y) ; x , y = y , x

data=[]
##Inmediatamente antes del paréntesis que comienza la lista de argumentos en la llamada a una función:
##SI
ejemplo(1)
##NO
ejemplo (1)


##Inmediatamente antes de un corchete que empieza una indexación o “slicing” (término utilizado tanto en el ámbito de habla inglesa como española):

##SI
data[1] = list[1]
##NO
data [2] = list [1]



list = [
    var1, var2,
    var3, var4
    ]


list = [
    var1, var2,
    var3, var4
]