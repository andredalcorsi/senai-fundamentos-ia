'''

18. Leia uma palavra ou frase e informe se ela é um palíndromo (lê-se igual nos dois sentidos).
Ignore espaços e diferença entre maiúsculas e minúsculas.

DICA: normalize primeiro (minúsculas, sem espaços), depois compare o texto com o seu reverso.

'''

escrito = str(input('Digite a palavra para comparar: '))

noSpace = escrito.split()

