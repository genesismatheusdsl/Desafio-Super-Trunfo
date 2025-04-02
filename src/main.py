# main.py - Jogo Super Trunfo

# Importação das bibliotecas necessárias
import random

# Definição das classes e estruturas de dados
class Carta:
    def __init__(self, nome, atributo1, atributo2, atributo3):
        self.nome = nome
        self.atributos = {
            "Força": atributo1,
            "Velocidade": atributo2,
            "Inteligência": atributo3
        }

    def mostrar_carta(self):
        print(f"\nCarta: {self.nome}")
        for chave, valor in self.atributos.items():
            print(f"{chave}: {valor}")

# Função para jogar uma rodada
def jogar_rodada(carta1, carta2, atributo_escolhido):
    valor1 = carta1.atributos[atributo_escolhido]
    valor2 = carta2.atributos[atributo_escolhido]

    print(f"\n{carta1.nome} tem {atributo_escolhido}: {valor1}")
    print(f"{carta2.nome} tem {atributo_escolhido}: {valor2}")

    if valor1 > valor2:
        print(f"{carta1.nome} venceu esta rodada!")
        return 1
    elif valor1 < valor2:
        print(f"{carta2.nome} venceu esta rodada!")
        return -1
    else:
        print("Empate!")
        return 0

# Função principal do jogo
def main():
    # Criando cartas de exemplo
    carta1 = Carta("Dragão", 90, 60, 50)
    carta2 = Carta("Tigre", 70, 80, 40)

    # Mostrar as cartas antes da rodada
    carta1.mostrar_c_
