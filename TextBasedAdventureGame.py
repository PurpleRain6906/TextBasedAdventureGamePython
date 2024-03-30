import random
from collections import Counter

class Words:
    northWords = ["w","forwards","north"]
    eastWords = ["d","right","east"]
    southWords = ["s","backwards","south"]
    westWords = ["a","left","west"]
    moveWords = ["move","go","travel","wander","run","walk","proceed","progress","advance","journey","trudge"]
    dryadAttackStatements = [
  "The once serene forest floor erupts as gnarled roots surge from the earth, the dryad at their helm lunging towards you with a primal roar!",
  "A chilling whisper echoes through the trees as vines erupt from the undergrowth, wrapping around your legs and yanking you towards the dryad's outstretched form!",
  "The bark of a nearby tree splits open, revealing a horrifying visage. With a snarl, the dryad lunges, a grotesque mix of wood and fury!",
  "The melodic song of a hidden bird becomes a discordant shriek. Vines lash out from the canopy, guided by the dryad's unseen hand, aiming to bind you!",
  "A beautiful flower you admire suddenly withers and explodes, showering you with a noxious pollen cloud. The dryad emerges from the haze, her rage a palpable force!",
  "A chilling gust of wind whips through the trees, carrying the dryad's insidious whispers. Before you can react, she bursts from the foliage, a whirlwind of wrath!",
  "You reach for a tempting berry, only to find the bush convulses. Razor-sharp thorns erupt, followed by the dryad's cackle as she lunges from the undergrowth!",
  "A vibrant flower unfurls, revealing a gaping maw lined with needle-like teeth. The dryad lunges, her form a grotesque fusion of flora and fauna!",
  "The ancient oak you seek shelter beneath groans in protest. Its bark cracks open, revealing the dryad's vengeful form poised to strike!",
  "The once harmonious chirping of insects transforms into a cacophony of buzzing and clicking. A swarm erupts from the foliage, followed by the dryad's shadowy form!",
  "The ground beneath your feet crumbles as grasping roots erupt, seeking to ensnare you. The dryad's laughter echoes as she lunges from the fissure!",
  "A massive puffball mushroom explodes, releasing a cloud of bioluminescent spores that blind you momentarily. The dryad lunges from the glowing cloud, a predator in the dark!",
  "The vibrant colors of the forest leech away, replaced by an unnatural gloom. The dryad emerges from the shadows, a creature of the night ready to strike!",
  "The path ahead crumbles, revealing a hidden pit. As you scramble back, the dryad erupts from the foliage, her wooden claws outstretched!",
  "A vibrant flower brushes against your arm, its petals draining the color from your skin. The dryad, revitalized, lunges with a renewed ferocity!",
  "A seemingly harmless sapling writhes and transforms, its branches morphing into wickedly sharp thorns. The dryad, now one with the plant, lunges for the kill!",
  "The forest floor splits open, revealing a network of gaping maws lined with razor-sharp teeth. The dryad emerges from the center, a monstrous harbinger of the forest's wrath!",
  "Vines erupt from all sides, wrapping around your limbs and constricting with terrifying force. The dryad appears amidst the tangled mess, her eyes glowing with malevolent glee!",
  "A gentle breeze caresses you, but your skin crawls as it carries a sickly sweet scent. You wither and weaken, the dryad seizing the opportunity to lunge for the final blow!",
  "The ground beneath your feet turns to stone, your legs fusing to the unforgiving surface. The dryad materializes before you, a predator toying with its petrified prey!",
]

class Items:
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
    coords = str(x) + "." + str(y)
    invalid = 1
    isMoving = False
    zone = "Forest"
    inventory = []
    def UpdateCoords():
        Player.coords = "(" + str(Player.x) + "." + str(Player.y) + ")"
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
            print(str(i) + " x" + str(Counter(Player.inventory)[i]))
        print("}------------------------------{")

class Enemies:
    def nymph():
        print(Words.dryadAttackStatements[random.randint(0,19)])
    def Pan():
        print("I am the god Pan!")

while 1:
    (Enemies.nymph())
    print(Player.alive)
    print(Player.x)
    print(Player.y)
    print(Player.z)
    print(Player.coords)
    print(Player.isMoving)
    Player.Move()
    Player.UpdateCoords()
    Player.checkInv()