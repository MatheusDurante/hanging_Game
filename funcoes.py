import os
import time 

def limparTela():
    os.system("cls")

def aguarde(segundos=1):
    time.sleep(segundos)

def quantidadeDeCaracter(caracter):
    while caracter <= 3:
        print("escrita invalida")
        aguarde(2)
        caracter = len(input("escreva uma palavra valida: "))
    print("palavra definida com sucesso")
    aguarde(2)
    
def callInput():
    return input("defina a palavra com no mínimo 3 caracteres: ")

def forca (erro):
    from main import dica1, dica2, dica3,player1,player2
    if erro == 6:
        print(" +---+")
        print("     |")
        print("     |")
        print("     |")
        print("    ===")
    elif erro == 5:
        print(" +---+")
        print(" o   |")
        print("     |")
        print("     |")
        print("    ===")
    elif erro == 4:
        print(" +---+")
        print(" o   |")
        print(" |   |")
        print("     |")
        print("    ===")
        print("dicas:")
        print(dica1)
    elif erro == 3:
        print(" +---+")
        print(" o   |")
        print("/|   |")
        print("     |")
        print("    ===")
        print("dicas:")
        print(dica1)
    elif erro == 2:
        print(" +---+")
        print(" o   |")
        print("/|\  |")
        print("     |")
        print("    ===")
        print("dicas:")
        print(dica1)
        print(dica2)
    elif erro == 1:
        print(" +---+")
        print(" o   |")
        print("/|\  |")
        print("/    |")
        print("    ===")
        print("dicas:")
        print(dica1)
        print(dica2)
        print(dica3)
    elif erro == 0:
        print(" +---+")
        print(" o   |")
        print("/|\  |")
        print("/ \  |")
        print("    ===")
        print("--- Você perdeu!!! ---")
        arquivo = open("bd.historico", "a")
        arquivo.write("\n"+ player2+ " venceu "+ player1)
        arquivo.close()