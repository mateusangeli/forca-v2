import random
lista = ["computador", "caneta", "portugues", "madeira", "garrafa", "teclado", "papel"] 

def palavraSecreta():
  # Vai a armazenar a palavra escolhida aleatoriamente pelo random
    index = random.randint(0,len(lista)-1)
  # Vai enviar a palavra para onde a função palavraSecreta for chamada
    return lista[index]


def palavraResposta(palavra):
  # Vai criar uma lista vazia, pra armazenar as letras digitadas pelo usuario
    resposta = []
    for  i in range (0, len(palavra)):
      resposta.append("_") # Inserir um elemento na lista
    # Retorna a variavel resposta para onde a função palavraResposta for chamada
    return resposta 


def verificacao(palavra, letra): 
  # Responsável por conferir se a letra digitada, está presente na palavra
    acertos = [] # lista vazia dos index das letras da palavra da lista
    for i in range (0, len(palavra)): # Vai verificar letra por letra da palavra
      if palavra[i] == letra: #Verifica se a letra digitada tem na palavra
       acertos.append(i) # Se a letra digitada existir na palavra, adiciona ela na lista que antes era vazia
    return acertos # Retorna a variavel acertos para onde a função verificacao for chamada


def veriwin(p_resposta): 
    for i in range  (0, len(p_resposta)): # Vai verificar se todas as letras foram encontradas
      if p_resposta[i] == "_": # se ainda existir o caractere _ na palavra resposta, vai dar negativo,  ou seja nao foi completada ainda
        return False
    return True # caso nao encontra, retorna verdadeiro


# Vai verificar a palavra secreta, ver quais foram as letras acertadas e inserir elas na palavra resposta, eliminando os  _.
def  colocaLetra(p_secreta, p_resposta, acertos):
      for i in range (0,  len(acertos)):
          index = acertos[i] #Comando  responsavel por ver a posição em que a letra acertada está na palavra.
          p_resposta[index] = p_secreta[index]
      return p_resposta


