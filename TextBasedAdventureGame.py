alive = True
playerX = 0
playerY = 0
zone = "clearing"
recentMove = 0
northWords = ["w","up","north"]
eastWords = ["d","right","east"]
southWords = ["s","down","south"]
westWords = ["a","left","west"]
moveWords = ["move","go","travel","wander","run","walk","proceed","progress","advance","journey","trudge"]
clearingLocationX = [-3,-2,-1,0,1,2,3,4]
clearingLocationY = [-4,-3,-2,-1,0,1,2,3]
forestLocationX = [-13,-12,-11,-10,-9,-8,-7,-6,-5,-4]
forestLocationY = [-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11]
desertLocationX = [-3,-2,-1,0,1,2,3,4,5,6,7,8]
desertLocationY = [4,5,6,7,8,9,10,11,12,13]
BorderLocationX = [9,-14]
BorderLocationY = [-6,14]





print("Welcome to a game! (currently without a name!)")
while alive == True:
    if playerX in clearingLocationX and playerY in clearingLocationY:
        zone = "clearing"
        if recentMove == 1:
            if previousZone == zone:
                print("You move further into the", zone + ".")
            else:
                print("You have moved into a", zone + ".")
            recentMove = 0
        else:
            print("You are in a", zone + ".")
        previousZone = zone
    elif playerX in forestLocationX and playerY in forestLocationY:
        zone = "forest"
        if recentMove == 1:
            if previousZone == zone:
                print("You move further into the", zone + ".")
            else:
                print("You have moved into a", zone + ".")
            recentMove = 0
        else:
            print("You are in a", zone + ".")
        previousZone = zone
    elif playerX in desertLocationX and playerY in desertLocationY:
        zone = "desert"
        if recentMove == 1:
            if previousZone == zone:
                print("You move further into the", zone + ".")
            else:
                print("You have moved into a", zone + ".")
            recentMove = 0
        else:
            print("You are in a", zone + ".")
        previousZone = zone

    playerInput = input()
    playerInput = playerInput.lower()
    playerInputSplit = playerInput.split()
    if playerInputSplit[0] in moveWords or northWords or eastWords or southWords or westWords:
        if playerInputSplit[0] in northWords:
            playerY += 1
            recentMove = 1
        elif playerInputSplit[0] in southWords:
            playerY += -1
            recentMove = 1
        elif playerInputSplit[0] in eastWords:
            playerX += 1
            recentMove = 1
        elif playerInputSplit[0] in westWords:
            playerX += -1
            recentMove = 1
        elif len(playerInputSplit) > 1:
            if playerInputSplit[1] in northWords:
                playerY += 1
                recentMove = 1
            elif playerInputSplit[1] in southWords:
                playerY += -1
                recentMove = 1
            elif playerInputSplit[1] in eastWords:
                playerX += 1
                recentMove = 1
            elif playerInputSplit[1] in westWords:
                playerX += -1
                recentMove = 1
            else:
                print("This is not a valid input!")
                alive = False
        else:
            print("This is not a valid input!")
            alive = False
print("You are in a", zone + ".")
while 1:
    deathInput = input()
    if deathInput != "restart":
        print("You are dead. You cannot", deathInput + ". Input 'restart' to restart.")
    else:
        print("Welcome to a game! (currently without a name!)")
        alive = True
