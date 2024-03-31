import random
from collections import Counter

class Words:
    northWords = ["w","forwards","north"]
    eastWords = ["d","right","east"]
    southWords = ["s","backwards","south"]
    westWords = ["a","left","west"]
    moveWords = ["move","go","travel","wander","run","walk","proceed","progress","advance","journey","trudge"]
    dryadAttackStatements = [
  "A gnarled hand bursts from the tree trunk, followed by a furious face twisted with bark and leaves. The dryad lunges, sharp branches bared like claws!",
  "The forest floor erupts as a dryad wreathed in vines explodes from the undergrowth. Thorns lash out, aiming to ensnare you in her deadly embrace!",
  "A seductive voice chills the air. A beautiful woman emerges from the tree, but her eyes glow with a malevolent green light. She lunges, faster than you thought possible!",
  "The once serene grove writhes in anger. A towering dryad composed of twisted branches and emerald leaves lunges at you, a living embodiment of nature's fury!",
  "The ground trembles as thick roots erupt from the earth, propelling a monstrous dryad towards you. Her bark-like skin cracks, revealing glowing embers beneath!",
  "A hauntingly beautiful melody lures you closer. But as you step into a sunbeam, the melody twists into a discordant screech. A dryad lunges from the shadows, rage contorting her face!",
  "A single perfect flower blooms on a nearby tree. As you reach out to touch it, the flower explodes, revealing a vengeful dryad with thorns dripping with a poisonous sap!",
  "The bark of a towering oak groans as it splits open. A colossal dryad emerges, her moss-covered eyes blazing with fury. Prepare to face the forest's ancient guardian!",
  "A sickly sweet scent fills the air. A grotesque dryad, her form a twisted mix of wood and decaying flesh, lunges from a hollowed-out log. Fight or flee the putrid embrace!",
  "The wind rustles the leaves, carrying fragmented whispers that promise pain. A dryad, her form barely there, shimmers into existence and lunges with unnatural speed!"
]
    panAttackStatements = [
    "A bestial roar pierces the stillness. Pan, the half-man, half-goat god of the wild, bursts from the thicket, hooves pounding, horns glinting maliciously. He lunges for you, a twisted grin revealing razor-sharp fangs.",
    "The earth trembles as Pan charges from the treeline. Leaves swirl around his horned head, obscuring his crazed eyes. With a savage cry, he raises his shepherd's crook, ready to deliver a bone-shattering blow.",
    "Sunlight dapples the forest floor, but a shadow falls dark and menacing. Pan lunges from behind a towering oak, his matted fur bristling, his eyes glowing with predatory hunger. ",
    "A chilling wind howls through the mountain pass. A monstrous figure emerges from the swirling mist – Pan, his goat legs carrying him with unnatural speed. His pan flute hangs broken at his side, replaced by a bloodthirsty snarl. ",
    "You hear the baying of hounds in the distance. Suddenly, Pan cuts through the undergrowth, a pack of rabid wolves snapping at his heels. He raises a hunting spear, its tip glinting with a malevolent light. ",
    "A hidden path leads deep into a forgotten grove. But guarding its entrance is Pan, his wild eyes blazing with fury. He slams his cloven hooves on the ground, the earth itself trembling in response.",
    "The full moon bathes the forest in an eerie glow. Pan steps out from the shadows, his pipes clutched in his hands. But the music they emit is no calming melody – it’s a jarring cacophony that chills you to the bone. ",
    "The gurgling of a hidden stream fills the air. Rounding a bend, you come face-to-face with Pan. Water drips from his matted fur, and his eyes gleam with a feral intensity. He lets out a guttural roar and charges.",
    "The scent of ripe apples hangs heavy in the air. As you reach for a fruit, a monstrous hand snatches it away. Pan stands before you, his face contorted in a grotesque parody of a smile. ",
    "Crumbling stones litter the ground, remnants of a forgotten temple. A monstrous roar echoes through the ruins. Pan emerges from the shadows, his eyes burning with a mad rage. He lowers his head, his sharp horns aimed directly at you. ",
]

class Items:
    scrolls = {
        "Vampiric Echo" : {
            "rarity" : "legendary",
            "effect" : "50% chance for an extra 10% vampiric strike"
        },
        "Echo" : {
            "rarity" : "rare",
            "effect" : "50% chance for an extra strike."
        },
        "Vampiric" : {
            "rarity" : "epic",
            "effect" : "Your main strike is 10% vampiric."
        },
        "Mnemonic" : {
            "rarity" : "rare",
            "effect" : "You store 10% of the damage dealt each time. This can be released for a damage bonus."
        },
    }

class Player:
    alive = True
    maxHealth = 5
    health = maxHealth
    x = 0
    y = 0
    z = 0
    coords = str(x) + ", " + str(y)
    invalid = 1
    isMoving = False
    attack = True
    zone = "Forest"
    inventory = []
    equips = []
    def UpdateCoords():
        Player.coords = "(" + str(Player.x) + ", " + str(Player.y) + ")"
    def Input():
        Input = input(">").lower().split()
        return Input
    def Move():
        if len(Input) > 0:
            if Input[0] in Words.eastWords:
                Player.x += 1
                Player.isMoving = True
            elif Input[0] in Words.westWords:
                Player.x -= 1
                Player.isMoving = True
            elif Input[0] in Words.northWords:
                Player.y += 1
                Player.isMoving = True
            elif Input[0] in Words.southWords:
                Player.y -= 1
                Player.isMoving = True
            elif Input[0] in Words.moveWords:
                if Input[1] in Words.eastWords:
                    Player.x += 1
                    Player.isMoving = True
                elif Input[1] in Words.westWords:
                    Player.x -= 1
                    Player.isMoving = True
                elif Input[1] in Words.northWords:
                    Player.y += 1
                    Player.isMoving = True
                elif Input[1] in Words.southWords:
                    Player.y -= 1
                    Player.isMoving = True
                else:
                    Player.invalid -= 1
                    Player.isMoving = False
            else:
                Player.invalid -= 1
                Player.isMoving = False
    def checkInv():
        print("}------------------------------{")
        for i in Counter(Player.inventory).keys():
            print("}---> " + str(i) + " x" + str(Counter(Player.inventory)[i]))
        print("}------------------------------{")

class Enemies:
    def nymph():
        print(Words.dryadAttackStatements[random.randint(0,9)])
    
    def Pan():
        print(Words.panAttackStatements[random.randint(0,9)])

while 1:
    if Player.alive == True:
        Input = Player.Input()
        Player.Move()
        Player.UpdateCoords()
        Player.checkInv()
        print(Player.alive)
        print(Player.x)
        print(Player.y)
        print(Player.z)
        print(Player.coords)
        print(Player.isMoving)
    else:
        print("You have died!")