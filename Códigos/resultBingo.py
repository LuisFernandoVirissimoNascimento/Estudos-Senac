from Bingo import*

gameIsOver = False
def CheckForBingo():
    # 27 possibilities
    for result in range(1,12):
        match result:
            case 1:
                result = 0
                result += bList[0] + iList[0] + nList[0] + gList[0] + oList[0]
                if result == 0:
                    bList[0] = strike("      Bingo !     ")
                    iList[0] = strike("      Bingo !     ")
                    nList[0] = strike("      Bingo !     ")
                    gList[0] = strike("      Bingo !     ")
                    oList[0] = strike("      Bingo !     ")
                    PrintGrid()
                    print("BINGO !")
                    return True
            case 2:
                result = 0
                result += bList[1] + iList[1] + nList[1] + gList[1] + oList[1]
                if result == 0:
                    bList[1] = strike("      Bingo !     ")
                    iList[1] = strike("      Bingo !     ")
                    nList[1] = strike("      Bingo !     ")
                    gList[1] = strike("      Bingo !     ")
                    oList[1] = strike("      Bingo !     ")
                    PrintGrid()
                    print("BINGO !")
                    return True
            case 3:
                result = 0
                result += bList[2] + iList[2] + nList[2] + gList[2] + oList[2]
                if result == 0:
                    bList[2] = strike("      Bingo !     ")
                    iList[2] = strike("      Bingo !     ")
                    nList[2] = strike("      Bingo !     ")
                    gList[2] = strike("      Bingo !     ")
                    oList[2] = strike("      Bingo !     ")
                    PrintGrid()
                    print("BINGO !")
                    return True
            case 4:
                result = 0
                result += bList[3] + iList[3] + nList[3] + gList[3] + oList[3]
                if result == 0:
                    bList[3] = strike("      Bingo !     ")
                    iList[3] = strike("      Bingo !     ")
                    nList[3] = strike("      Bingo !     ")
                    gList[3] = strike("      Bingo !     ")
                    oList[3] = strike("      Bingo !     ")
                    PrintGrid()
                    print("BINGO !")
                    return True
            case 5:
                result = 0
                result += bList[4] + iList[4] + nList[4] + gList[4] + oList[4]
                if result == 0:
                    bList[4] = strike("      Bingo !     ")
                    iList[4] = strike("      Bingo !     ")
                    nList[4] = strike("      Bingo !     ")
                    gList[4] = strike("      Bingo !     ")
                    oList[4] = strike("      Bingo !     ")
                    PrintGrid()
                    print("BINGO !")
                    return True
            case 6:
                result = 0
                result += bList[0] + bList[1] + bList[2] + bList[3] + bList[4]
                if result == 0:
                    bList[0] = strike("      Bingo !     ")
                    bList[1] = strike("      Bingo !     ")
                    bList[2] = strike("      Bingo !     ")
                    bList[3] = strike("      Bingo !     ")
                    bList[4] = strike("      Bingo !     ")
                    PrintGrid()
                    print("BINGO !")
                    return True
            case 7:
                result = 0
                result += iList[0] + iList[1] + iList[2] + iList[3] + iList[4]
                if result == 0:
                    iList[0] = strike("      Bingo !     ")
                    iList[1] = strike("      Bingo !     ")
                    iList[2] = strike("      Bingo !     ")
                    iList[3] = strike("      Bingo !     ")
                    iList[4] = strike("      Bingo !     ")
                    PrintGrid()
                    print("BINGO !")
                    return True
            case 8:
                result = 0
                result += nList[0] + nList[1] + nList[2] + nList[3] + nList[4]
                if result == 0:
                    nList[0] = strike("      Bingo !     ")
                    nList[1] = strike("      Bingo !     ")
                    nList[2] = strike("      Bingo !     ")
                    nList[3] = strike("      Bingo !     ")
                    nList[4] = strike("      Bingo !     ")
                    PrintGrid()
                    print("BINGO !")
                    return True
            case 9:
                result = 0
                result += gList[0] + gList[1] + gList[2] + gList[3] + gList[4]
                if result == 0:
                    gList[0] = strike("      Bingo !     ")
                    gList[1] = strike("      Bingo !     ")
                    gList[2] = strike("      Bingo !     ")
                    gList[3] = strike("      Bingo !     ")
                    gList[4] = strike("      Bingo !     ")
                    PrintGrid()
                    print("BINGO !")
                    return True
            case 10:
                result = 0
                result += oList[0] + oList[1] + oList[2] + oList[3] + oList[4]
                if result == 0:
                    oList[0] = strike("      Bingo !     ")
                    oList[1] = strike("      Bingo !     ")
                    oList[2] = strike("      Bingo !     ")
                    oList[3] = strike("      Bingo !     ")
                    oList[4] = strike("      Bingo !     ")
                    PrintGrid()
                    print("BINGO !")
                    return True
            case 11:
                result = 0
                result += bList[0] + iList[1] + nList[2] + gList[3] + oList[4]
                if result == 0:
                    bList[0] = strike("      Bingo !     ")
                    iList[1] = strike("      Bingo !     ")
                    nList[2] = strike("      Bingo !     ")
                    gList[3] = strike("      Bingo !     ")
                    oList[4] = strike("      Bingo !     ")
                    PrintGrid()
                    print("BINGO !")
                    return True
            case 12:
                result = 0
                result += bList[4] + iList[3] + nList[2] + gList[1] + oList[0]
                if result == 0:
                    bList[4] = strike("      Bingo !     ")
                    iList[3] = strike("      Bingo !     ")
                    nList[2] = strike("      Bingo !     ")
                    gList[1] = strike("      Bingo !     ")
                    oList[0] = strike("      Bingo !     ")
                    PrintGrid()
                    print("BINGO !")
                    return True
    return False
numerosJaSorteados = []
while gameIsOver == False:
    PrintGrid()
    if isPlaying == "Yes":
        sorteio = int(input("Qual o número ?\n"))
    else:
        while True:
            sorteio = random.randint(1,75)
            if sorteio not in numerosJaSorteados:
                numerosJaSorteados.append(sorteio)
                break
    
    print(f"O Número sorteado foi : {sorteio}")
    
    # Don't do this at home
    for i in range(5):
        if bList[i] == sorteio:
            bList[i] = 0
    for i in range(5):
        if iList[i] == sorteio:
            iList[i] = 0
    for i in range(5):
        if nList[i] == sorteio:
            nList[i] = 0
    for i in range(5):
        if gList[i] == sorteio:
            gList[i] = 0
    for i in range(5):
        if oList[i] == sorteio:
            oList[i] = 0
    gameIsOver = CheckForBingo()
    #PrintGrid()