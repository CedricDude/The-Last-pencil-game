def john_take():
    while True:
        temp = input()
        if not (temp.isdigit()) or temp not in ['1', '2', '3']:
            print("Possible values: '1', '2' or '3'")
            continue

        elif int(temp) > no_of_pencils:
            print("Too many pencils were taken")
            continue
        return int(temp)


print("How many pencils would you like to use:")
while True:
    temp = input()
    if temp.isdigit():
        if int(temp) == 0:
            print("The number of pencils should be positive")
            continue
        global no_of_pencils
        no_of_pencils = int(temp)
        break
    else:
        print("The number of pencils should be numeric")

print("Who will be the first (John, Jack):")
while True:
    temp = input()
    if temp != "John" and temp != "Jack":
        print("Choose between 'John' and 'Jack'")
        continue
    else:
        current_player = temp
        break


print("|" * no_of_pencils)
print("{}'s turn:".format(current_player))
while True:
    if current_player == "John":
        take_out = john_take()

    else:
        if no_of_pencils % 4 == 1:
            take_out = 1
        elif no_of_pencils % 4 == 0:
            take_out = 3
        elif no_of_pencils % 4 == 2:
            take_out = 1
        else:
            take_out = 2
        print(take_out)

    no_of_pencils -= take_out
    if no_of_pencils == 0:
        if current_player == "John":
            print("{} won!".format("Jack"))
        else:
            print("{} won!".format("John"))
        break
    else:
        print("|" * no_of_pencils)
        if current_player == "John":
            print("{}'s turn:".format("Jack"))
            current_player = "Jack"
        elif current_player == "Jack":
            print("{}'s turn:".format("John"))
            current_player = "John"
