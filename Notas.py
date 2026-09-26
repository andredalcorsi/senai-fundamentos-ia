'''Comentários de várias linhas

print('Bem vindo ao SENAI')
#Operações matemáticas
print (2+5) #Soma
print (10-12) #Subtração
print (8*10) #Multiplicação
print (10/5) #Divisão
print (83//5) #Resultado da divisão inteira
print (41%2)  #Resto da divisão inteira
print (9**5) # Exponenciação
print ((9+3)*(8/8))

soma_idades = 0
for i in range(4):
    idade=int(input('Idade: ))
    soma_idades += idade   #Qundo incluo o + na frente do igual, é como se tivesse colocado a variável + alguma coisa (soma_idades = soma_idades + idade
--------------------------------------------------------
#Variáveis

nome = 'Samiramis Gabriel'
idade = 36

print(f'Bem vinda {nome}, com {idade} anos')

--------------------------------------------------------
# Entrada de dados
nome= input('Digite seu nome: ')
print(f'Bem vinda, Sra. {nome}')


#Escreva um programa que receba 2 números e realize a sua soma

num1 = int(input('Digite o 1º número da soma: '))
num2 = int(input('Digite o 2º número da soma: '))
soma = num1 + num2
print(f'A soma de {num1} + {num2} é igual a {soma}')

--------------------------------------------------------

#Exercícios
##Calculando direto na resposta
real = float(input('Insira o valor em Reais: '))

## Escrever em 2 linhas sem escrever 2 linhas de print e arredondamento dos números
print(f'Volume da esfera: {Volume:.2f}\nÁrea da esfera: {round(Area,2)}')

-----------------------------------------------------------
#Strings

Senai = 'Luis Eulálio'

##Fatiamento
print(Senai[0]) #Apresenta o caractere da posição definida
print(Senai[3:7]) #Apresenta os caracteres de um range de posições
print(Senai[3:]) #Apresenta todos caracteres a partir da posição inicial
print(Senai[:7]) #Apresenta todos caracteres até a posição definida
print(Senai [3:10:2])   #Apresenta os caracteres das posições definidas pulando de 2 em 2

##Análises
print(len(Senai)) #Conta Quantidade de caracteres
print(Senai.count('l')) #Conta a frequência de um determinado caractere
print(Senai.find('l'))  #Onde está o 1º 'l'
print(Senai.rfind('l')) # Onde está o último 'l'


#Transformação
print(Senai.replace('l','p')) #Alterar o caracter por outra coisa
print(Senai.upper()) #Maiúscula
print(Senai.lower()) #Minúscula
print(Senai.capitalize()) #primeiras letras maiúsculas

nome = input('Nome: ').strip() #Tira os espaços antes e depois
print(nome)

#para escrever todos os símbolos, basta clicar em Alt + código dele (tabela disponível no Google)

-----------------------------------------------------------------
#Condicionais
#1
altura = float(input('Altura: '))

if altura > 1.2:
    print('Pode entrar no brinquedo!')
else:
    print('Não pode entrar no brinquedo!')

#2
altura = float(input('Altura: '))
peso = float(input('Peso: '))

if altura > 1.2 and peso < 120:
    print('Pode entrar no brinquedo!')
else:
    print('Não pode entrar no brinquedo!')

--------------------------------------------------------------------

#Loop For

#1
for contador in range(1,100): #99 repetições - Se quiser 100, tem que colocar 101
    print('*')

#2
import time
for i in range (1,11):
    print(i) #Utilizo minha variável auxiliar para printar
    time.sleep(1)

#3
for i in range (10,0,-1): #o terceiro é o índice que vai andar o for
    print(i)

#4
soma = 0
for i in range (1,11): 'for i in range (10):
    n=int(input('N: '))
    soma = soma + n

print (f'A soma é: {soma}' e a média é {soma/10})

-------------------------------------------------------------------------
# While

#1
i = 0
while i < 5:
    print('Bem vindo ao SENAI!')
    i += 1

#2
resposta = 'S'
while resposta != 'N':
    print('Bem vindo ao SENAI!')
    resposta = input('Deseja continuar? [S/N] ').strip().upper()[0]

--------------------------------------------------------------------------------
# While True


#1
while True:
    print('Bem vindo ao Senai')
    n = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if n == 'N':
        break
#2
while True:
    print('-' *20) #Dar 20 hífens para dar um espaçamento entre as linhas
    menu = int(input('1. Oi'
                     '\n2. Olá'
                     '\n3. Sair -->'))
    if menu == 1:
        print('Oi')
    elif menu == 2:
        print('Olá')
    elif menu == 3:
        break
    else:
        print('Opção Inválida')

--------------------------------------------------------------------------------
#Try - Tratamento de erros

try:
    n1 = int(input('Insira 1 número: '))
    n2 = int(input('Insira outro número: '))
    x = n1/n2
    print(f'{n1} / {n2} = {x}')
except ZeroDivisionError:
    print('Não podemos dividir nada por zero!')
except ValueError:
    print('Só aceitamos números')

----------------------------------------------------------------------------------
#Funções - Nada mais é que criação de código que poder reutilizado (Bibliotecas)
# Para ler o código da função de uma biblioteca basta clicar encima da função com o Crtl
def quebra_linha():
    print('*************')

def mensagem(x):
    quebra_linha()
    print(x)
    quebra_linha()

print(mensagem('Bem Vindo'))

def area(x, y):
    return x * y

print(f'{area(30,10)} m2')

def volume(x, y, z):
    return area(x, y) * z

print(volume(8,6,4))

def media(*a): #Lê quantas variáveis forem digitadas
    return(a)

print (10,9,7,6,8)

----------------------------------------------------------------------------------
#Tuplas, Listas, Listas aninhadas e Dicionários

#Tuplas - Nunca pode ser editada
#()
carro = ('Ferrari', 'Vermelha', 2026)

#Fatiamento
print(carro[1])
print(carro[0:2])
print(carro[-1])

#Iteração
for i in carro:
    print(i)

for i in range(0, len(carro)):
    print(carro[i])

print(enumerate(carro)) #Enumerate é uma função que retorna o índice e o conteúdo da Tupla

for posicao, caracteristica, in enumerate(carro):
    print(f'{posicao} - {caracteristica}')

idades = (5,9,10,58,6,60,77,90,50)

print(max(idades))
print(min(idades))
print(sum(idades))
print(sum(idades)/len(idades))
print(sorted(idades))
print(sorted(idades, reverse=True))

----------------------------------------------------------------------------------
#Listas
#CRIANDO UMA lISTA:
carro = ['Ferrari', 'Vermelha', 2026]

#ALTERANDO UMA LISTA:
carro[1] = 'Amarelo'

#Adicionando uma coluna na lista:
carro.insert(1,'Gasolina') #Adiciona no meio na lista
carro.append('979 CV') #Adiciona no final da lista

#Remove posição:
carro.pop(7) #Remove a coluna desejada
carro.remove('Gasolina') #Remove a coluna que tem a informação

print(carro)

#Entrada de dados pelo usuário:
lista_idades = []

for i in range(5):
    lista_idades.append(int(input('N:')))

print(lista_idades)

#Cópia de listas

a = [1,2,3]
b = a #Se fixar assim, sempre que a lista A ou B forem alteradas, também vai alterar na outra lista
#Se o objetico é copiar a lista para continuar editando posteriomente, o ideal é fazer assim:
c = a[:]

b.append(4)
c.append(5)

print(a)
print(b)
print(c)

----------------------------------------------------------------------------------
#Listas aninhadas

#Formato Linha
Alunos = [['Maria', 22], ['João', 53], ['Thiago', 32]]

#Acesso aos dados
for i in Alunos:
    print(i)

print(Alunos[1]) #Para mostrar todos os dados da Maria
print(Alunos[1][0]) #Para mostrar apenas o nome da Maria
print(Alunos[1][0][0]) #Para mostrar apenas a primeira letra do nome da Maria

#Criando nova lista somente com o nome:
lista_nomes = []

for i in Alunos:
    lista_nomes.append(i[0])

print(sorted(lista_nomes))
-----------------------------
#Com input:
Alunos = []
dados = []

for i in range(3):
    dados.append(input('Nome: '))
    dados.append(int(input('Idade: ')))
    Alunos.append(dados[:])
    dados.clear()

    print(Alunos)

-----------------------------

# Formato Coluna
Alunos = [['Maria', 'João', 'Thiago'], [22, 53, 32]]

print(sum(Alunos[1])/3)
#Nesse formato é possível calcular sem precisar ficar procurando os dados na lista

#-----------------------------
#Com input:
# Formato 1
Nomes = []
Idades = []
Alunos = []

for i in range(3):
    Nomes.append(input('Nome: '))
    Idades.append(int(input('Idade: ')))

print(Alunos)

# Formato 2
Alunos = [[],[]]

for i in range (3):
    Alunos[0].append(input('Nome: '))
    Alunos[1].append(int(input('Idade: ')))

print(Alunos)
----------------------------------------------------------------------------------

from Tupla import quebra_linha

#Dicionários

df = {'Nome':'Luis Tatin','Idade': 45}

print(df['Nome']) #Acesso à informação

df['Sexo'] = 'M' #Inserir informação

del df['Idade'] #Remover informação

#Mostrar dados
print(df) #Retorna a estrutura completa
print(df.values()) #Retorna apenas os valores
print(df.keys()) #Retorna apenas as chaves
print(df.items()) #Retorna a estrutura completa

#Itera os valores em sequência
quebra_linha()
for i in df.values():
    print(i)

#-----------------------------
#Lista com dicionários

df = [{'Marca': 'A', 'Modelo': 'X', 'Ano': 2000},
      {'Marca': 'B', 'Modelo': 'Y', 'Ano': 2001},
      {'Marca': 'C', 'Modelo': 'Z', 'Ano': 2002}]

df = []
carro = {}

try:
    for i in range(3):
        carro['Marca'] = input('Marca: ')
        carro['Modelo'] = input('Modelo: ')
        carro['Ano'] = int(input('Ano: '))

        df.append(carro.copy())

    print(df)
except ValueError:
    print('Só aceitamos números.')

# Dicionário com listas

df = {'Marca': ['A', 'B', 'C'],
      'Modelo': ['X', 'Y', 'Z'],
      'Ano': [2000, 2001, 2002]}

print(f'A média é {sum(df['Ano'])/len(df['Ano'])}')

#Exemplo manual

df = {}
#Input do dicionário com 1 linha:
df['Marca'] = [input('Marca: ') for i in range(3)]
df['Modelo'] = [input('Modelo: ') for i in range(3)]
df['Ano'] = [input('Ano: ') for i in range(3)]

for i, j in df.items():
    print(f'{i} - {j}')

#Exemplo compatível:
marcas = []
for i in range(3):
    marca.append('Digite a marca: ')

df['Marca'] = marcas[:]

'''
