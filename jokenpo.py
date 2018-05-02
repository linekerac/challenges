# -*- coding: utf-8 -*-

def menu():
    print('##### JOKENPÔ #####\n'
          '* [1] -> Pedra;   *\n'
          '* [2] -> Papel;   *\n'
          '* [3] -> Tesoura; *\n'
          '###################')

def juiz(x, y):
    if x == 1: #Pedra
        if y == 1: #Pedra
            print("Empate!")
        elif y == 2: #Papel
            print("Vencedor: Jogador 2!")
        elif y == 3: #Tesoura
            print("Vencedor: Jogador 1! ")
    elif x == 2: #Papel
        if y == 1: #Pedra
            print("Vencedor: Jogador 1!")
        elif y == 2: #Papel
            print("Empate!")
        elif y == 3: #Tesoura
            print("Vencedor: Jogador 2!")
    elif x == 3: #Tesoura
        if y == 1: #Pedra
            print("Vencedor: Jogador 2!")
        elif y == 2: #Papel
            print("Vencedor: Jogador 1!")
        elif y == 3: #Tesoura
            print("Empate!")
menu()
print()
jog1 = int(input("Jogador 1: "))
jog2 = int(input("Jogador 2: "))
print()
juiz(jog1, jog2)



