from  errbot  import  BotPlugin , botcmd
de  importação aleatória  randint 


classe  Dados ( BotPlugin ):
    "" "
    Rolar os dados para suporte a jogos de RPG de mesa.
    Tem o rolar de n dados com m faces, entre outros comandos.
    "" "

    @ botcmd ( split_args_with = '' )
    def  rolar ( self , msg , args ):
        "" "
        Informar quantos dados e faces.
        Forma de usar:
        ! rolar <dados> <faces>
        onde <dados> e <faces> são números inteiros.
        "" "

        tente :
            dados  =  int ( args [ 0 ])
            faces  =  int ( args [ 1 ])
        exceto :
            yield  "Por favor, informe os dados e faces como números inteiros"
            rendimento  "na seguinte forma:"
            rendimento  "! rolar <dados> <faces>"
        mais :
            somatorio  =  0
            para  parada  no  intervalo ( 1 , dados  +  1 ):
                dado  =  randint ( 1 , faces )
                somatorio  =  somatorio  +  dado
                rendimento  "Dado"  +  str ( parada ) +  "="  +  str ( dado )
            rendimento  "Somatório ="  +  str ( somatorio )