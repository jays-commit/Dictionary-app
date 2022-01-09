import json
import difflib

while True:

    word = input("Enter Word: ")
    if word == "/quit":
        break

    # print(translate(word))

    cont = input("\nWould you like to continue? Y/N\n")
    cont = cont.lower()
    if cont == "y":
        continue

    if cont == "n":
        break

print("Session has ended")