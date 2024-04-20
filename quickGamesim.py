from Player import playerStats
import os
import game 

#Sam Minor
#quickGameSim.py edited 4/20/24
    
def main():
    #variables to describe weeks left per cycle
    #prestige to describe team's total prestige
    #wincount to count number of wins per tournament
    weeksLeft = 5
    prestige = 20
    winCount = 0
    print("Welcome to the Game Manager! Here you act as the manager of an up-and-coming team of players.")
    print("As manager you'll have the ability to sign free agents, train your players, and play a tournament every few weeks to gain prestige.")
    enter = input("Press enter to continue.")
    os.system('cls')
    
    #generating the 5 players 
    #first calling createPlayerNames() to take the names.txt file and assign those values to a list
    #Then taking a name from that list and assigning it to the first player
    #Removing that value from the list before returning and doing the same 5 times so there are
    #no repeated names. 
    nameList = game.createPlayerNames()
    playerName, nameList = game.givePlayerNames(nameList)   
    player1 = game.genFirstLvl(playerName)
    playerName, nameList = game.givePlayerNames(nameList)   
    player2 = game.genFirstLvl(playerName)
    playerName, nameList = game.givePlayerNames(nameList)   
    player3 = game.genFirstLvl(playerName)
    playerName, nameList = game.givePlayerNames(nameList)   
    player4 = game.genFirstLvl(playerName)
    playerName, nameList = game.givePlayerNames(nameList)   
    player5 = game.genFirstLvl(playerName)
    
    #assigning team overall by taking the total of your players and printing it
    teamOverall = game.yourTeamOVR(player1.total, player2.total, player3.total, player4.total, player5.total)    
    
    val = int(input("|||||Main Menu|||||\n(1)View Team\n(2)bootcamp\n(3)Sign new player\n(4)play tournament\n(5)quit\n||||||||||||||||||||\n"))
    os.system('cls')
    
    while val != 0:
        #if the user chooses 1 for the input
        #prints the team overall and prestige as a display using the printPlayerStats function which takes the generated values for the individuals        
        if(val == 1):                
            teamOverall = game.yourTeamOVR(player1.total, player2.total, player3.total, player4.total, player5.total)  
            player1.total = game.setPlayer(player1.shooting, player1.brains)
            player2.total = game.setPlayer(player2.shooting, player2.brains)
            player3.total = game.setPlayer(player3.shooting, player3.brains)
            player4.total = game.setPlayer(player4.shooting, player4.brains)
            player5.total = game.setPlayer(player5.shooting, player5.brains)
            print("||||||||||||||||||||\nteam overall:", teamOverall,"\nteam prestige:", prestige, "\n||||||||||||||||||||\n")
            game.printPlayerStats(player1.shooting, player1.brains, player1.total, player1.name)
            game.printPlayerStats(player2.shooting, player2.brains, player2.total, player2.name)
            game.printPlayerStats(player3.shooting, player3.brains, player3.total, player3.name)
            game.printPlayerStats(player4.shooting, player4.brains, player4.total, player4.name)
            game.printPlayerStats(player5.shooting, player5.brains, player5.total, player5.name)
            print("||||||||||||||||||||\n")
            #assigning val to reset the loop as opposed to calling it again
            val = 100
            
        if(val == 2 and (weeksLeft > 0)):
            weeksLeft = weeksLeft - 1
            print("||||||||||||||||||||\nweeks left:", weeksLeft)
            loopval = True            
            while(loopval):
                upVal = int(input("Select training focus:\n(1)aim training\n(2)demo review\n(3)scrims\n(4)anti-strat\n||||||||||||||||||||\n"))
                if(upVal < 5):
                    if upVal == 1:
                        player1.shooting, player2.shooting, player3.shooting, player4.shooting, player5.shooting = game.upgradePlayers(player1.shooting, player2.shooting, player3.shooting, player4.shooting, player5.shooting, 1)
                        print("aim training")
                        loopval = False
                    elif upVal == 2:
                        player1.brains, player2.brains, player3.brains, player4.brains, player5.brains = game.upgradePlayers(player1.brains, player2.brains, player3.brains, player4.brains, player5.brains, 2)
                        print("demo review")
                        loopval = False
                    elif upVal == 3:
                        player1.brains, player2.brains, player3.brains, player4.brains, player5.brains = game.upgradePlayers(player1.brains, player2.brains, player3.brains, player4.brains, player5.brains, 3)
                        player1.shooting, player2.shooting, player3.shooting, player4.shooting, player5.shooting = game.upgradePlayers(player1.shooting, player2.shooting, player3.shooting, player4.shooting, player5.shooting, 3)
                        print("play scrims")
                        loopval = False
                    elif upVal == 4:
                        player1.brains, player2.brains, player3.brains, player4.brains, player5.brains = game.upgradePlayers(player1.brains, player2.brains, player3.brains, player4.brains, player5.brains, 4)
                        player1.shooting, player2.shooting, player3.shooting, player4.shooting, player5.shooting = game.upgradePlayers(player1.shooting, player2.shooting, player3.shooting, player4.shooting, player5.shooting, 4)
                        print("anti-strat")
                        loopval = False
                    else:
                        upVal = 5

            val = 100
        
            
        if(val == 3 and (weeksLeft > 0)):
            weeksLeft = weeksLeft - 1
            playerName1, nameList = game.givePlayerNames(nameList)   
            playerFA1 = game.genFAFirstLevel(playerName1)
            playerName2, nameList = game.givePlayerNames(nameList)   
            playerFA2 = game.genFAFirstLevel(playerName2)
            playerName3, nameList = game.givePlayerNames(nameList)   
            playerFA3 = game.genFAFirstLevel(playerName3)
                        
            print("weeks left:", weeksLeft, "\nchoose new player\n")
            game.printPlayerStats(playerFA1.shooting, playerFA1.brains, playerFA1.total, playerFA1.name)
            game.printPlayerStats(playerFA2.shooting, playerFA2.brains, playerFA2.total, playerFA2.name)
            game.printPlayerStats(playerFA3.shooting, playerFA3.brains, playerFA3.total, playerFA3.name)
            
            FAChoice = int(input("(1)FA 1\n(2)FA 2\n(3)FA 3\n(4)keep current players\n"))
            
            if FAChoice == 1:                
                nameList.append(playerName2)
                nameList.append(playerName3)
                tempPlayer = playerFA1
            elif FAChoice == 2:
                tempPlayer = playerFA2
                nameList.append(playerName1)
                nameList.append(playerName3)
            elif FAChoice == 3:
                tempPlayer = playerFA3
                nameList.append(playerName1)
                nameList.append(playerName2)
            os.system('cls')
            game.printPlayerStats(player1.shooting, player1.brains, player1.total, player1.name)
            game.printPlayerStats(player2.shooting, player2.brains, player2.total, player2.name)
            game.printPlayerStats(player3.shooting, player3.brains, player3.total, player3.name)
            game.printPlayerStats(player4.shooting, player4.brains, player4.total, player4.name)
            game.printPlayerStats(player5.shooting, player5.brains, player5.total, player5.name)
            count = True
            while count and FAChoice < 4:                
                replacePlayer = int(input("Who to replace: (1-5)\n"))
                if(replacePlayer == 1):
                    nameList.append(player1.name)
                    player1 = tempPlayer
                    count = False
                elif replacePlayer == 2:
                    nameList.append(player2.name)
                    player2 = tempPlayer
                    count = False
                elif replacePlayer == 3:
                    nameList.append(player3.name)
                    player3 = tempPlayer
                    count = False
                elif replacePlayer == 4:
                    nameList.append(player4.name)
                    player4 = tempPlayer
                    count = False
                elif replacePlayer == 5: 
                    nameList.append(player5.name)
                    player5 = tempPlayer
                    count = False
                    
            val = 100
            
        if(val == 4):
            os.system('cls')
            weeksLeft = 5            
            enemyOverall = game.enemyTeam()     
            print("your team:", teamOverall)
            print("their team:", enemyOverall)
            prestige, winCount = game.playGame(1, teamOverall, enemyOverall, prestige, winCount)
            
            enemyOverall = game.enemyTeam()
            print("your team:", teamOverall)
            print("their team:", enemyOverall)   
            prestige, winCount = game.playGame(2, teamOverall, enemyOverall, prestige, winCount)
            
            enemyOverall = game.enemyTeam()
            print("your team:", teamOverall)
            print("their team:", enemyOverall)   
            prestige, winCount = game.playGame(3, teamOverall, enemyOverall, prestige, winCount)
            
            winCount = game.gameWin(winCount)                  
            
            val = 100    
        
        
        
        if(val == 5):
            break;   
        
        if prestige < 15:
            loss = input("You've been fired. Game Over.")
            os.system('cls')
            break
        
        
        else:            
            val = int(input("|||||Main Menu|||||\n(1)View Team\n(2)bootcamp\n(3)Sign new player\n(4)play tournament\n(5)quit\n||||||||||||||||||||\n"))
            os.system('cls')
    
        
    
main()