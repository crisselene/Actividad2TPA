#codigo para utilizar utf-8
import sys
import math
import random
sys.stdin.encoding
from random import *
'UTF-8' 
from builtins import str

listaInicial = []
picosyValles = []
cuenta=0
p=0
v=0
 #variables del correo y la contrasena del login
 #es obligar
correo = "actividad@gmail.com"
expediente = 21732599

#EjercicioA-------------------------------------------------------------------------------
def AobtenerMediana (lista):
    if(len(lista)%2!=0):
        pos =int((len(lista)/2)+1)
        print("El numero de elementos es impar",
        ", la posicion de la mediana es ",pos,"y su valor es ",lista[pos-1])
    else:
        pos =int((len(lista)/2))
        dato = lista[pos-1]+lista[pos]
        med = dato/2
        print("El numero de elementos es par y la mediana es: ", med)
 
    
def AjuntarYOrdenar(lista1,lista2):
    #meto los elementos de la lista2 en la lista1
    for i in range (0,len(lista2)):
        lista1.append(lista2[i])
    print("Lista sin ordenar: ",lista1)
    lista1 = Aquicksort(lista1)
    print("Lista ordenada: ",lista1)
    return lista1       

def Aquicksort(lista):
    #tres listas que marcaran los valores menores,mayores e iguales al pivote
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        #el primer elemento de la lista es el pivote
        pivote = lista[0]
        #se va recorriendo el array y se comparan los valores con el pivote
        for i in lista:
            #si el valor es menor que el pivote se pone a la izquierda
            if i < pivote:
                izquierda.append(i)
            #si el valor es igual que el pivote se pone en el centro
            elif i == pivote:
                centro.append(i)
            #si el valor es mayor que el pivote se pone a la derecha
            elif i > pivote:
                derecha.append(i)
        #se llama recursivamente con los arrays de derecha e izquierda
        return Aquicksort(izquierda)+centro+Aquicksort(derecha)
    else:
        return lista
#----------------------------------------------------------------------------------------
    

#EjercicioB------------------------------------------------------------------------------
def divideB(array,brray,inicio,fin):
    #metodo que utiliza divide and conquer para dividir al caso unidad
    #los arrays e ir comparando las posiciones
    #llama al metodo imprimirB 
    if inicio==fin :
        sonDistintos = imprimirB(array[fin],brray[fin])
    else:
        ma = int((inicio+fin)/2)
        sonDistintos = ma1=divideB(array,brray,inicio,ma)
        sonDistintos=ma2=divideB(array,brray,ma+1,fin);
    return sonDistintos
    
def compararLargoB(a,b): 
    #metodo que compara si los array tienen el mismo tamano y si es asi
    #llama al metodo divideB
    if(len(a) == len(b)): 
        print("Los arrays tienen el mismo largo")
        sonDistintos = divideB(a,b,0,len(a)-1)
    else : 
        print("Los arrays tienen distinto largo")  
        sonDistintos = 1
    return sonDistintos 
 
def imprimirB (a,b):
    #imprime los resultados y retorna el dato "sonDistintos"
    #que se iguala a 0 si los arrays tienen son iguales y 1 si son distintos
    if a==b:
        print("a:",a , " es igual a b:" , b)
        sonDistintos=0
        print("Iguales\n")
    else:
        print("a:",a , " es distinto a b:" , b)
        sonDistintos=1
        print("Distintas\n");
    return sonDistintos
#----------------------------------------------------------------------------------------

#EjercicioC------------------------------------------------------------------------------
def CtrasponerDC(m , fInicio, fFin, cInicio, cFin):
    if(fInicio<fFin):
        fmitad = int((fInicio+fFin)/2)
        cmitad = int((cInicio+cFin)/2)
        CtrasponerDC(m, fInicio, fmitad, cInicio, cmitad)
        CtrasponerDC(m, fInicio, fmitad, cmitad+1, cFin)
        CtrasponerDC (m, fmitad+1, fFin, cInicio, cmitad)
        CtrasponerDC (m, fmitad+1, fFin, cmitad+1, cFin)
        mtx =Cintercambiar (m, fmitad+1, cInicio, fInicio, cmitad+1, fFin-fmitad)
        return mtx
        
def Cintercambiar(m, fIniA, cIniA,fIniB,cIniB,dimen):
    i = 0
    j = 0
    while i<= dimen-1:
        while j<= dimen-1:
            aux = m[fIniA+i][cIniA+j]
            m[fIniA+i][cIniA+j] = m[fIniB+i][cIniB+j]
            m[fIniB+i][cIniB+j] = aux
            i+=1
            j+=1
    return m
#----------------------------------------------------------------------------------------

#EjercicioD------------------------------------------------------------------------------
def Drandom(lista,j):
    n = -1 #variable para comprobar que dos numeros consecutivos no sean iguales
    while j < 10 :
        num = randint(0, 10)
        j+=1
        if n != num:
            n = num
            lista.append(num)
        else:
            Drandom(lista,j)
        

def DgenerarArray():
    lista =[] #array vacio que se rellenara aleatoriamente
    Drandom(lista,0)
    return lista

def Ddivide(lista,inicio,fin):
    if inicio == fin:
        n1 = Dcomparar(lista[fin])
    else:
        mitad = int((inicio+fin)/2)
        n1 = Ddivide(lista,inicio,mitad)
        n1 = Ddivide(lista,mitad+1,fin)
    return(lista[fin])
       
def Dcomparar(valor):
    global p
    global v
    global posp
    global posv
    if (cuenta < len(listaInicial)-1):
        Dcontador()
        if valor > listaInicial[cuenta] and valor > listaInicial[cuenta-2]:
            if cuenta-1 != 0:
                print("pico en la posicion ", cuenta-1)
                #p sirve para saber si no se encuentra otro pico antes de encontrar un valle
                #posp sirve para guardar la posicion del pico
                if p==0:
                    p=1
                    posp=cuenta-1
                else: p=0
        if valor < listaInicial[cuenta] and valor < listaInicial[cuenta-2]:
            if cuenta-1 != 0:
                print("valle en la posicion ", cuenta-1)
                #v sirve para saber si no se encuentra otro valle antes de encontrar un pico
                #posv sirve para guardar la posicion del valle
                if v==0:
                    v=1
                    posv=cuenta-1
                else: v=0
        if(v==1 and p ==1):
            dato = listaInicial[posp]-listaInicial[posv]
            print("La diferencia del valle y el pico es: " , dato)
            print("---------------------------------------------------------------------------------------\n")
            menu()
            
def Dcontador():
    global cuenta
    cuenta+=1
#-----------------------------------------------------------------------------------------

       
def login():
   #se pide el correo
    email = input("Ingrese su email de la uem:")
    correo = email
    contrasena = (input("Ingrese la contrasena (numero de expediente):"))
    #la contrasena tiene que ser 21732599 obligatoriamente
    icontrasena = int(contrasena)
    if(icontrasena != expediente):
        print("No autorizado\nSALIENDO DEL PROGRAMA...")
    else: menu()
           
        
#Funcion para imprimir el menu y elegir opcion
def menu():
    print("\n******************** UNIVERSIDAD EUROPEA DE MADRID *************************\n"
         + ( "Escuela de Ingenieria Arquitectura y Diseno\n\n"))

    print("*****************MENU**********************\n"
          "A: Ejercicio A\n"
          "B: Ejercicio B\n"
          "C: Ejercicio C\n"
          "D: Ejercicio D\n"
          "S: Salir\n")
    opcion = input("Elija una opcion:")
    
    if opcion == "A" or opcion=="a":
        print("\n------------------------------EJERCICIO A---------------------------------------------")
        lista1 = [1,2,3,7,8]
        lista2 = [0,4,6,9]
        listaV = AjuntarYOrdenar(lista1, lista2)
        AobtenerMediana(listaV)
        print("---------------------------------------------------------------------------------------\n")
        menu()
    elif opcion == "B" or opcion =="b":
        print("\n------------------------------EJERCICIO B---------------------------------------------")
        a=[1,2,3]
        b=[1,2,4]
        sonDistintos = compararLargoB(a,b)
        if sonDistintos== 1 : print("Las listas son DISTINTAS")
        else: print("Las listas son IGUALES")
        print("---------------------------------------------------------------------------------------\n")
        menu()
    elif opcion == "C" or opcion =="c":
        print("\n------------------------------EJERCICIO C---------------------------------------------")
        m=[[1,2],[3,4]]
        print("Matriz: ",m)
        mtx = CtrasponerDC(m, 0, len(m)-1, 0, len(m)-1)
        print("Matriz traspuesta: ",mtx)
        print("---------------------------------------------------------------------------------------\n")
        menu()
    elif opcion == "D" or opcion =="d":
        print("\n------------------------------EJERCICIO D---------------------------------------------")
        array = DgenerarArray()
        print(array)
        global listaInicial   
        listaInicial = array
        Ddivide(array, 0, len(array)-1)  
    else:
        print("SALIENDO DEL PROGRAMA...")
        sys.exit(-1)

#ejecucion
login()




