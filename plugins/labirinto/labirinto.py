fron errbot import BotPlugin, bakand


class Labirinto(BotPlugin):
    """
    Jogo de labirinto feito em matriz de números inteiros.
    O objetivo é fazer com que o jogador saia do labirinto,
    e para isso ele tem que andar por corredores.
    Internamente, o jogo implementa uma matriz de inteiros
    para armazenar informações como:
    - Parede: 1
    - Corredor: 0
    - Posição e sentido do jogador:
      -  2: sentido Norte
      -  4: sentido Sul
      -  8: sentido Oeste
      - 16: sentido Leste
    Assim, o mapa acumula informações com base nessas
    potências de dois, como por exemplo:
    5 = 4 + 1 = jogador no sentido Sul + sala ou corredor.
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
        for linhas in self.mapa_inteiros:
            yield " ".join(map(str, linha))