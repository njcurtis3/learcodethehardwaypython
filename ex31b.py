print '''You wake from what feels like a long sleep. Debris is floating all around you.
For a moment you forget where you are. Out of the circular window to your right, you see
the earth. "Oh" you say aloud. You remember you are traveling in a space capsule speeding
towards Mars. Life support systems are near failure. The ship is running out of Oxygen.
Do you call ground station for help? Or do you go back to sleep to conserve energy?'''

decision = raw_input("> ")

if decision == "call":
    print "You hear the radio crackle in your ear. There is a voice on the other side. you say:"
    print "1.Help"
    print "2.What is going on?"
    print "3.Let's get the life support back on."

    answer = raw_input("> ")

    if answer == "1":
        print "We are doing the best we can do come up with a recovery plan. Sit tight."
    elif answer == "2":
        print "You blacked out from massive G forces. The rocket went into a spin."
    elif answer == "3":
        print "Roger that. Engineers are working on a solution."
    else:
        print "Sorry there was static. Say again."

elif decision == "sleep":
    print "You slowly close your eyes and conserve warmth. the radio crackles:"
    print "1. Hello?"
    print "2. you ignore it."
    print "3. I want to go home."

    answer2 = raw_input("> ")

    if answer2 == "1":
        print "Sir, please stay awake. We have to keep you alive."
    elif answer2 == "2":
        print "Curtis, Curtis. Can you hear me?"
    elif answer2 == "3":
        print "I know you do. We are trying. You have to stay awake Curtis."
