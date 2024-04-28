'''
Este programa foi desenvolvido para ser uma ferramenta de resolução da questão 3, itens (b), (c), (d), da primeira fase
da Olimpíada de Matemática da Universidade Estadual de Campinas (OMU) nível Beta 
'''

import math

'''
(b) Quantas soluções inteiras tem a equação?
'''

#Calculando os divisores positivos de x:
divisoresPositivos = []
for i in range(1, 1008+1):
    if 1008 % i == 0:
        divisoresPositivos.append(i)
        
print("Os divisores positivos de 1008 são:", divisoresPositivos)

# Perceba que se a | 1008 (a ∈ Z, a ≠ 0), então -a | 1008. Ou seja, devemos também considerar os divisores negativos de 1008:
divisoresNegativos = []        
for i in divisoresPositivos:
    divisoresNegativos.insert(0, -i)

print("Os divisores negativos de 1008 são:", divisoresNegativos)

# Assim, os divisores inteiros positivos e negativos de 1008 são:
divisores = divisoresNegativos + divisoresPositivos

# Note que (x + 5) | 1008. Isso implica que x + 5 ≠ 0 => x  ≠ -5. Assim, calculando os valores possíveis de x a partir dos divisores de 1008:
x = []

for i in divisores:
    x.append(i-5)
    if(i-5 == 0):
        print("ALERTA! DIVISÃO POR 0! (i =",i)

# Por fim, tendo todos os valores de x alocados em uma lista (x), podemos utilizar o método 'len()', para descobrir a quantidade de soluções!
print("\n(b) x possui", len(x), "valores possíveis, ou seja, a equação possui", len(x), "soluções! São elas:", x)

#Lembre-se que conforme definimos, y é inteiro se 1008/(x+5) for inteiro!

'''
(c) Encontre todas as soluções inteiras da equação nas quais x é um número primo.
'''

# Para isso, basta varrer a lista que contem os valores de x em busca de números primos (lembrando que, para ser primo, o número deve ser positivo!):
xPrimos = []

def checaSePrimo (num):
    if num <= 1:
        return False

    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False

    return True

for i in range(0,len(x)):
    if checaSePrimo(x[i]) == True:
        xPrimos.append(x[i])

# Como a pergunta pede para que ENCONTREMOS todas as soluções, vamos também encontrar os valores de y a partir de x, conforme descrito na solução:
solucoesC = []

def encontraY (x):
    y = (8*x**3 - x - 13)/(x+5)
    
    return y

for i in range(0, len(xPrimos)):
    x1 = xPrimos[i]
    y1 = encontraY(x1)
    #y sempre rerá um número inteiro! O método int() foi usado abaixo apenas para que o par não fique (x, y.0).
    solucoesC.append((x1,y1))

# Assim, temos todos as soluções (x,y) em que x é um número primo! São elas:
print("\n(c) As soluções inteiras da equação em que x é primo são:", solucoesC)
    
'''
(d) Encontre todas as soluções inteiras da equação nas quais x e y são inteiros negativos.
'''

# Para isso, vamos calcular, dentre todas as soluções inteiras, aquelas que tem os valores de x e y negativos. Note que, se x + 5 < 0, y será positivo, conforme descrito na resolução.
solucoesNegativas = []

for i in x:
    if i+5 > 0:
        y = encontraY(i)
        if(y < 0 and i < 0):
            solucoesNegativas.append((i,y))
            
# Dessa forma, temos todas as soluções inteiras, com (x, y) < 0. São elas:
print("\n(d)Soluções com x, y negativos:", solucoesNegativas)