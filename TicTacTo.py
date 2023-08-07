from colorama import Fore
bord = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
cpu = "X"
Player = "O"

def PrintBord(bord):
  for i in range(0, len(bord), 3):
    group = bord[i:i+3]
    print(group)
    print("---------------")
  print("               ")


def checkDraw():
  for i in range(len(bord)):
    if bord[i] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      return False
  return True

def checkWin():
  if bord[0] == bord[1] and bord[0] == bord[2]:
    return True
  if bord[3] == bord[4] and bord[3] == bord[5]:
    return True
  if bord[6] == bord[7] and bord[6] == bord[8]:
    return True
  if bord[0] == bord[3] and bord[0] == bord[6]:
    return True
  if bord[1] == bord[4] and bord[1] == bord[7]:
    return True
  if bord[2] == bord[5] and bord[2] == bord[8]:
    return True
  if bord[0] == bord[4] and bord[0] == bord[8]:
    return True  
  if bord[2] == bord[4] and bord[2] == bord[6]:
    return True
  else:
    return False
  
def checkLetterWon(letter):
  if bord[0] == bord[1] and bord[0] == bord[2] and bord[0] == letter:
    return True
  if bord[3] == bord[4] and bord[3] == bord[5] and bord[3] == letter:
    return True
  if bord[6] == bord[7] and bord[6] == bord[8] and bord[6] == letter:
    return True
  if bord[0] == bord[3] and bord[0] == bord[6] and bord[0] == letter:
    return True
  if bord[1] == bord[4] and bord[1] == bord[7] and bord[1] == letter:
    return True
  if bord[2] == bord[5] and bord[2] == bord[8] and bord[2] == letter:
    return True
  if bord[0] == bord[4] and bord[0] == bord[8] and bord[0] == letter:
    return True  
  if bord[2] == bord[4] and bord[2] == bord[6] and bord[2] == letter:
    return True
  else:
    return False

def isFree(position):
  if bord[position] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
    return True
  else: return False 
  
 

def insert(position, letter):
  if isFree(position):
    bord[position] = letter
    PrintBord(bord)
    if checkDraw():
      print(Fore.YELLOW + "Remis!")
      exit()
    if checkWin():
      if letter == cpu:
        print(Fore.RED + "CPU gewwint!")
        exit()
      if letter == Player:
        print(Fore.GREEN + "Spieler gewwint!")
        exit()
    return
  else:
    print("!!!iliegale position!!!")
    position = int(input("bitte neue position eingeben: ")) - 1 
    insert(position, letter)
    return

def PlayerMove():
  pos = int(input("bitte feld eingeben: ")) - 1
  insert(pos, Player)
  return

def CpuMove():
  bestScore = -800
  bestMove = 0
  available_moves = [i for i in range(len(bord)) if bord[i] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]]

  for i in available_moves:
      safe = bord[i]
      bord[i] = cpu
      score = minimax(bord, False)
      bord[i] = safe
      if score > bestScore:
        bestScore = score
        bestMove = i
  insert(bestMove, cpu)
  return
  
def minimax(bord, isMax):
  if checkLetterWon(cpu):
    return 1
  elif checkLetterWon(Player):
    return -1
  elif checkDraw():
    return 0
  
  if isMax:
    bestScore = -800
    for i in range(len(bord)):
        if bord[i] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            safe = bord[i]
            bord[i] = cpu
            score = minimax(bord, False)
            bord[i] = safe
            bestScore = max(bestScore, score)
    return bestScore
  else:
    bestScore = 800
    for i in range(len(bord)):
        if bord[i] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            safe = bord[i]
            bord[i] = Player
            score = minimax(bord, True)
            bord[i] = safe
            bestScore = min(bestScore, score)
    return bestScore
      

while not checkWin():
  CpuMove()
  PlayerMove()
