for attempts_left in range(3, 0, -1):
     password = input("Enter your password" "(you have {} attempts left): ".format(attempts_left))
    if password == "85563and":
        print("Acces granted")
        break
else:
    print("Acces denied")

