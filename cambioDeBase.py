'''
Camila Zambrano
24/01/22
Ejercicio en clase: cambios de base
'''
from queue import Queue

def cambioACualquierBase(numero,base):
    stack = []
    resultado = ''
    
    while numero > 0:
        residuo = numero % base
        numero //= base
        stack.append(residuo)
   
    while len(stack) != 0:
        resultado += str(stack.pop())
    
    print(resultado)
    
def cambioBaseDecimal(numero, base):
    queue = []
    suma = 0;
    
    while numero > 0:
        residuo = numero % 10
        numero //= 10
        queue.append(residuo)
        
    for i in range(len(queue)):
        suma += queue.pop(0)*pow(base, i)
    
    return suma

def hexaCambioBaseDecimal(numero):
    numero = numero.upper()
    hexa = []
    suma = 0
    for i in numero:
        hexa.append(i)
        
    for j in range(len(hexa)):
        valor = hexa.pop()
        letra = valorLetras(valor)
        if (letra != 0):
            suma += letra*pow(16, j)
        else:
            suma += int(valor)*pow(16, j)
    
    print(str(suma))

def cambioBaseHexa(numero):
    stack = []
    resultado = ''
    
    while numero > 0:
        residuo = numero % 16
        numero //= 16
        stack.append(residuo)
        
    while len(stack) != 0:
        pop = stack.pop()
        cambio = valorNumero(pop)
        if cambio == '':
            resultado += str(pop)
        else:
            resultado += cambio
    
    print(resultado)

def valorLetras(letra):
    valor = 0
    if letra == 'A':
        valor = 10
    if letra == 'B':
        valor = 11
    if letra == 'C':
        valor = 12
    if letra == 'D':
        valor = 13
    if letra == 'E':
        valor = 14
    if letra == 'F':
        valor = 15
    return valor 

def valorNumero(numero):
    letra = ''
    if numero == 10:
        letra = 'A'
    if numero == 11:
        valor = 'B'
    if numero == 12:
        letra = 'C'
    if numero == 13:
        letra = 'D'
    if numero == 14:
        letra = 'E'
    if numero == 15:
        letra = 'F'
    return letra

original = input('Ingrese el numero original:')
baseO = input('Ingrese la base del numero original:')
baseD = input('Ingrese la base a la cual quiere convertir el numero original:')

if baseO == '10' or baseO == '16' or baseD == '10' or baseD == '16': 
    
    if baseO == '10' and baseD != '16':
        cambioACualquierBase(int(original),int(baseD))
    
    if baseD == '10' and baseO != '16':
        print(str(cambioBaseDecimal(int(original), int(baseO))))

    if baseD == '16' and baseO != '10': 
        Bdecimal = cambioBaseDecimal(int(original), int(baseO))
        cambioBaseHexa(Bdecimal)

    if baseD == '16' and baseO == '10':
        cambioBaseHexa(int(original))
    
    if baseO == '16' and baseD != '10':
        Bdecimal = hexaCambioBaseDecimal(original)
        cambioACualquierBase(Bdecimal,int(baseD))
    
    if baseO == '16' and baseD == '10':
        print(str(hexaCambioBaseDecimal(original)))
        
else:
    Bdecimal = cambioBaseDecimal(int(original), int(baseO))
    cambioACualquierBase(Bdecimal,int(baseD))
    
