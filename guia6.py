import math

#EJERCICIO 1
# 1)  
def imprimir_hola_mundo () -> None:
    print('hola mundo')
imprimir_hola_mundo ()
imprimir_hola_mundo ()
imprimir_hola_mundo ()

# 2)
def imprimir_un_verso() -> None:
    print ('esto''\n''es''\n''un''\n''verso')
imprimir_un_verso()

# 3) devuelve raiz de 2 con 4 decimales
def raiz_de_dos() -> float:
    return round(math.sqrt(2),4)

# 4) 
def factorial_de_dos() -> int:
    return 2

# 5)
def perimetro () -> float:
    # return 2 * 3.14
    return 2 * math.pi

a = perimetro()
print (a)
print (perimetro ())

#EJERCICIO 2
# 1)
def imprimir_un_saludo (nombre:str) -> str:
    print ('hola' + nombre)

# 2)
def raiz_de(numero:float) -> float:
    return math.sqrt(numero)

# 3) 
def farenheit_a_celcius(far:float) -> float:
    return (far - 32) * 0.555

# 4)
def imprimir_dos_veces_estribillo(estribillo:str) -> str:
    return estribillo * 2

# 5)
def es_multiplo_de (n:int , m:int) -> bool:
    return n % m == 0
 
# 6)
def es_par(n:int) -> bool:
    return es_multiplo_de (n , 2)

# 7) 
def cantidad_de_pizzas(comensales:int, porciones:int) -> int:
    return round((comensales*porciones) /8)  

# EJERCICIO 3
# 1)
def alguno_es_0(i:float , j:float) -> bool:
    return i==0 or j==0

# 2) 
def ambos_son_0(i:float ,  j:float) -> bool:
    return i==0 and j==0

# 3)
def es_nombre_largo (nombre:str) -> bool:
     return len(nombre) <= 8 and len(nombre) >= 3

def es_nombre_largo2 (nombre:str) -> bool:
    if len(nombre) >= 8 or len(nombre) <= 3:
        return False
    return True

# 4)    
def es_bisiesto(año:int) -> bool:
    return es_multiplo_de(año, 400) or es_multiplo_de(año,4) and not es_multiplo_de(año,100)

# EJERCICIO 4
# 1)
def peso_pino(altura:float) -> float:
    if altura <= 3:
        return altura*300
    else:
        return 900 + altura * 200
    
# 2) 
def es_peso_util(peso:float) -> bool:
    return peso>=400 and peso<=1000


# 3)4)
def sirve_pino(altura:int) -> bool:
    return es_peso_util (peso_pino (altura))

# EJERCICIO 5
# 1)
def devolver_doble_si_es_par (x:int) -> int:
    if x % 2 == 0:
        return x * 2
    return x

# 2)
def devolver_valor_si_par_sino_siguiente(x:int) -> int:
    if es_par(x):
        return x
    else:
        return x + 1

# 3)
def devolver_doble_si_multiplo3_triple_si_multiplo9(x:int) -> int:
    if es_multiplo_de(x,9):
        return x*3
    if es_multiplo_de(x,3):
        return x*2
    else:
        return x 
    
# 4)
def lindo_nombre(nombre:str) -> None:
    if len(nombre) >= 5:
        print('Tu nombre tiene muchas letras!')
    else:
        print('Tu nombre tiene menos de 5 caracteres')

# 5) 
def el_rango(n:int) -> None:
    if n<=5:
        print('Menor a 5')
    if n>=10 and n <= 20:
        print('Entre 10 y 20')
    else: 
        print('Mayor a 20')

# 6)
def quien_labura(edad:int, sexo:str) -> None:
    if edad<18:
        print('Te vas de vacaciones')
    if (edad >= 18 and edad > 60 and sexo == "Femenino") or (edad >= 18 and edad < 65 and sexo == "Masculino"):
        print('Agarrá la pala')
    else: 
        print('Te vas de vacaciones')

# EJERCICIO 6
# 1)
def imprimir_1_al_10() -> None:
    x: int = 1
    while x <= 10:
        print(x)
        x += 1

# 2)
def imprimir_numeros_pares() -> None:
    x: int = 10
    while x <= 40:
        print(x)
        x += 2

# 3)
def imprimir_eco() -> None:
    x: int = 1
    while x <= 10:
        print('Eco')
        x += 1

# 4) 
def cuenta_regresiva(n: int):
    while(n >= 1):
        print(n)
        n -= 1
    print("DESPEGUE")    

# 5) 
def viaje_tiempo(x:int, y:int) -> None:
    i: int
    while i < x:
        print(i + '\n''Viajó al año anterior') 
        i -= y

# EJERCICIO 7
# 1)
def imprimir_1_al_10_2() -> None:
    for x in range (1, 10+1, 1):
        print(x)

# 2)
def imprimir_numeros_pares2() -> None:
    for x in range(10, 40+1, 2):
        print(x)

# 3)
def imprimir_eco2() -> None:
    for x in range(1, 10+1, 1):
        print('Eco')

# 4) 
def cuenta_regresiva2(x:int) -> None:
    for i in range(x, 0, -1):
        print(i)
    print('DESPEGUE')

# 5) 
def viaje_tiempo2(x:int , y:int) -> None:
    i:int
    for i in range(x, y-1, -1):
        print (i + '\n''Viajó al año anterior')


# EJERCICIO 8
# 1)
print('1)')
x = 5 
print('x:',x)
y = 7 
x = x + y 
print ('x:' , x)

# 2) 
print('2)')
x = 5 
y = 7 
z = x + y
y = z * 2
print ('z:', z)
print ('y:',y)

# 3)
print('3)')
x = 5  
y = 7  
x = "hora" 
y = x * 2
print ('y:',y)

# 4)
print('4)')
x = False 
res = not(x)
print ('res:',res)

# 5)
print('5)')
x = True 
y = False 
res = x and y 
x = res and x
print ('res:', res)
print ('x:',x)

#EJERCICIO 9
def rt(x: int, g: int) -> int:
    g = g + 1
    return x + g

g: int = 0
def ro(x: int) -> int:
    global g
    g = g + 1
    return x + g

print('Ej 9')

print(ro(1))
print(ro(1))
print(ro(1))

print(rt(1,0))
print(rt(1,0))
print(rt(1,0))


