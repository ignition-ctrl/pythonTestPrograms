monthService = 0
goalHours = 0


print ("This is your total month's time: " + str(monthService))
print ("This is your hour goal: " + str(goalHours))
print ("1. Add more time \n 2. Change hour goal \n 3. Send report")
query =  raw_input("What would you like to do? Type in the number for the option \n")


if query == "1":
    query2 = raw_input("Did you want to change your time?")
    while (query == "yes" or query == "Yes"):
        serviceTime = raw_input("How many hours did you preach today? \n")
        monthService += int(serviceTime)
        print ("This is your total month's time: " + str(monthService))
        query = raw_input("Did you wish to add more time? \n")
    else:
        print ("this is your total time" + monthService)
elif query == "2":
    newHours = input("Please enter your new goal")
    goalHours = newHours
elif query == "3":
    print ("Report sent")

print (goalHours)
