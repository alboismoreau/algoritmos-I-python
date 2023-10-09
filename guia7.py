import math
# EJERCICIO 1
# 1)
def pertenece(s:[int],e:int) -> bool:
  for i in s:
     if i == e:
        return True
     else:
        return False

# 2)
def divide_a_todos(s:[int], e : int) -> bool:
   for i in s:
      if not i % e == 0:
         return False
      else:
         return True

# 3)
def suma_total(s:[int]) -> int:
    total:int = 0
    indice: int = 0
    while indice < len(s):
       total += s[indice]
       indice += 1
       return total

def suma_total2 (s:[int]) -> int:
   for elemento in s:
      total= total + elemento
      return total
   
# 4)
def ordenados(s:[int]) -> bool:
    indice: int = 0 
    while indice < len(s) - 1 and s[indice] < s[indice +1]:
      indice += 1
    return indice == len(s) -1
   

def ordenados2(s:[int]) -> bool:
   for i in range (len(s) - 1 ):
      if not s[i] < s [i+1]:
         return False
      else:
       return True

         
#5)
def lista_palabras (l:[str]) -> bool:
   for palabra in l:
      if len(palabra) > 7:
         return True
      else: 
         return False

# 6)
def inversa (s:str) -> str:
   palabra_inverida: str= ""
   i = len(s) -1 
   while i >= 0:
      palabra_inverida += s[i]
      i -= 1
      return palabra_inverida

def palindromo(texto:str) -> bool:
   if texto == inversa (texto):
      return True
   else:
      return False

# 7)
def hay_mayuscula(contra:str) -> bool:
   for letra in contra:
      if 'A' <= letra <= 'Z':
         return True
      return False
   
def hay_minuscula(contra:str) -> bool:
   for letra in contra:
      if 'a' <= letra <= 'z':
         return True
      return False

def hay_digito (contra:str) -> bool:
   for letra in contra:
      if '0' <= letra <= '9':
         return True
      return False

def fortaleza_contra(contra:str) -> str:
   if len(contra) < 5:
      return 'ROJA'
   if len(contra) > 8 and hay_minuscula(contra) and hay_mayuscula(contra) and hay_digito(contra):
      return 'VERDE'
   else:
      return'AMARILLA'

# 8)
def cuenta_bancaria(historial:[(str,int)]) -> int:
   saldo : int = 0
   for t in historial:
      if t[0] == 'I':
         saldo += t[1]
      if t[0] == 'R':
         saldo -= t[1]
         return saldo
    
# 9)
def tresVocalesDistintas(palabra:str) -> bool:
   tieneA = 0
   tieneE = 0
   tieneI = 0
   tieneO = 0
   tieneU = 0
   for letra in palabra:
      if letra == 'A' or 'a':
         tieneA = 1
      if letra == 'E' or 'e':
         tieneE = 1
      if letra == 'I' or 'i':
         tieneI = 1
      if letra == 'O' or 'o':
         tieneO = 1
      if letra == 'U' or 'u':
         tieneU = 1
         return tieneA + tieneE + tieneI + tieneO + tieneU >= 3

    
      
#EJERCICIO 2
# 1) 
def borra_posiciones_pares(lista:[int]) -> None: 
   for i in range (0, len(lista), 2):
      lista[i] = 0
    
      