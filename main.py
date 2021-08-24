1#Permite que o arquivo main acesse todo o conteudo presente na palavra e na interface.
# Os e  time são duas biblioteca responsaveis por: OS = limpar/time = dar uma pausa
# Ao utilizar o comando "as", vc consegue apelidar alguma coisa importada
import palavras as p 
import interface as f
import os
import time

#Inicializando e dando valor as variaveis do jogo
vida = 5
palavra = ""
palavra_resposta = ""
letras_usadas = [] #Utilizada para  mostrar na tela as letras ja usadas anteriormente pelo  usuario
pontuacao = 0
lista = []
qtd_letra = 0

## fim das variáveis

## definição das funções
def chanceUnica(palavra):
  global qtd_letra, pontuacao, vida
  for i in range (0,len(palavra)):
    if palavra[i] == "_":
      qtd_letra += 1
  print("Quantidade de acertos: ", qtd_letra)
  if qtd_letra >= len(palavra)//2:
    print("+++ Chance Única +++")
    chance = print("Gostaria de participar do modo chance unica? [s] para sim e [n] para não: ")
    if chance == "s":
      vida == 1
      p_completa = input("Digite a palavra completa, você só tem uma chance: ")
      if p_completa == palavra_resposta:
        pontuacao += 15
        print("Parabéns, você acertou a palavra no modo Chance Única e ganhou 15 pontos!")
        return True
      else:
        vida == 0
        pontuacao -= 5
        print("Você errou a palavra e perdeu 5 pontos")
    else:
      return False


def start():
    global palavra, palavra_resposta, pontuacao # Seta as variaveis como globais para assim  poder mexer no valor delas.
    palavra = p.palavraSecreta() # Seleciona uma palavra da lista presente na palavras.py
    palavra_resposta = p.palavraResposta(palavra) #Setar a palavra secreta como a palavra resposta
    while(True):
        os.system('clear')
        print("Letras digitadas: ")
        print(letras_usadas)
        print("Vidas restantes: ", vida)
        f.painel(palavra_resposta)
        if (vida == 0 or p.veriwin(palavra_resposta) == True):
            break
        play()
        chanceUnica(palavra)

        #colocar após jogar uma letra
        
    if vida < 1:
      print("Você perdeu e será encaminhado ao menu inicial =(")
      nome = input("Digite seu nome: ")
      lista.append(nome)
      lista.append(pontuacao)
    else:
      print("Você ganhou e uma nova partida será iniciada =)")
      time.sleep(3)
      pontuacao += 5
      start() 
      play()


def play():
  global vida, palavra_resposta, letras_usadas
  letra = input("Digite uma letra: ")
  if len(letra) == 1: # Verifica se só foi digitada uma letra
    letras_usadas.append(letra) # Coloca a letra digitada pelo usuario na lista de  letras usadas que futuramente vao ser impressas na tela
    acertos = p.verificacao(palavra, letra) #Verifica se a letra está na palavra
    chanceUnica(palavra)
    if len(acertos) == 0: # Caso ela não esteja, essa condicional é ativada
      vida -= 1 # Vai retirar uma  vida do usuário ja que a letra digitada nao constava na palavra
      print("Infelizmente não existe essa letra na palavra secreta =(, voce ainda tem", vida, "chances") 
      time.sleep(0.8)
    else:
      palavra_resposta = p.colocaLetra(palavra, palavra_resposta, acertos)
  else:
    print("Só é permitido uma letra por vez, insira novamente!")
    time.sleep(3)

    
# função principal
def main():
  global nome, vida
  while(True):
    opc = int(input("Escolha uma das opções, sendo [1] Nova partida, [2] Pontuações, [3] Sair: "))
    if opc == 1:
      vida = 5
      start()
      
    if opc == 2:
      print(" +++++ Jogadores e suas pontuações +++++ ")
      print(lista)
      break
    if opc == 3:
      print("Programa finalizado!!")
      break
# fim das declarações das funções

# começa executar daqui 
main()

# fim do programa

