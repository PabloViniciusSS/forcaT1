# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 10:21:50 2022

@author: Pablo Vinícius
"""
import random

def loser(n, c):
    if n == c:
        ('você perdeu o jogo')
        
def win(i,j):
    if ''.join(status) == palavra:
        print("VocÊ venceu o jogo")

    
palavras = ["cao", "pao", "massa"]

palavra = random.choice(palavras)
print(palavra)


tentativa = 0

chance = 6

letra_escolhida = list()

status = ["_"] * len(palavra)

print(status)

while tentativa < chance and ''.join(status) != palavra:
        letra = str(input(" Digite uma letra: ")) 
        while letra in letra_escolhida:
            print("Você ja tentou essa letra")
            letra = str(input(" Digite uma letra: ")) 

        letra_escolhida.append(letra)
            
        
        if letra in palavra:
            print(" Você acerto a letra")
            for i in range(len(palavra)):
               if letra == palavra[i]:
                    status[i] = letra
            
        else:
            print('Você errou')
            tentativa += 1            
            print("Você ja fez ", tentativa, "VocÊ tem ", chance - tentativa)
        
        
        print('seu status é: ')
        print(status)

if tentativa == chance:
   print("Você perdeu")
else:
    print("VocÊ ganhou")
           
            
print(status)
      
    
            
              
    
    
    
  
    
            
        
        
