# trabalho 1
import random 
import numpy as np

class JogoVelha:
    def __init__(self) -> None:
        self.tabuleiro = Tabuleiro()
        self.jogador_hum = JogadorHumano('X')
        self.jogador_maq = JogadorComputador('O', self.tabuleiro)
        self.turno = 0
    
    def jogar(self) -> None:
        while True:
            self.tabuleiro.imprimir_tabuleiro()
            resultado = self.fim_de_jogo()
            
            if resultado:
                print(f'O vencedor é {self.jogador_atual().simbolo}')
                break
            
            elif self.tabuleiro_cheio():
                print('Empate')
                break
            
            else:
                jogador = self.jogador_atual()
                linha, coluna = jogador.fazer_jogada()
                self.tabuleiro.marcar_tabuleiro(linha, coluna, jogador.simbolo)
                self.turno += 1
    
    def fim_de_jogo(self) -> bool:
        jogador = self.jogador_atual()
        casas = self.tabuleiro.casas
        
        # Verifica se há três símbolos iguais em uma linha
        for linha in casas:
            if linha[0] == linha[1] == linha[2] == jogador.simbolo:
                return True
        
        # Verifica se há três símbolos iguais em uma coluna
        for coluna in range(3):
            if casas[0][coluna] == casas[1][coluna] == casas[2][coluna] == jogador.simbolo:
                return True
            
        # Verifica se há três símbolos iguais nas diagonais
        if (casas[0][0] == casas[1][1] == casas[2][2] == jogador.simbolo or
            casas[0][2] == casas[1][1] == casas[2][0] == jogador.simbolo):
            return True
    
        return False
    
    def tabuleiro_cheio(self) -> bool:
        # Verifica se todas as casas estão ocupadas
        for linha in self.tabuleiro.casas:
            for entrada in linha:
                if entrada == '.':
                    return False  
        return True  

    def jogador_atual(self):
        if self.turno % 2 == 0:
            return self.jogador_hum
        else:
            return self.jogador_maq 
        
class Tabuleiro:
    def __init__(self):
        self.casas = np.full((3,3), '.')
        
    def marcar_tabuleiro(self, linha: int, coluna: int, simbolo: str) -> None:
        if self.casas[linha][coluna] == '.':
            self.casas[linha][coluna] = simbolo  
            
    def imprimir_tabuleiro(self):
        print('\n')
        print(self.casas)
1
class Jogador:
    def __init__(self, simbolo: str) -> None:
        self.simbolo = simbolo
    
    def fazer_jogada(self) -> None:
        pass

class JogadorHumano(Jogador):
    def __init__(self, simbolo: str) -> None:
        super().__init__(simbolo)
        
    def fazer_jogada(self) -> tuple:
        linha = int(input('Indique a linha da sua jogada (0,1,2): '))
        coluna = int(input('Indique a coluna da sua jogada (0,1,2): '))
        return linha, coluna
        
class JogadorComputador(Jogador):
    def __init__(self, simbolo: str, tabuleiro: Tabuleiro) -> None:
        super().__init__(simbolo)
        self.tabuleiro = tabuleiro
        
    def fazer_jogada(self) -> tuple:
        while True:
            linha = random.randint(0, 2)
            coluna = random.randint(0, 2)
            if self.tabuleiro.casas[linha][coluna] == '.':
                return linha, coluna
            
# Instanciando objetos e iniciando o jogo
jogo_da_velha = JogoVelha()
jogo_da_velha.jogar()
