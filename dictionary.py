import json
import difflib
import sys

data = json.load(open("data.json"))


def translate(word):
    """
    This function takes a word from the user and returns a string definition
    :param word: string input
    :return: returns string
    """
    word = word.lower()
    if word in data:
        new_word = "".join(data[word])
        return new_word
    else:
        suggest = difflib.get_close_matches(word, data.keys(), n=1)
        new_suggest = "".join(suggest)

        user_res = input("Did you mean {} instead? Enter Y if yes and" \
                         " N if no ".format(new_suggest))
        user_res = user_res.lower()
        if user_res == "y":
            return "".join(data[new_suggest])

        return "Word doesn't exist please double check spelling"


while True:

    word = input("Enter Word: ")
    if word == "/quit":
        break

    print(translate(word))

    while True:
        cont = input("\nWould you like to continue? Y/N\n")
        cont = cont.lower()
        if cont == "y":
            break

        elif cont == "n":
            sys.exit()

        else:
            continue


