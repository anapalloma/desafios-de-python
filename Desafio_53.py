# -*- coding: utf-8 -*-
"""Desafio_53.ipynb

**Desafio 53** - Crie um programa que leia uma frase qualquer e diga se ela é um palíndormo, desconsiderando os espaços.
"""

frase = str(input('Digite uma frase: ')).upper().strip().split()
tratado = ''.join(frase)
inverso = tratado[len(tratado)::-1]

print(f'\nO inverso de {tratado} é {inverso}')
if (tratado == inverso):
  print('A frase digitada é um palíndromo!')
else:
  print('A frase digitada não é um palíndromo!')
