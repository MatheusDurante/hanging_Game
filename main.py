#Matheus Durante - ra: 1134846
#gabriel gaio    - ra: 1134812

from funcoes import limparTela, aguarde, callInput,forca,quantidadeDeCaracter
import random
while True:
    limparTela()
    print("===---Bem Vindos ao Jogo Da Forca---===")
    print("(0) sair")
    print("(1) jogar")
    print("(2) historico de partidas")
    opcao = input()
    if opcao == "0":
        break
    elif opcao == "1":
        player1 = input("insira o nome do participante que vai adivinhar (min 3 caracter): ")
        caracter = player1
        quantidadeDeCaracter(len(caracter) )
        player2 = input("insira o nome do participante que vai incerir as palavras (min 3 caracter): ")
        caracter = player2
        quantidadeDeCaracter(len(caracter) )
        limparTela()
        palavra = callInput()
        while len(palavra) <= 3:
                print("não foi definido uma palavra")
                aguarde(2)
                palavra = callInput() 
        print("palavra definida com sucesso")
        aguarde(2)
        dica1 = input("coloque a primeira dica: ")
        caracter = dica1
        quantidadeDeCaracter(len(caracter) )
        dica2 = input("coloque a segunda dica: ") 
        caracter = dica2
        quantidadeDeCaracter(len(caracter) )
        dica3 = input("coloque a terceira dica: ")
        caracter = dica3
        quantidadeDeCaracter(len(caracter) )
        palavra = palavra.split(",")
        palavra = random.choice(palavra)
        erro = 6
        letras_adivinhadas = []
        while erro != 0:
            limparTela()
            palavra_oculta = ""
            for letra in palavra:
                if letra in letras_adivinhadas:
                    palavra_oculta += letra
                else:
                    palavra_oculta += "_"
            print(palavra_oculta)
            letra = input("Digite uma letra: ")
            if letra in  letras_adivinhadas:
                print("Você já tentou essa letra, tente outra.")
                aguarde(2)
                continue
            letras_adivinhadas.append(letra)
            if letra in palavra:
                print("Você acertou!")
                forca(erro)
                aguarde(2)
            else:
                print("Você errou!")
                erro -= 1
                forca(erro)
                aguarde(2)
            if set(palavra) == set(letras_adivinhadas):
                print("Parabéns, você ganhou!")
                aguarde(2)
                arquivo = open("bd.historico", "a")
                arquivo.write( "\n"+player1+ " venceu "+ player2)
                arquivo.close()
                erro = 0
    elif opcao == "2":
        try:
            arquivo = open("bd.historico", "r")
            dados = arquivo.read()
            print(dados)
            arquivo.close()
            aguarde(5)
        except:
            print("Nenhum dado encontrado")
            arquivo = open("bd.historico", "w")
            arquivo.close()
    else:
        print("Opção invalida")