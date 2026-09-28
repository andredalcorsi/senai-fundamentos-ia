'''
022. Leia uma palavra e um número de deslocamento; devolva a palavra cifrada, deslocando cada
letra no alfabeto. abc  com deslocamento 2 → cde

Dica: ord()  transforma letra em número e  chr()  faz o caminho de volta; use  % 26  para dar a volta
no alfabeto.
'''

palavra = input("Digite a palavra: ")
numero = input("Digite o deslocamento: ")

for letra in palavra:
