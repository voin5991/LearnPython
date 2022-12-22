attempts_left = 3
while attempts_left > 0:
    attempts_left -= 1
    password = input("Enter your password" "(you have {} attempts left): ".format(attempts_left + 1))
    if password == "85563and":
        print("Acces granted")
        break
else:
    print("Acces denied")
