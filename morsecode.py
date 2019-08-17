def pruf(scan, x=0):
    save = open("log","a")
    save.write(scan+":\n\n")
    for i in range(len(scan)):
        if scan[x] == " ":
            print("   ", end="")
            save.write("   ")
            x = x + 1
        elif scan[x] == "A" or scan[x] == "a":
            print("*-", end=" ")
            save.write("*- ")
            x = x + 1
        elif scan[x] == "B" or scan[x] == "b":
            print("-***", end=" ")
            save.write("-*** ")
            x = x + 1
        elif scan[x] == "C" or scan[x] == "c":
            print("-*-*", end=" ")
            save.write("-*-* ")
            x = x + 1
        elif scan[x] == "D" or scan[x] == "d":
            print("-**", end=" ")
            save.write("-** ")
            x = x + 1
        elif scan[x] == "E" or scan[x] == "e":
            print("*", end=" ")
            save.write("* ")

            x = x + 1
        elif scan[x] == "F" or scan[x] == "f":
            print("**-*", end=" ")
            save.write("**-* ")

            x = x + 1
        elif scan[x] == "G" or scan[x] == "g":
            print("--*", end=" ")
            save.write("--* ")

            x = x + 1
        elif scan[x] == "H" or scan[x] == "h":
            print("****", end=" ")
            save.write("**** ")

            x = x + 1
        elif scan[x] == "I" or scan[x] == "i":
            print("**", end=" ")
            save.write("** ")

            x = x + 1
        elif scan[x] == "J" or scan[x] == "j":
            print("*---", end=" ")
            save.write("*--- ")

            x = x + 1
        elif scan[x] == "K" or scan[x] == "k":
            print("-*-", end=" ")
            save.write("-*- ")

            x = x + 1
        elif scan[x] == "L" or scan[x] == "l":
            print("*-**", end=" ")
            save.write("*-** ")

            x = x + 1
        elif scan[x] == "M" or scan[x] == "m":
            print("--", end=" ")
            save.write("-- ")

            x = x + 1
        elif scan[x] == "N" or scan[x] == "n":
            print("-*", end=" ")
            save.write("-* ")

            x = x + 1
        elif scan[x] == "O" or scan[x] == "o":
            print("---", end=" ")
            save.write("--- ")

            x = x + 1
        elif scan[x] == "P" or scan[x] == "p":
            print("*--*", end=" ")
            save.write("*--* ")

            x = x + 1
        elif scan[x] == "Q" or scan[x] == "q":
            print("--*-", end=" ")
            save.write("--*- ")

            x = x + 1
        elif scan[x] == "R" or scan[x] == "r":
            print("*-*", end=" ")
            save.write("*-* ")

            x = x + 1
        elif scan[x] == "S" or scan[x] == "s":
            print("***", end=" ")
            save.write("*** ")

            x = x + 1
        elif scan[x] == "T" or scan[x] == "t":
            print("-", end=" ")
            save.write("- ")

            x = x + 1
        elif scan[x] == "U" or scan[x] == "u":
            print("**-", end=" ")
            save.write("**- ")

            x = x + 1
        elif scan[x] == "V" or scan[x] == "v":
            print("***-", end=" ")
            save.write("***- ")

            x = x + 1
        elif scan[x] == "W" or scan[x] == "w":
            print("*--", end=" ")
            save.write("*-- ")

            x = x + 1
        elif scan[x] == "X" or scan[x] == "x":
            print("-**-", end=" ")
            save.write("-**- ")

            x = x + 1
        elif scan[x] == "Y" or scan[x] == "y":
            print("-*--", end=" ")
            save.write("-*-- ")

            x = x + 1
        elif scan[x] == "Z" or scan[x] == "z":
            print("--**", end=" ")
            save.write("--** ")

            x = x + 1
        elif scan[x] == "1":
            print("*----", end=" ")
            save.write("*---- ")

            x = x + 1
        elif scan[x] == "2":
            print("**---", end=" ")
            save.write("**--- ")

            x = x + 1
        elif scan[x] == "3":
            print("***--", end=" ")
            save.write("***-- ")

            x = x + 1
        elif scan[x] == "4":
            print("****-", end=" ")
            save.write("****- ")

            x = x + 1
        elif scan[x] == "5":
            print("*****", end=" ")
            save.write("***** ")

            x = x + 1
        elif scan[x] == "6":
            print("-****", end=" ")
            save.write("-**** ")

            x = x + 1
        elif scan[x] == "7":
            print("--***", end=" ")
            save.write("--*** ")

            x = x + 1
        elif scan[x] == "8":
            print("---**", end=" ")
            save.write("---** ")

            x = x + 1
        elif scan[x] == "9":
            print("----*", end=" ")
            save.write("----* ")

            x = x + 1
        elif scan[x] == "0":
            print("-----", end=" ")
            save.write("----- ")

            x = x + 1
        else:
            print("Only Letters and Numbers!")
            break

    save.write("\n\n------------------------------------------------------------------------------------------")
    save.write("\n\n")
    save.close()
    print("\n")
