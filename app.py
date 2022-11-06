#'hamburger creator' adapted for python
#original project: https://https://scratch.mit.edu/projects/44733420/
#original written in scratch by hibot (http://hibot3000.com)
#python version written by zycone (https://zycone.neocities.org)
#requires python 3.10 (https://www.python.org/downloads/release/python-3100/)


import time

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# now, to clear the screen (taken from stackoverflow)
cls()

#import os is cross-platform

#information goes here

time.sleep(1)
print("hamburger creator for python")
time.sleep(1)   #from stackoverflow
print("\n")

#time for the meat ( ͡° ͜ʖ ͡°)

print("pick your meat")
print("beef, chicken, veggie?")
meat = input()

meat1 = ["Beef","beef"]
meat2 = ["Chicken","chicken"]
meat3 = ["Veggie","veggie"]

if meat in meat1:
    print("you put beef as your meat")
elif meat in meat2:
    print("you put chicken as your meat")
elif meat in meat3:
    print("you put veggie as your meat, it ain't a meat anymore innit")
else:
    print("that's not a thing, thank you for corrupting mcdonalds you're fired")
    input()
    quit()
#"i still don't know why the or statements failed so epicly" ~hibot

#veggie time

print("\n")
print("pick your vegetables")
print("lettuce, tomato, both or none?")
vegetable = input()

vegetable1 = ["lettuce","Lettuce"]
vegetable2 = ["tomato","Tomato"]
vegetable3 = ["both","Both"]
vegetable4 = ["none","None"]

if vegetable in vegetable1:
    print("you picked lettuce as your vegetables")
elif vegetable in vegetable2:
    print("you picked tomato as your vegetables")
elif vegetable in vegetable3:
    print("you picked both tomato and lettuce as your vegetables")
elif vegetable in vegetable4:
    print("carnivore ain't picking any vegetables eh")
else:
    print("that's not a thing, thank you for corrupting mcdonalds you're fired")
    input()
    quit()

#cheese time

print("\n")
print("would you like some cheese?")
print("yes or no?")
cheese = input()

cheese1 = ["yes","Yes"]
cheese2 = ["no","No"]

if cheese in cheese1:
    print("you put a slice of cheese")

    print("\n")
    print("would you like to make it double?")
    print("yes or no?")
    doublecheese = input()

    doublecheese1 = ["yes","Yes"]
    doublecheese2 = ["no","No"]

    if doublecheese in doublecheese1:
        print("double cheese activated")
    elif doublecheese in doublecheese2:
        print("double cheese inactivated")
    else:
        print("that's not a thing, thank you for corrupting mcdonalds you're fired")
        input()
        quit()

elif cheese in cheese2:
    print("no cheese today :()")
    doublecheese = None
else:
    print("that's not a thing, thank you for corrupting mcdonalds you're fired")
    input()
    quit()

#bacon time

print("\n")
print("would you like some bacon?")
print("yes or no?")
bacon = input()

bacon1 = ["yes","Yes"]
bacon2 = ["no","No"]

if bacon in bacon1:
    print("you put some slices of bacon")
elif bacon in bacon2:
    print("thank you for not contributing to the clogging of your arteries")
else:
    print("that's not a thing, thank you for corrupting mcdonalds you're fired")
    input()
    quit()

#pickle time

print("\n")
print("would you like some pickles?")
print("yes or no?")
pickles = input()

pickles1 = ["yes","Yes"]
pickles2 = ["no","No"]

if pickles in pickles1:
    print("you put some slices of the pickle")
elif pickles in pickles2:
    print("no pickle today :(")
else:
    print("that's not a thing, thank you for corrupting mcdonalds you're fired")
    input()
    quit()

#sauce time

print("\n")
print("would you like some sauce?")
print("yes or no?")
sauceA = input()

sauceA1 = ["yes","Yes"]
sauceA2 = ["no","No"]

if sauceA in sauceA1:
    print("what sauce would you like?")
    print("ketchup, mustard, or mayonnaise?")
    sauceB = input()

    sauceB1 = ["ketchup","Ketchup"]
    sauceB2 = ["mustard","Mustard"]
    sauceB3 = ["mayonnaise","Mayonnaise","mayo","Mayo","mayonez","Mayonez"]
    sauceB4 = ["no","No","none","None"]

    if sauceB in sauceB1:
        print("you squeezed some ketchup on your burger")
    elif sauceB in sauceB2:
        print("you squeezed some mustard on your burger")
    elif sauceB in sauceB3:
        print("you squeezed some mayonnaise on your burger")
    elif sauceB in sauceB4:
        print("too late lol, thank you for corrupting mcdonalds you're fired")
        input()
        quit()
    else:
        print("that's not a thing, thank you for corrupting mcdonalds you're fired")
        input()
        quit()

elif sauceA in sauceA2:
    print("no sauce today :(")
    sauceB = "false"
else:
    print("that's not a thing, thank you for corrupting mcdonalds you're fired")
    input()
    quit()

#double bun

print("\n")
print("would you like another bun with that?")
doublebun = input()

doublebun1 = ["yes","Yes"]
doublebun2 = ["no","No"]

if doublebun in doublebun1:
    print("you placed a second middle bun")
    secondingredients = "true"
elif doublebun in doublebun2:
    print("you've skipped to the top bun")
    secondingredients = "false"
else:
    print("that's not a thing, thank you for corrupting mcdonalds you're fired")
    input()
    quit()

#double ingredients from here

if secondingredients == "true":
    print("\n")
    print("the following are the second ingredients")
    time.sleep(1)
    #here be the second ingredients (lit. ctrl+c, ctrl+v)
    #meat, veggie and cheese only (no bacon, pickles, sauce)
    #meat time ( ͡° ͜ʖ ͡°)

    print("\n")
    print("pick your meat")
    print("beef, chicken, veggie?")
    meatS = input()

    meatS1 = ["Beef","beef"]
    meatS2 = ["Chicken","chicken"]
    meatS3 = ["Veggie","veggie"]

    if meatS in meatS1:
        print("you put beef as your meat")
    elif meatS in meatS2:
        print("you put chicken as your meat")
    elif meatS in meatS2:
        print("you put veggie as your meat, it ain't a meat anymore innit")
    else:
        print("that's not a thing, thank you for corrupting mcdonalds you're fired")
        input()
        quit()

    #veggie time

    print("\n")
    print("pick your vegetables")
    print("lettuce, tomato, both or none?")
    vegetableS = input()

    vegetableS1 = ["lettuce","Lettuce"]
    vegetableS2 = ["tomato","Tomato"]
    vegetableS3 = ["both","Both"]
    vegetableS4 = ["none","None"]

    if vegetableS in vegetableS1:
        print("you picked lettuce as your vegetables")
    elif vegetableS in vegetableS2:
        print("you picked tomato as your vegetables")
    elif vegetableS in vegetableS3:
        print("you picked both tomato and lettuce as your vegetables")
    elif vegetableS in vegetableS4:
        print("carnivore ain't picking any vegetables eh")
    else:
        print("that's not a thing, thank you for corrupting mcdonalds you're fired")
        input()
        quit()

    #cheese time (no double cheese this time)

    print("\n")
    print("would you like some cheese?")
    print("yes or no?")
    cheeseS = input()

    cheeseS1 = ["yes","Yes"]
    cheeseS2 = ["no","No"]

    if cheeseS in cheeseS1:
        print("you put a slice of cheese")
    elif cheeseS in cheeseS2:
        print("no cheese today :()")
    else:
        print("that's not a thing, thank you for corrupting mcdonalds you're fired")
        input()
        quit()

    time.sleep(1)

    #rejoins for sesame bun

elif secondingredients == "false":
    print("\n")
    print("skipping to the top bun...")
    meatS = "false"
    vegetableS = "false"
    cheeseS = "false"
    time.sleep(1)

else:
    print("that's not a thing, thank you for corrupting mcdonalds you're fired")
    input()
    quit()

#sesame bun (finisher)

print("\n")
print("would you like a sesame or a plain bun?")
print("type 'sesame' or 'plain'")
sesamebun = input()

sesamebun1 = ["sesame","Sesame"]
sesamebun2 = ["plain","Plain"]

if sesamebun in sesamebun1:
    print("you placed a sesame bun")
elif sesamebun in sesamebun2:
    print("you placed a plain bun")
else:
    print("that's not a thing, thank you for corrupting mcdonalds you're fired")
    input()
    quit()

#"call your all new burger something!" prompt

print("\n")
print("call your all-new burger something!")
name = input()

print("\n")
print("loading commercial...")
print("use your imagination to create the visuals and audio")
time.sleep(1)
#gather variables: ctrl+r or lists.py

#commercial break
cls()

print("introducing the all new '"+ name +"' burger!")
time.sleep(0.5)
print("\n")

#meat
if meat in meat1:

    meatS1 = ["Beef","beef"]
    meatS2 = ["Chicken","chicken"]
    meatS3 = ["Veggie","veggie"]

    if meatS in meatS1:
        print("with two all-beef patties,")
    elif meatS in meatS2:
        print("with two patties of beef and chicken,")
    elif meatS in meatS3:
        print("with two patties of beef and the vegetable,")
    elif meatS == "false":
        print("with a juicy beef patty,")
    else:
        print("error")
        time.sleep(1)
        quit()
elif meat in meat2:

    meatS1 = ["Beef","beef"]
    meatS2 = ["Chicken","chicken"]
    meatS3 = ["Veggie","veggie"]

    if meatS in meatS1:
        print("with two patties of chicken and beef")
    elif meatS in meatS2:
        print("with two tender chicken patties,")
    elif meatS in meatS3:
        print("with two patties of chicken and the vegetable,")
    elif meatS == "false":
        print("with a tender chicken patty,")
    else:
        print("error")
        time.sleep(1)
        quit()
elif meat in meat3:

    meatS1 = ["Beef","beef"]
    meatS2 = ["Chicken","chicken"]
    meatS3 = ["Veggie","veggie"]

    if meatS in meatS1:
        print("with two patties of veggie and beef,")
    elif meatS in meatS2:
        print("with two patties of veggie and chicken,")
    elif meatS in meatS3:
        print("with two patties of the vegetable,")
    elif meatS == "false":
        print("with a patty of the vegetable,")
    else:
        print("error")
        time.sleep(1)
        quit()
else:
    print("error")
    time.sleep(1)
    quit()

time.sleep(0.5)
#vegetable

if vegetable in vegetable1:

    vegetableS1 = ["lettuce","Lettuce"]
    vegetableS2 = ["tomato","Tomato"]
    vegetableS3 = ["both","Both"]
    vegetableS4 = ["none","None"]

    if vegetableS in vegetableS1:
        print("and an awful ton of lettuce,")
    elif vegetableS in vegetableS2:
        print("and some delicate slices of the lettuce and tomato,")
    elif vegetableS in vegetableS3:
        print("and some lettuce and one slice of tomato,")
    elif vegetableS in vegetableS4:
        print("and with some lettuce at the bottom,")
    elif vegetableS == "false":
        print("and some lettuce at the bottom,")
    else:
        print("error")
        time.sleep(1)
        quit()
elif vegetable in vegetable2:

    vegetableS1 = ["lettuce","Lettuce"]
    vegetableS2 = ["tomato","Tomato"]
    vegetableS3 = ["both","Both"]
    vegetableS4 = ["none","None"]

    if vegetableS in vegetableS1:
        print("and some delicate slices of the tomato and lettuce,")
    elif vegetableS in vegetableS2:
        print("and an awful lot of the tomato,")
    elif vegetableS in vegetableS3:
        print("and some tomato with a flake of lettuce,")
    elif vegetableS in vegetableS4:
        print("and some tomato at the bottom,")
    elif vegetableS == "false":
        print("and some tomato at the bottom,")
    else:
        print("error")
        time.sleep(1)
        quit()
elif vegetable in vegetable3:

    vegetableS1 = ["lettuce","Lettuce"]
    vegetableS2 = ["tomato","Tomato"]
    vegetableS3 = ["both","Both"]
    vegetableS4 = ["none","None"]

    if vegetableS in vegetableS1:
        print("and some delicate slices of the lettuce with tomato at bottom,")
    elif vegetableS in vegetableS2:
        print("and some delicate slices of the tomato with lettuce at bottom,")
    elif vegetableS in vegetableS3:
        print("and a god awful ton of lettuce and tomato,")
    elif vegetableS in vegetableS4:
        print("and some lettuce and tomato at the bottom,")
    elif vegetableS == "false":
        print("and some lettuce and tomato,")
    else:
        print("error")
        time.sleep(1)
        quit()
elif vegetable in vegetable4:

    vegetableS1 = ["lettuce","Lettuce"]
    vegetableS2 = ["tomato","Tomato"]
    vegetableS3 = ["both","Both"]
    vegetableS4 = ["none","None"]

    if vegetableS in vegetableS1:
        print("and some lettuce of the top,")
    elif vegetableS in vegetableS2:
        print("and some tomato of the top,")
    elif vegetableS in vegetableS3:
        print("and a god awful ton of lettuce and tomato on the top,")
    elif vegetableS in vegetableS4:
        time.sleep(0.01)
    elif vegetableS == "false":
        time.sleep(0.01)
    else:
        print("error")
        time.sleep(1)
        quit()
else:
    print("error")
    time.sleep(1)
    quit()

time.sleep(0.5)
#cheese

if cheese in cheese1:

    doublecheese1 = ["yes","Yes"]
    doublecheese2 = ["no","No"]

    if doublecheese in doublecheese1:

        cheeseS1 = ["yes","Yes"]
        cheeseS2 = ["no","No"]

        if cheeseS in cheeseS1:
            print("three slices of cheese,")
        elif cheeseS in cheeseS2:
            print("two slices of cheese,")
        elif cheeseS == "false":
            print("two slices of cheese,")
        else:
            print("error")
            time.sleep(1)
            quit()
    elif doublecheese in doublecheese2:

        cheeseS1 = ["yes","Yes"]
        cheeseS2 = ["no","No"]

        if cheeseS in cheeseS1:
            print("two slices of cheese,")
        elif cheeseS in cheeseS2:
            print("a slice of cheese,")
        elif cheeseS == "false":
            print("a slice of cheese,")
        else:
            print("error")
            time.sleep(1)
            quit()
    else:
        print("error")
        time.sleep(1)
        quit()
elif cheese in cheese2:
    time.sleep(0.01)

else:
    print("error")
    time.sleep(1)
    quit()

time.sleep(0.5)
#bacon

if bacon in bacon1:
    print("some slices of the bacon,")
elif bacon in bacon2:
    time.sleep(0.01)
else:
    print("error")
    time.sleep(1)
    quit()

time.sleep(0.5)
#pickles

if pickles in pickles1:
    print("some slices of the pickles,")
elif pickles in pickles2:
    time.sleep(0.01)
else:
    print("error")
    time.sleep(1)
    quit()

time.sleep(0.5)
#sauces

if sauceA in sauceA1:

    sauceB1 = ["ketchup","Ketchup"]
    sauceB2 = ["mustard","Mustard"]
    sauceB3 = ["mayonnaise","Mayonnaise","mayo","Mayo","mayonez","Mayonez"]

    if sauceB in sauceB1:
        print("a generous amount of ketchup,")
    elif sauceB in sauceB2:
        print("a generous amount of mustard,")
    elif sauceB in sauceB3:
        print("a generous amount of mayonnaise,")
    else:
        print("error")
        time.sleep(1)
        quit()

elif sauceA in sauceA2:
    time.sleep(0.01)
else:
    print("error")
    time.sleep(1)
    quit()

time.sleep(0.5)
#double bun

if doublebun in doublebun1:
    print("a middle bun,")
elif doublebun in doublebun2:
    time.sleep(0.01)
else:
    print("error")
    time.sleep(1)
    quit()

time.sleep(0.5)
#top bun
if sesamebun in sesamebun1:
    print("all topped with a sesame-seed bun!")
elif sesamebun in sesamebun2:
    print("all topped with a white bun!")

time.sleep(1)
#miscallaneous (a.k.a rest of commercial)
print("\n")
print("buy now at our locations nationwide or via delivery and pay in 30,000 seconds time!")
time.sleep(0.5)
print("\n")
print("now at mcdonalds!")

#bullshit jingle
time.sleep(0.2)
print("ba")
time.sleep(0.2)
print("la")
time.sleep(0.2)
print("ba")
time.sleep(0.2)
print("ba")
time.sleep(0.2)
print("baaa~")

#exit prompt
time.sleep(0.2)
print("\n")
print("if you are done aweing at your creation, press enter to exit")
input()

cls()
print("thank you for playing")
print(":)")
print("\n")
print("v.1.1")
time.sleep(5)
exit()
