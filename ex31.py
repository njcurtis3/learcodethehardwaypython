print "You enter a dark room with two doors. Do you go through door #1, door #2, or down the stairs?"

door = raw_input(">")

stairs = raw_input(">.")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input(".>")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good Job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input(">")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good Job!"
    elif insanity == "3":
        print "AHHHHHHHH!"    
    else:
        print "The insanity rots your eyes into a pool of much. Good Job!"


if stairs == "stairs":
    print "There is a dragon...waiting for it's next meal. What do you do?"
    print "1. scream at the dragon"
    print "2. throw the torch sitting on the wall"
    print "3. Cry like a baby."

    dragon = raw_input(">")

    if dragon == "1":
        print "The dragon screams back. WITH FIRE! You are dead."
    elif dragon == "2":
        print "The dragon swallows the torch whole. But spares you."
    elif dragon == "3":
        print "The dragon laughs at you loudly"
    else:
        print "Well...you die."
