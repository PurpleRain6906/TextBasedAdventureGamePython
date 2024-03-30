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
    class Words:
        bladedWeapons = ["Katana","Claymore","Scimitar","Glaive","Warhammer","Dual Wielded Daggers","Kama","Nunchaku","Khopesh","Gladius"]
        rangedWeapons = ["Longbow","Shortbow","Composite Bow","Crossbow","Sling","Throwing Spears","Hunting Sling","Atlatl","Blowgun","Hand Cannon"]
        magicScrolls = ["Fireball Scroll", "Ice Bolt Scroll", "Healing Touch Scroll","Lightning Strike Scroll", "Invisibility Scroll", "Telekinesis Scroll","Summon Creature Scroll", "Mind Control Scroll", "Haste Scroll","Illusion Scroll"]
        companions = ["Dog", "Cat", "Hawk", "Horse", "Monkey", "Wolf", "Giant Lizard","Small Dragon", "Robot", "Ghost"]
        allWeapons = bladedWeapons + rangedWeapons + magicScrolls + companions
        bladedWeaponsDesc = ["A curved, single-edged sword known for its elegance and lethality in skilled hands. Offers good slashing damage and quick attacks.","A large, two-handed sword with a broad blade. Ideal for powerful swings and crowd control.","A curved, single-edged sword with a forward-pointing tip. Excellent for thrusting attacks and precise cuts.","A long, two-handed weapon with a spear-like point and a single-edged blade at the end. Good for both thrusting and sweeping attacks.","A versatile weapon with a heavy, blunt head and often spikes or hooks. Effective against armored enemies and can deliver crushing blows.","A pair of small, pointed knives used for lightning-fast attacks and exploiting enemy openings. Great for agile characters.","A single-edged, curved blade resembling a sickle. Useful for both slashing and reaping attacks, can also disarm enemies.","Two wooden staves connected by a rope or chain. Offers fast, close-range strikes and can disarm enemies.","A curved sword with a distinctive, forward-curving blade. Good for slashing attacks and can hook around enemy shields.","A short sword with a straight, double-edged blade. Ideal for thrusting attacks in close formation combat."]
        rangedWeaponsDesc = ["A powerful bow known for its long range and accuracy. Requires significant strength to draw back the string.","A smaller, more agile bow than the longbow, ideal for mounted archers or close-quarters combat.","Made from different materials laminated together, offering power and flexibility. Popular in Asian cultures.","A mechanical bow with a trigger mechanism, allowing for easier aiming and deadlier bolts.","A simple weapon using a projectile and a strap for launching. Often used by lightly-armored skirmishers.","A versatile weapon for throwing or close-quarters combat. Can be used for single targets or area denial.","A heavier version of the sling, capable of launching larger projectiles or even stones for siege warfare.","A throwing stick that adds leverage and power to spears, increasing their range and lethality.","A silent weapon using small darts that can inflict damage or status effects like poison. Useful for stealthy attacks or hunting small game.","A heavy, single-shot firearm with a long reload time. Powerful against armored enemies but cumbersome to use."]
        magicScrollsDesc = ["Hurls a blazing orb at the target, dealing significant fire damage and potentially inflicting a burning effect that deals damage over time.","Launches a shard of enchanted ice, piercing the target and dealing cold damage. May also slow their movement or even freeze them momentarily.","Bathes a target in restorative energy, mending their wounds and restoring lost health. Can be used on yourself or an ally.","Calls down a bolt of crackling lightning from the heavens, striking a single enemy or arcing between multiple foes in a chain. Deals significant electrical damage and may stun them momentarily.","Shrouds the caster in an illusion, masking their presence from sight. Useful for sneaking past enemies or repositioning for a surprise attack. The effect fades after a short duration.","Grants the user temporary control over nearby objects with their mind. This allows them to throw objects at enemies, disarm them, or even create temporary barriers for defense.","Unfurls a magical portal, summoning a powerful creature to fight alongside the caster for a limited time. The type of creature varies depending on the scroll.","Briefly seizes control of an enemy's mind, turning them against their allies for a short duration. This can be a powerful tactical tool to turn the tide of battle.","Imbues the caster or an ally with invigorating energy, granting them increased movement speed and attack speed for a limited time. This allows for a flurry of attacks or a quick escape.","Weaves a convincing illusion to deceive enemies. This could be a decoy to distract them, a false image to hide the caster's true location, or even a terrifying apparition to demoralize foes."]
        companionDesc = ["A loyal and versatile companion offering both offensive and defensive support. Can be trained for combat, tracking, or resource gathering.","A nimble and independent companion, providing scouting and stealth benefits. Can inflict minor damage on enemies.","A high-flying companion offering aerial recon and distraction tactics. Can mark enemies for the player and potentially carry small items.","A reliable mount for increased travel speed and maneuverability. Can be used for combat charges or swift escapes.","A playful and agile companion with surprising climbing and thieving abilities. Can access hidden areas and retrieve items.","A fierce and pack-oriented companion, useful for flanking attacks and overwhelming enemies. Requires strong leadership from the player.","A powerful and intimidating companion, offering brute force and protection in combat. Can also be used for transporting heavy items.","A rare and powerful companion, capable of breathing fire or other elemental attacks. Requires a high level of training and care.","A customizable companion with various functionalities depending on its programming. Can be used for combat, exploration, or crafting assistance.","An ethereal companion with unique abilities like phasing through walls and scouting enemy positions. May have limitations in direct combat."]

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
    zone = "Forest"
    inventory = ["Fireball Scroll"]
    def UpdateCoords():
        Player.coords = "(" + str(Player.x) + ", " + str(Player.y) + ")"
    def Input():
        Input = input().lower().split()
        return Input
    def Move():
        inputSplit = Player.Input()
        if len(inputSplit) > 0:
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
    def checkInv():
        print("}------------------------------{")
        for i in Counter(Player.inventory).keys():
            print("}---> " + str(i) + " x" + str(Counter(Player.inventory)[i]))
        print("}------------------------------{")
    class Fight:
        def Options():
            inputNum = 0
            for item in Counter(Player.inventory).keys()
            if "Fireball Scroll" in Counter(Player.inventory).keys():
                inputNum += 1
                print(f"{inputNum}. ")
            fireNum = inputNum

class Enemies:
    def nymph():
        print(Words.dryadAttackStatements[random.randint(0,9)])
    
    def Pan():
        print(Words.panAttackStatements[random.randint(0,9)])

while 1:
    if Player.alive == True:
        Player.Fight.Options()
        Enemies.nymph()
        Enemies.Pan()
        print(Player.alive)
        print(Player.x)
        print(Player.y)
        print(Player.z)
        print(Player.coords)
        print(Player.isMoving)
        Player.Move()
        Player.UpdateCoords()
        Player.checkInv()
    else:
        print("You have died!")