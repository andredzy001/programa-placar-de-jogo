TIMEA = input("Nome do primeiro time: ")
TIMEB = input("Nome do segundo time: ")
GOLA = int(input (f"Placar do time {TIMEA}: "))
GOLB = int(input(f" Placar do time {TIMEB}: "))
if GOLA > GOLB:
    print (f"O ganhador foi time {TIMEA} com {GOLA} gols")
elif GOLB > GOLA:
     print (f"O ganhador foi time {TIMEB} com {GOLB} gols")
elif GOLA == GOLB:
    print ("O jogo foi empatado")