from errbot import BotPlugin, botcmd


class Labirinto(BotPlugin):
    """
    Jogo de labirinto feito em matriz de números inteiros.
    O objetivo é fazer com que o jogador saia do labirinto,
    e para isso será preciso movimentar-se pelas salas e
    corredores.
    Internamente, o jogo implementa uma matriz de inteiros
    para armazenar informações como:
    - Parede: 1
    - Sala ou corredor: 0
    - Posição e sentido do jogador:
      -  2: sentido Norte
      -  4: sentido Sul
      -  8: sentido Oeste
      - 16: sentido Leste
    Assim, o mapa acumula informações com base nessas
    potências de dois, como por exemplo:
    8 = 8 + 0 = jogador no sentido Oeste + sala ou corredor    
    """

    mapa_inteiros = [[1, 1, 1, 8, 1],
                     [1, 0, 0, 0, 1],
                     [1, 0, 0, 1, 1],
                     [1, 1, 0, 0, 1],
                     [1, 1, 1, 0, 0]]

    @botcmd
    def mapa(self, msg, args):
        """
        Apresentar o mapa do bot.
        """
        
        for linha in self.mapa_inteiros:
            yield " ".join(map(str, linha))