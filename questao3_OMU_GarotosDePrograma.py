'''
Este programa foi desenvolvido para ser uma ferramenta de resolução da questão 3, itens (b), (c), (d), da primeira fase
da Olimpíada de Matemática da Universidade Estadual de Campinas (OMU) nível Beta 
'''

'''
(b) Quantas soluções inteiras tem a equação?
'''

divisores = []

#Calculando os divisores positivos de x:
for i in range(1,int(math.sqrt(128))):
    if 128 % i == 0
        divisores.append(i)

# Perceba que se a | 1008 (a ∈ Z, a ≠ 0), então -a | 1008. Ou seja, devemos também considerar os divisores negativos de 1008:
for i in divisores:
    divisores.insert(0, -i)

# Note que (x + 5) | 1008. Isso implica que x + 5 ≠ 0 => x  ≠ -5. Assim, calculando os valores possíveis de x a partir dos divisores de 1008:
x = []

for i in divisores:
    x.append(i-5)

    if (i-5 == 0)
        print("Alerta! O divisor", i, "gera valor 0 na divisão!")

# Por fim, tendo todos os valores de x alocados em uma lista, podemos utilizar o método 'len()', para descobrir a quantidade de soluções!
print("(b) x possui", len(x), "valores possíveis, ou seja, a equação possui", len(x), "soluções!")

'''
(c) Encontre todas as soluções inteiras da equação nas quais x é um número primo.
'''

# Para isso, basta varrer a lista que contem os valores de x em busca de números primos (lembrando que, para ser primo, o número deve ser positivo!):
xPrimos = []

def checaSePrimo (num):
    if num <= 1:
        return false

    for i in range(2, int(sqrt(num))):
        if num % i == 0:
            return false

    return true

for i in x:
    if checaSePrimo(num) == true:
        xPrimos.append(num)

# Como a pergunta pede para que ENCONTREMOS todas as soluções, vamos também encontrar os valores de y a partir de x, conforme descrito na solução:
solucoesC = []

def encontraY (x):
    y = (8*x**3 - x - 13)/(x+5)

    solucoesC.append((x,y))

# Assim, temos todos as soluções (x,y) em que x é um número primo! São elas:
for i in solucoesC:
    print(i)

'''
(d) Encontre todas as soluções inteiras da equação nas quais x e y são inteiros negativos.
'''

# Para isso, vamos calcular, dentre todas as soluções inteiras, aquelas que tem os valores de x e y negativos. Note que, se x+5 < 0, y será positivo, conforme descrito na resolução.
solucoesNegativas = []

for i in x:
    if i+5 > 0:
        if(encontraY(i) < 0):
            solucoesNegativas.append((x,y))
            
# Dessa forma, temos todas as soluções inteiras, com (x, y) < 0. São elas:
for i in solucoesNegativas:
    print(i)

seq = [1, 2, 3, 4, 6, 7, 8, 9, 12, 14, 16, 18, 21, 24, 28, 36, 42, 48, 56, 63, 72, 84, 112, 126, 144, 168, 252, 336, 504, 1008]
seqNeg = [-1, -2, -3, -4, -6, -7, -8, -9, -12, -14, -16, -18, -21, -24, -28, -36, -42, -48, -56, -63, -72, -84, -112, -126, -144, -168, -252, -336, -504, -1008]

seqDiv = seqNeg + seq

for i in seqNeg:
    print(i-5)

for i in seq:
    print (i - 5)

seq2 = [-4, -3, -2, -1, 1, 2, 3, 4, 7, 9, 11, 13, 16, 19, 23, 31, 37, 43, 51, 58, 67, 79, 107, 121, 139, 163, 247, 331, 499, 1003]
xNEG =[-6,-7,-8,-9,-11,-12,-13,-14,-17,-19,-21,-23,-26,-29,-33,-41,-47,-53,-61,-68,-77,-89,-117,-131,-149,-173,-257,-341,-509,-1013]

for m in seq2:
    if m > 1:
    # Iterate from 2 to n // 2
        for i in range(2, (m//2)+1):
        # If num is divisible by any number between
            if (m % i) == 0:
                print(m, "is not a prime number")
                break
            else:
                print(m, "is a prime number")
    else:
        print(m, "is not a prime number")



seq3 = [2,3,7,11,13,19,23,31,37,43,67,79,107,139,163,331,499]

for i in seq3:
    y = (8*i**3 - i - 13)/i+5
    
    print((i,y))

for i in xNEG:
    y = (8*i**3 - i - 13)/i+5
    
    print((i,y))    

'''
2 is a prime number
3 is a prime number
7 is a prime number
11 is a prime number
13 is a prime number
19 is a prime number
23 is a prime number
31 is a prime number
37 is a prime number
43 is a prime number
67 is a prime number
79 is a prime number
107 is a prime number
139 is a prime number
163 is a prime number
331 is a prime number
499 is a prime number

(2, 7)
(3, 25)
(7, 227)
(11, 664)
(13, 975)
(19, 2285)
(23, 3475)
(31, 6619)
(37, 9647)
(43, 13250)
(67, 33417)
(79, 46955)
(107, 87502)
(139, 149200)
(163, 206225)
(331, 863444)
(499, 1972245)
'''