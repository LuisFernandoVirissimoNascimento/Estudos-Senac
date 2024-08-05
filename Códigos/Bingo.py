import random
isPlaying = input("Are you playing ?\n")
def FillList(list:list, min:int, max:int, hasBlank:bool):
    for i in range(5):
        if(hasBlank and i == 2):       
            list.append(0)    
        else:
            while True:
                randomAdd = random.randint(min,max)
                if randomAdd not in list:
                    list.append(randomAdd)
                    break

bList = []
FillList(bList, 1, 15, False)
iList = []
FillList(iList, 16, 30, False)
nList = []
FillList(nList, 31, 45, True)
gList = []
FillList(gList, 46, 60, False)
oList = []
FillList(oList, 61, 75, False)

print(bList,iList,nList,gList,oList)
def strike(text):
    return ''.join([u'\u0336{}'.format(c) for c in text])
def GridFormatter(num):
    try:
        if num == 0:
            return "      Bingo !     "
        if num < 10:
            return f"        0{num}        "
        else:
            return f"        {num}        "
    except TypeError:
        return num
    
def PrintGrid():
    print(f"""
    ________________________________________________________________________________________________
    |                  |                  |                  |                  |                  |
    |{GridFormatter(bList[0])}|{GridFormatter(iList[0])}|{GridFormatter(nList[0])}|{GridFormatter(gList[0])}|{GridFormatter(oList[0])}|
    |__________________|__________________|__________________|__________________|__________________|
    |                  |                  |                  |                  |                  |
    |{GridFormatter(bList[1])}|{GridFormatter(iList[1])}|{GridFormatter(nList[1])}|{GridFormatter(gList[1])}|{GridFormatter(oList[1])}|
    |__________________|__________________|__________________|__________________|__________________|
    |                  |                  |                  |                  |                  |
    |{GridFormatter(bList[2])}|{GridFormatter(iList[2])}|{GridFormatter(nList[2])}|{GridFormatter(gList[2])}|{GridFormatter(oList[2])}|
    |__________________|__________________|__________________|__________________|__________________|
    |                  |                  |                  |                  |                  |
    |{GridFormatter(bList[3])}|{GridFormatter(iList[3])}|{GridFormatter(nList[3])}|{GridFormatter(gList[3])}|{GridFormatter(oList[3])}|
    |__________________|__________________|__________________|__________________|__________________|
    |                  |                  |                  |                  |                  |
    |{GridFormatter(bList[4])}|{GridFormatter(iList[4])}|{GridFormatter(nList[4])}|{GridFormatter(gList[4])}|{GridFormatter(oList[4])}|
    |                  |                  |                  |                  |                  |
    -------------------------------------------------------------------------------------------------
    """)

PrintGrid()

## Do this per now
# gameIsOver = False
# def CheckForBingo():
#     # 27 possibilities
#     for result in range(1,12):
#         match result:
#             case 1:
#                 result = 0
#                 result += bList[0] + iList[0] + nList[0] + gList[0] + oList[0]
#                 if result == 0:
#                     bList[0] = "Bingo !"
#                     iList[0] = "Bingo !"
#                     nList[0] = "Bingo !"
#                     gList[0] = "Bingo !"
#                     oList[0] = "Bingo !"
#                     PrintGrid()
#                     print("BINGO !")
#                     return True
#             case 2:
#                 result = 0
#                 result += bList[1] + iList[1] + nList[1] + gList[1] + oList[1]
#                 if result == 0:
#                     bList[1] = "Bingo !"
#                     iList[1] = "Bingo !"
#                     nList[1] = "Bingo !"
#                     gList[1] = "Bingo !"
#                     oList[1] = "Bingo !"
#                     PrintGrid()
#                     print("BINGO !")
#                     return True
#             case 3:
#                 result = 0
#                 result += bList[2] + iList[2] + nList[2] + gList[2] + oList[2]
#                 if result == 0:
#                     bList[2] = "Bingo !"
#                     iList[2] = "Bingo !"
#                     nList[2] = "Bingo !"
#                     gList[2] = "Bingo !"
#                     oList[2] = "Bingo !"
#                     PrintGrid()
#                     print("BINGO !")
#                     return True
#             case 4:
#                 result = 0
#                 result += bList[3] + iList[3] + nList[3] + gList[3] + oList[3]
#                 if result == 0:
#                     bList[3] = "Bingo !"
#                     iList[3] = "Bingo !"
#                     nList[3] = "Bingo !"
#                     gList[3] = "Bingo !"
#                     oList[3] = "Bingo !"
#                     PrintGrid()
#                     print("BINGO !")
#                     return True
#             case 5:
#                 result = 0
#                 result += bList[4] + iList[4] + nList[4] + gList[4] + oList[4]
#                 if result == 0:
#                     bList[4] = "Bingo !"
#                     iList[4] = "Bingo !"
#                     nList[4] = "Bingo !"
#                     gList[4] = "Bingo !"
#                     oList[4] = "Bingo !"
#                     PrintGrid()
#                     print("BINGO !")
#                     return True
#             case 6:
#                 result = 0
#                 result += bList[0] + bList[1] + bList[2] + bList[3] + bList[4]
#                 if result == 0:
#                     bList[0] = "Bingo !"
#                     bList[1] = "Bingo !"
#                     bList[2] = "Bingo !"
#                     bList[3] = "Bingo !"
#                     bList[4] = "Bingo !"
#                     PrintGrid()
#                     print("BINGO !")
#                     return True
#             case 7:
#                 result = 0
#                 result += iList[0] + iList[1] + iList[2] + iList[3] + iList[4]
#                 if result == 0:
#                     iList[0] = "Bingo !"
#                     iList[1] = "Bingo !"
#                     iList[2] = "Bingo !"
#                     iList[3] = "Bingo !"
#                     iList[4] = "Bingo !"
#                     PrintGrid()
#                     print("BINGO !")
#                     return True
#             case 8:
#                 result = 0
#                 result += nList[0] + nList[1] + nList[2] + nList[3] + nList[4]
#                 if result == 0:
#                     nList[0] = "Bingo !"
#                     nList[1] = "Bingo !"
#                     nList[2] = "Bingo !"
#                     nList[3] = "Bingo !"
#                     nList[4] = "Bingo !"
#                     PrintGrid()
#                     print("BINGO !")
#                     return True
#             case 9:
#                 result = 0
#                 result += gList[0] + gList[1] + gList[2] + gList[3] + gList[4]
#                 if result == 0:
#                     gList[0] = "Bingo !"
#                     gList[1] = "Bingo !"
#                     gList[2] = "Bingo !"
#                     gList[3] = "Bingo !"
#                     gList[4] = "Bingo !"
#                     PrintGrid()
#                     print("BINGO !")
#                     return True
#             case 10:
#                 result = 0
#                 result += oList[0] + oList[1] + oList[2] + oList[3] + oList[4]
#                 if result == 0:
#                     oList[0] = "Bingo !"
#                     oList[1] = "Bingo !"
#                     oList[2] = "Bingo !"
#                     oList[3] = "Bingo !"
#                     oList[4] = "Bingo !"
#                     PrintGrid()
#                     print("BINGO !")
#                     return True
#             case 11:
#                 result = 0
#                 result += bList[0] + iList[1] + nList[2] + gList[3] + oList[4]
#                 if result == 0:
#                     bList[0] = "Bingo !"
#                     iList[1] = "Bingo !"
#                     nList[2] = "Bingo !"
#                     gList[3] = "Bingo !"
#                     oList[4] = "Bingo !"
#                     PrintGrid()
#                     print("BINGO !")
#                     return True
#             case 12:
#                 result = 0
#                 result += bList[4] + iList[3] + nList[2] + gList[1] + oList[0]
#                 if result == 0:
#                     bList[4] = "Bingo !"
#                     iList[3] = "Bingo !"
#                     nList[2] = "Bingo !"
#                     gList[1] = "Bingo !"
#                     oList[0] = "Bingo !"
#                     PrintGrid()
#                     print("BINGO !")
#                     return True
#     return False
# numerosJaSorteados = []
# while gameIsOver == False:
#     gameIsOver = CheckForBingo()
#     while True:
#         sorteio = random.randint(1,75)
#         if sorteio not in numerosJaSorteados:
#             numerosJaSorteados.append(sorteio)
#             break
    
#     print(f"O Número sorteado foi : {sorteio}")
    
#     # Don't do this at home
#     for i in range(5):
#         if bList[i] == sorteio:
#             bList[i] = 0
#     for i in range(5):
#         if iList[i] == sorteio:
#             iList[i] = 0
#     for i in range(5):
#         if nList[i] == sorteio:
#             nList[i] = 0
#     for i in range(5):
#         if gList[i] == sorteio:
#             gList[i] = 0
#     for i in range(5):
#         if oList[i] == sorteio:
#             oList[i] = 0
#     #PrintGrid()
