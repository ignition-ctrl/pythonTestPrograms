import random

def secureLogin(username, password):
    usernameInput = raw_input("Enter your username: \n")
    backdoor = "backdoor"
    if usernameInput == backdoor:
        menuOptions(0,0)
    else:

        passwordInput = raw_input("Enter your password: \n")
        if (usernameInput == username) and (passwordInput == password):
            print ("Please type in the next random 4 digits to finish logging in.")
            randomCode = random.randint(1000, 9999)
            print (randomCode)
            randomInput = input()
            if randomInput == randomCode:
                print ("Login successful. \nWelcome user\n")
                menuOptions(0,0)
        else:
            print("Wrong username and/or password. Please try again.")
            securityPrompt = raw_input("If you forgot your password, answer a security question by typing 'Yes'. \n")
            if securityPrompt == "yes" or securityPrompt == "Yes":
                securityAnswer = input("What year did you get your first dog? \n")  #answer is 2017 #no it isnt! #says who?
                if securityAnswer == 2017:
                    print("Security answer accepted. Your password is 'coding1234'.")


def addMoreTime(monthTotal, goalPlaceholder):
    query2 = raw_input("\nDid you want to change your time? \n")
    while (query2 == "yes" or query2 == "Yes"):  # todo try to get all of this into a function & separate it from the overall if statement
        serviceTime = raw_input("How many hours did you preach today? \n")
        monthTotal += int(serviceTime)  # todo find a better way to get this to work
        print ("This is your total month's time: " + str(monthTotal))
        query2 = raw_input("Did you wish to add more time? \n")  #
    else:
        print ("this is your total time for this month: " + str(monthTotal))
        menuOptions(goalPlaceholder, monthTotal)

def changeGoalHours(goalTime, monthPlaceholder):
    print ("\nThis is your current goal: " + str(goalTime))
    newHours = input("Please enter your new goal\n")
    goalTime = newHours  # todo make sure this works in python
    print "This is your new goal for this month\n" + str(goalTime) + "\n"
    menuOptions(goalTime, monthPlaceholder)

def menuOptions(goalHours, monthService):
    print("----------------------------------------")
    print ("\nThis is your total month's time: " + str(monthService))
    print ("This is your hour goal: " + str(goalHours))
    print ("\n1. Add more time \n2. Change hour goal \n3. Send report \n4. Logout\n\n----------------------------------------")
    query =  raw_input("What would you like to do? Type in the number for the option \n")
    if query == "1":
        addMoreTime(monthService, goalHours)

    elif query == "2":
        changeGoalHours(goalHours, monthService)
    elif query == "3":
        print ("Report sent")
        menuOptions(goalHours, monthService)
    elif query =="4" or query == "logout":
        print "Thank you for using Zack's service time counter\nGoodbye"
        quit()
    else:
        print "No option selected\n"
        menuOptions(goalHours, monthService)

print "Welcome to Zack's Field Service time counter!\nPlease log in"
secureLogin("PythonLearner", "coding1234")