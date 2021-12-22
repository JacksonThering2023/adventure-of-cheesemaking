import random
no = 0
points = 250
aPoints = 1
while aPoints > 0:
    fire = input("you have " + str(points) + " points to spend, how many should go to fire? (" + str(points) +"/250)\n")
    if int(fire) > 100:
        fire = 100
    points = points - int(fire)
    
    cheeseMaking = input("you have " + str(points) + " points to spend, how many should go to cheese making? (" + str(points) +"/250)\n")
    if int(cheeseMaking) >= 100:
        cheeseMaking = 100
        print("I dont think that you can lose with that skill")
    if 100 > int(cheeseMaking) > 80:
        print("I heard that cheese making is pretty nice to have")
    points = points - int(cheeseMaking)
    
    strength = input("you have " + str(points) + " points to spend, how many should go to your strength? (" + str(points) +"/250)\n")
    while points - int(strength) < 0:
        print("you do not have enough points for that my guy")
        strength = input("you have " + str(points) + " points to spend, how many should go to your strength? (" + str(points) +"/250)\n")
    if int(strength) > 100:
        strength = 100
    points = points - int(strength)
    
    shadowFight2Ability = input("you have " + str(points) + " points to spend, how good at shadow fight 2 are you? (" + str(points) +"/250)\n")
    while points - int(shadowFight2Ability) < 0:
        print("you do not have enough points for that my guy")
        shadowFight2Ability = input("you have " + str(points) + " points to spend, how good at shadow fight 2 are you? (" + str(points) +"/250)\n")
    if int(shadowFight2Ability) > 100:
        shadowFight2Ability = 100
    points = points - int(shadowFight2Ability)
    
    jimmyJohns = input("you have " + str(points) + " points to spend, how good are you at jimmy johns, the battle royal? (" + str(points) +"/250)\n")
    while points - int(jimmyJohns) < 0:
        print("you do not have enough points for that my guy")
        jimmyJohns = input("you have " + str(points) + " points to spend, how many should go to your strength? (" + str(points) +"/250)\n")
    if int(jimmyJohns) > 100:
        jimmyJohns = 100
    points = points - int(jimmyJohns)
    aPoints = points
    print("you havent spent all of your points!")
print("\n\ngreat! now it is time to go on an adventure")
while no == 0:
    no = 1
    print("one day you are playing the hit battle royal game called jimmy johns. while playing the game, you get double teamed, what do you do to live?")
    a = input("1.)crank some phat 90s\n2.)run away and hide\n3.)try to kill both of them\n")
    if int(a) == 1:
        if int(jimmyJohns) + (int(cheeseMaking) - 60) > random.randrange(0, 51):
            print("as you crank those 90s, you survive and then snipe both of them, and win the game")
        elif int(jimmyJohns) + (int(cheeseMaking) - 60) < random.randrange(0, 51):
            print("as you attempt to crank on them kids, one of them snipes you out of your build. out of pure hatred and rage you throw your controller at your mom and get grounded. you are unable to go on an adventure.")
    
    if int(a) == 2:
        if int(jimmyJohns) + (int(cheeseMaking) - 60) > random.randrange(0, 51):
            print("as you run away and hide, you come across a legendary chest, letting you double pump on them scrubs, and ultimately wining the game")
        elif int(jimmyJohns) + (int(cheeseMaking) - 60) < random.randrange(0, 51):
            print("as you run away and hide, one of them sees you and cracks your sheild. you see a legendary chest while running and go towards it, someone was camping the chest and kills you. you throw your controller at your mom in rage, getting you grounded, not being able to complete the adventure.")
    
    if int(a) == 3:
        if int(jimmyJohns) + (int(cheeseMaking) - 60) > random.randrange(0, 51):
            print("as you attempt to peak the two hekkers, you can pick one off with a rifle. the last person cracks your sheild, but you snipe em last second, winning the game.")
        elif int(jimmyJohns) + (int(cheeseMaking) - 60) < random.randrange(0, 51):
            print("the very milisecond, the very frame, as you peak, both of them snipe you. as you lose the game, out of rage you throw your controller at your mom, getting you grounded. you cannot complete the adventure anymore")

