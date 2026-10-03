'''
022. Leia uma palavra e um número de deslocamento; devolva a palavra cifrada, deslocando cada
letra no alfabeto. abc  com deslocamento 2 → cde

Dica: ord()  transforma letra em número e  chr()  faz o caminho de volta; use  % 26  para dar a volta
no alfabeto.
'''

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
lista_numeros = []

palavra = input("Digite a palavra: ")
deslocamento = int(input("Digite o deslocamento: "))



# Descobrir os números


#for letra in palavra:
 #   print(ord(letra) + deslocamento)
  #  lista_numeros.append(ord(letra) + deslocamento)

# Volta
#for n in lista_numeros:
 #   print(chr(n))




