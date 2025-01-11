# Tabuleiro inicial
tabuleiro = [" " for _ in range(9)]

# Função para exibir o tabuleiro
def imprimir_tabuleiro():
    print("|" + tabuleiro[0] + "|" + tabuleiro[1] + "|" + tabuleiro[2] + "|")
    print("|" + tabuleiro[3] + "|" + tabuleiro[4] + "|" + tabuleiro[5] + "|")
    print("|" + tabuleiro[6] + "|" + tabuleiro[7] + "|" + tabuleiro[8] + "|")

# Função para verificar se há um vencedor
def verificar_vencedor():
    # Combinações vencedoras (linhas, colunas, diagonais)
    combinacoes = [
        [0, 1, 2],  # Linha 1
        [3, 4, 5],  # Linha 2
        [6, 7, 8],  # Linha 3
        [0, 3, 6],  # Coluna 1
        [1, 4, 7],  # Coluna 2
        [2, 5, 8],  # Coluna 3
        [0, 4, 8],  # Diagonal principal
        [2, 4, 6],  # Diagonal secundária
    ]
    
    for combinacao in combinacoes:
        a, b, c = combinacao
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] and tabuleiro[a] != " ":
            return tabuleiro[a]  # Retorna "X" ou "O"
    return None  # Ninguém venceu ainda

# Função principal do jogo
def jogar():
    jogador_atual = "X"  # "X" começa
    jogadas_realizadas = 0  # Contador de jogadas

    while jogadas_realizadas < 9:  # Máximo de 9 jogadas (tabuleiro cheio)
        imprimir_tabuleiro()
        print(f"Jogador {jogador_atual}, é sua vez!")
        
        # Solicita a posição ao jogador
        try:
            posicao = int(input("Escolha uma posição (0-8): "))
            if posicao < 0 or posicao > 8:
                print("Posição inválida. Escolha um número entre 0 e 8.")
                continue
            if tabuleiro[posicao] != " ":
                print("Posição ocupada. Escolha outra.")
                continue
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        # Atualiza o tabuleiro
        tabuleiro[posicao] = jogador_atual
        jogadas_realizadas += 1

        # Verifica se há um vencedor
        vencedor = verificar_vencedor()
        if vencedor:
            imprimir_tabuleiro()
            print(f"Parabéns! O jogador {vencedor} venceu!")
            return

        # Alterna o jogador
        jogador_atual = "O" if jogador_atual == "X" else "X"

    # Se o tabuleiro está cheio e ninguém venceu, é empate
    imprimir_tabuleiro()
    print("Empate! O jogo terminou.")

# Inicia o jogo
jogar()

