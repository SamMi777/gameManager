import random
from Player import playerStats

def genFirstLvl(name):
    p1 = random.randint(40,100)
    p2 = random.randint(40,100)
    
    total = (p1+p2)/2
    
    player = playerStats(p1, False, p2, total, name)
    
    return player

def setPlayer(shooting, brains):
    total = (shooting + brains) /2
    return total 
    

def printPlayerStats(shooting, brains, total, name):
    print(name,"","\nshooting:",shooting,"\nbrains:",brains,"\noverall:",total,"\n")
    
def yourTeamOVR(OVR1, OVR2, OVR3, OVR4, OVR5):
    teamOVR = (OVR1+OVR2+OVR3+OVR4+OVR5) / 5
    return teamOVR

def enemyTeam():
    enemy = random.randint(40, 100)
    return enemy

def playGame(game,us, them, prstg, wincnt):
    if us > them:
        print("game:",game,"You win! not even close.")
        prstg = prstg + 1
        wincnt = wincnt +1
    elif them > us:
        print("game:",game,"You lose. almost had it.")
        prstg = prstg - 1
    else:
        print("game:",game,"Tie. everyone loses.")    
        
    return prstg, wincnt    
       

def gameWin(wincnt):
        if wincnt == 0:
            print("You didn't win any games. Your team goes home dissapointed.")
        elif wincnt == 1:
            print("You won a game. Your team didn't quite reach expectations.")
        elif wincnt == 2:
            print("You came in second. Better luck next time.")
        else:
            print("You won! You went undefeated and won the tournament!")
            
        return 0
    
def upgradePlayers(value1, value2, value3, value4, value5, upgradeType):
    if (upgradeType == 1) or (upgradeType == 2):
        value1 = value1 + random.randint(0,3)
        value2 = value2 + random.randint(0,3)
        value3 = value3 + random.randint(0,3)
        value4 = value4 + random.randint(0,3)
        value5 = value5 + random.randint(0,3)
        
    elif upgradeType == 3:
        value1 = value1 + random.randint(0,1.5)
        value2 = value2 + random.randint(0,1.5)
        value3 = value3 + random.randint(0,1.5)
        value4 = value4 + random.randint(0,1.5)
        value5 = value5 + random.randint(0,1.5)
        
    else:
        coinFlip = random.randint(0,1)
        if coinFlip == 0:
            value1 = value1 + random.randint(0,5)
            value2 = value2 + random.randint(0,5)
            value3 = value3 + random.randint(0,5)
            value4 = value4 + random.randint(0,5)
            value5 = value5 + random.randint(0,5)            
        
        
    return value1, value2, value3, value4, value5