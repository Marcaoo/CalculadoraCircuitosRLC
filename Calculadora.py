# -*- coding: utf-8 -*-
"""
Created on Thu May  8 13:13:59 2025

@author: Marcão
"""

import math
import os
import time

def limpa_tela():
    time.sleep(3)
    os.system('cls')
    menu()

def rlc_serie():
    r = float(input('Digite o valor de resistência: '))
    l = float(input('Digite o valor de indução: '))
    c = float(input('Digite o valor de capacitância: '))
    f = int(input('Digite o valor da frequência em hz: '))
          
    xl = 2 * math.pi * f * l
    xc = 1 /(2* math.pi * f * c)
    z = math.sqrt(r**2 + (xl -xc)**2)
    
    print(f'O valor de impedância do circuito RLC-Série é de: {z}Ohm')
    limpa_tela()
    
def rlc_paralelo():
    r = float(input('Digite o valor de resistência: '))
    l = float(input('Digite o valor de indução: '))
    c = float(input('Digite o valor de capacitância: '))
    f = int(input('Digite o valor de frequência: '))

    xl = 1/(2 * math.pi * f * l)
    xc = 2 * math.pi * f * c
    z = 1/math.sqrt((1/r**2) + (xl-xc)**2)    
    
    print(f'O valor de impedância do circuito RLC-Série é de: {z}Ohm')
    limpa_tela()
    
def menu():
    print(28*'*')
    print('CALCULADORA DE CIRCUITOS RLC')
    print(28*'*')
    
    print('Tipos de circuitos: ')
    print('1-RLC série')
    print('2-RLC paralelo')
    
    escolha = int(input('Escolha a opção que deseja: '))
    
    if escolha == 1:
        rlc_serie()
    elif escolha ==2:
        rlc_paralelo()
    else:
        print('Opção inválida!')
        limpa_tela()    
menu()