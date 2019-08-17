import morsecode

print('For help type "?" or "help()"')
print("Translate into Morsecode:")
while True:
    x = input("> ")
    if x == "exit()" or x == "quit()" or x == "stop()" or x == "e()" or x == "q()" or x == "s()":
        print("Bye Bye")
        break

    elif x == "help()" or x == "?":
        print("1. The lenght of a dot is one unit.")
        print("2. A dash is three units.")
        print("3. The Space between parts of the same letter is one unit.")
        print("4. The Space between letters is three units.")
        print("5. The Space between words is seven units.")
        print('6. To see the log type "log()".')
        print('7. To reset the log type "log().clear"')
        print('8. To exit type "exit()" or "e()".\n')
        continue

    elif x == "log()":
        file = open("log", "r")
        print("------------------------------------------------------------------------------------------")
        print(file.read())
        file.close()

    elif x == "log().clear" or x == "log().reset":
        print("Are you sure?")
        quest = input("y / n\n> ")
        if quest == "y":
            file = open("log", "w")
            file.close()
            print("The log has been reset!\n")
        else:
            print("The log has not been deleted!\n")

    else:
        morsecode.pruf(x)
