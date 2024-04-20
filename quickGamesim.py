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
    
    #generating the 5 players on the team using a given name for parameter
    player1 = game.genFirstLvl("j-train")
    player2 = game.genFirstLvl("mlkao")
    player3 = game.genFirstLvl("don4ld")
    player4 = game.genFirstLvl("sn1perk1ng")
    player5 = game.genFirstLvl("h34dsh0t")
    
    #assigning team overall by taking the total of your players and printing it
    teamOverall = game.yourTeamOVR(player1.total, player2.total, player3.total, player4.total, player5.total)    
    
    val = int(input("Main Menu\n(1)View Team\n(2)bootcamp\n(3)Sign new player\n(4)play tournament\n(5)quit\n"))
    
    while val != 0:
        #if the user chooses 1 for the input
        #prints the team overall and prestige as a display using the printPlayerStats function which takes the generated values for the individuals        
        if(val == 1):                
            player1.total = game.setPlayer(player1.shooting, player1.brains)
            player2.total = game.setPlayer(player2.shooting, player2.brains)
            player3.total = game.setPlayer(player3.shooting, player3.brains)
            player4.total = game.setPlayer(player4.shooting, player4.brains)
            player5.total = game.setPlayer(player5.shooting, player5.brains)
            print("team overall:", teamOverall,"\nteam prestige:", prestige, "\n")
            game.printPlayerStats(player1.shooting, player1.brains, player1.total, player1.name)
            game.printPlayerStats(player2.shooting, player2.brains, player2.total, player2.name)
            game.printPlayerStats(player3.shooting, player3.brains, player3.total, player3.name)
            game.printPlayerStats(player4.shooting, player4.brains, player4.total, player4.name)
            game.printPlayerStats(player5.shooting, player5.brains, player5.total, player5.name)
            #assigning val to reset the loop as opposed to calling it again
            val = 100
            
        if(val == 2 and (weeksLeft > 0)):
            weeksLeft = weeksLeft - 1
            print("weeks left:", weeksLeft)
            loopval = True            
            while(loopval):
                upVal = int(input("Select training focus:\n(1)shooting\n(2)brain\n(3)combination\n(4)high risk/high reward\n"))
                if(upVal < 5):
                    if upVal == 1:
                        player1.shooting, player2.shooting, player3.shooting, player4.shooting, player5.shooting = game.upgradePlayers(player1.shooting, player2.shooting, player3.shooting, player4.shooting, player5.shooting, 1)
                        print("upgrade shooting")
                        loopval = False
                        teamOverall = game.yourTeamOVR(player1.total, player2.total, player3.total, player4.total, player5.total)  
                    elif upVal == 2:
                        player1.brains, player2.brains, player3.brains, player4.brains, player5.brains = game.upgradePlayers(player1.brains, player2.brains, player3.brains, player4.brains, player5.brains, 2)
                        print("upgrade brain")
                        loopval = False
                        teamOverall = game.yourTeamOVR(player1.total, player2.total, player3.total, player4.total, player5.total)  
                    elif upVal == 3:
                        player1.brains, player2.brains, player3.brains, player4.brains, player5.brains = game.upgradePlayers(player1.brains, player2.brains, player3.brains, player4.brains, player5.brains, 3)
                        player1.shooting, player2.shooting, player3.shooting, player4.shooting, player5.shooting = game.upgradePlayers(player1.shooting, player2.shooting, player3.shooting, player4.shooting, player5.shooting, 3)
                        print("upgrade both")
                        loopval = False
                        teamOverall = game.yourTeamOVR(player1.total, player2.total, player3.total, player4.total, player5.total)  
                    elif upVal == 4:
                        player1.brains, player2.brains, player3.brains, player4.brains, player5.brains = game.upgradePlayers(player1.brains, player2.brains, player3.brains, player4.brains, player5.brains, 4)
                        player1.shooting, player2.shooting, player3.shooting, player4.shooting, player5.shooting = game.upgradePlayers(player1.shooting, player2.shooting, player3.shooting, player4.shooting, player5.shooting, 4)
                        print("risk reward")
                        loopval = False
                        teamOverall = game.yourTeamOVR(player1.total, player2.total, player3.total, player4.total, player5.total)  
                    else:
                        upVal = 5

            val = 100
        
            
        if(val == 3 and (weeksLeft > 0)):
            weeksLeft = weeksLeft - 1
            #add new player menu: 
            #os clr
            #new players(3-5) offer to switch out your players
            #if selected, override the stored data for your player
            print("weeks left:", weeksLeft, "\nnew player signed!\n")
            game.printPlayerStats(player1.shooting, player1.brains, player1.total, player1.name)
            game.printPlayerStats(player2.shooting, player2.brains, player2.total, player2.name)
            game.printPlayerStats(player3.shooting, player3.brains, player3.total, player3.name)
            game.printPlayerStats(player4.shooting, player4.brains, player4.total, player4.name)
            game.printPlayerStats(player5.shooting, player5.brains, player5.total, player5.name)
            val = 100
            
        if(val == 4):
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
        
        else:            
            val = int(input("Main Menu\n(1)View Team\n(2)bootcamp\n(3)Sign new player\n(4)play tournament\n(5)quit\n"))
            os.system('cls')
    
        
    
main()