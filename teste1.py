# -*- coding: utf-8 -*-
"""Teste1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18xQflMBM5Syo0C05WU_KfO02BnssTShO
"""

import requests

def main():
  print('Nomython')

  nome = input('digite o nome para consulta: ') 

  
  request = requests.get('https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking'.format(nome))
  nomes = request.json()
  print('NOME:{}'.format(nomes[0]))

if __name__ == '__main__':
  main()



