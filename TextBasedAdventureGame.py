import random
import time

class Words:
    northWords = ["w","forwards","north"]
    eastWords = ["d","right","east"]
    southWords = ["s","backwards","south"]
    westWords = ["a","left","west"]
    moveWords = ["move","go","travel","wander","run","walk","proceed","progress","advance","journey","trudge"]

class Player:
    alive = True
    maxHealth = 5
    health = maxHealth
    x = 0
    y = 0
    z = 0
    coords = str(x) + "." + str(y)
    invalid = 1
    isMoving = False
    zone = "Forest"
    def UpdateCoords():
        Player.coords = "(" + str(Player.x) + "." + str(Player.y) + ")"
    def Input():
        Input = input().lower().split()
        return Input
    def Move():
        inputSplit = Player.Input()
        if inputSplit[0] in Words.eastWords:
            Player.x += 1
            Player.isMoving = True
        elif inputSplit[0] in Words.westWords:
            Player.x -= 1
            Player.isMoving = True
        elif inputSplit[0] in Words.northWords:
            Player.y += 1
            Player.isMoving = True
        elif inputSplit[0] in Words.southWords:
            Player.y -= 1
            Player.isMoving = True
        elif inputSplit[0] in Words.moveWords:
            if inputSplit[1] in Words.eastWords:
                Player.x += 1
                Player.isMoving = True
            elif inputSplit[1] in Words.westWords:
                Player.x -= 1
                Player.isMoving = True
            elif inputSplit[1] in Words.northWords:
                Player.y += 1
                Player.isMoving = True
            elif inputSplit[1] in Words.southWords:
                Player.y -= 1
                Player.isMoving = True
            else:
                Player.invalid -= 1
                Player.isMoving = False
        else:
            Player.invalid -= 1
            Player.isMoving = False
        
class Enemies:
    health = 5

while 1:
    print(Player.alive)
    print(Player.x)
    print(Player.y)
    print(Player.z)
    print(Player.coords)
    print(Player.isMoving)
    Player.Move()
    Player.UpdateCoords()
