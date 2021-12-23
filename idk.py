import random
import math
one = 0
two = 0
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
while one == 0:
    one = 1
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

while two == 0:
    two = 1
    print("after clapping everyone in jimmy johns, a giant troll tries to eat you, what do you do")
    b = input("1.)try and use strength to fight it\n2.)use your fire skill and burn it\n3.)offer the troll some cheese that you made earlier\n")
    if int(b) == 1:
        if int(strength) * math.sqrt((int(shadowFight2Ability) - 10) ** 2) + 1 > random.randrange(0, 21):
            print("you slay the troll, and are able to continue with your quest")
        elif int(strength) * math.sqrt((int(shadowFight2Ability) - 10) ** 2) + 1 < random.randrange(0, 21):
            print("the troll goes nom nom on you, and you die")
    
    if int(b) == 2:
        if int(fire) * math.sqrt((int(shadowFight2Ability) - 10) ** 2) + 1 > random.randrange(0, 21):
            print("you kill the troll in a fiery blaze, letting you continue your adventure")
        elif int(fire) * math.sqrt((int(shadowFight2Ability) - 10) ** 2) + 1 < random.randrange(0, 21):
            print("your fire is not enough to kill the troll, and you are chomped on. nom nom nom. you are died.")
    
    if int(b) == 3:
        if int(cheeseMaking) > 95:
            print("the troll said 'mmmmmm, tasty cheese, byee' you did it, you may continue with your quest")
        elif int(cheeseMaking) < 95:
            print("YOUR CHEESE LEVEL IS NOT ENOUGH YOU SHALL PERISHHHHHH")

