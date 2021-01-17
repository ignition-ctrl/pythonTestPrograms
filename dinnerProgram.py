momMakingDinner = False
meBeingHungry = True
momMadeSopes = False
momMadeSalad = False

if momMakingDinner and meBeingHungry:
    print("that smells good mom!")
    if momMadeSopes:
        print ("oh man, thanks mom!")
    elif momMadeSalad:
        print ("really, mom?")
elif momMakingDinner and not meBeingHungry:
    print("hey mom, I think I'll pass")
elif not momMakingDinner and meBeingHungry:
    print("hey mom, can you make dinner?")
else:
    print("is anyone hungry?")
