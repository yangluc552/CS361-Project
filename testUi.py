import time
import os

while True:
    choice = input("Enter 1 to generate a random quote or 2 to exit: ")
    if choice == "1":
        try:
            fileToProcess = open("quote.txt", "w") 
            fileToProcess.write("run\n")
        except IOError:
            print("Could not open file!")
            continue

        time.sleep(5)

        while True:         
            try:
                fileToProcess = open("quote.txt", "r") 
                randomQuote = fileToProcess.readline().strip()
                time.sleep(2)
                print("The Random Quote is: ", randomQuote) 
                if randomQuote != "run":
                    break
            except IOError:
                print("Could not open file!")
            continue

    elif choice == "2":
        break
    else:
        print("Unknown option")

