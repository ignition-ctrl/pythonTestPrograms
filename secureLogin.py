import random




def secureLogin(username, password):
    usernameInput = raw_input("Enter your username: \n")
    passwordInput = raw_input("Enter your password: \n")
    if (usernameInput == username) and (passwordInput == password):
        print ("Please type in the next random 4 digits to finish logging in.")
        randomCode = random.randint(1000, 9999)
        print (randomCode)
        randomInput = input()
        if randomInput == randomCode:
            print ("Login successful. \nWelcome user")
    else:
        print("Wrong username and/or password. Please try again.")
        securityPrompt = raw_input("If you forgot your password, answer a security question by typing 'Yes'. \n")
        if securityPrompt == "yes" or securityPrompt == "Yes":
            securityAnswer = input("What year did you get your first dog? \n")  #answer is 2017 #no it isnt! #says who?
            if securityAnswer == 2017:
                print("Security answer accepted. Your password is 'coding1234'.")
            else: print("Security answer not accepted")

secureLogin("PythonLearner", "coding1234")
