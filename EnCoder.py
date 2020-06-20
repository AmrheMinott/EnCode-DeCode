'''

    This application created in pyhton was done for fun and aided in goal creation process.
    Variables (1)
        userInput: (String) -- this variable is what the user entered from the terminal

    What App Does:
        Takes a string passed in from the keyboard via user's input and encrpyts that value.
        There is also the ability of the app to decode the same thought and ideas that were added orignially.
'''


import os


# encryption dictionary
# this dictionary is used to hold a few words that I personally know and so I use them in the encrptyion process
encrypt = {
    "aspectos":"$aspectos$",

    "bien":"$bien$",

    "computador":"$computador$",
    "culturas":"$culturas$",

    "de":"$de$",
    "dinero":"$dinero$",

    "hablando":"$hablando$",
    "como":"$como$",

    "letra":"$letra$",
    "letras":"$letras$",

    "ninos":"$ninos$",

    "persona":"$persona$",
    "proteccion":"$proteccion$",

    "quien":"$quien$",

    "realizacion":"$realizacion$",
    "real":"$real$",

    "y":"$y$"
}

def encode(userInput):
    # the string that will be used to hold the values of the the string in the final result
    builtString = " "

    # converts the string to lowercase
    userInput = userInput.lower();

    # iterate through each word
    for word in userInput.split():
        # if the word is one of our encrypted word from memory then replace it from the origanl string
        if word in encrypt:
            builtString += (encrypt.get(word) + " ")
        else:
            builtString += (" E" + word + "E ")

    # reverse the string
    reverse = builtString[::-1]
    print(f"{reverse}")




def decode(userInput):
    # we decode here
    unverse = userInput.replace("E" , "")
    unverse = unverse.replace("$" , "")

    # flips the word backwards to undo reversing
    unverse = unverse[::-1]
    # iterate through each word
    for key, value in encrypt.items():
        for word in unverse.split():
            if word == value:
                unverse = unverse.replace(word , value)

    print(f"{unverse}")


def load(filename):
    print('getcwd:      ', os.getcwd())
    print('__file__:    ', __file__)
    path = os.getcwd()
    path = path + '/' + filename
    print(path)

    # in the event of an error we say the file could not be found and we return a dummy value
    try:
        file = open(filename, 'r')
        read = file.readlines()
        file.close()
        return read
    except FileNotFoundError:
        print("file is not found try again")
        return "DUMMY_VALUE"






def main():
    # string via user to encrpt is entered
    mainMenuOption = ""
    userInput = ''

    while mainMenuOption != "3":

        print("Main Menu\n ")

        mainMenuOption = input("strings (1) or a .txt file (2) or (3) to exit program ")

        if mainMenuOption == "1":
            
            while userInput != "exit":
                userInput = input("\n\n\nEnter String: -> ")
                if userInput == "exit":
                    break
                option = input("\n\n\n(E -> encode or D -> decode or exit to return to main menu). Enter option: -> ")

                if option == "e" or option == "E":
                    encode(userInput)
                elif option == "d" or option == "D":
                    decode(userInput)
                elif option == 'exit': # not really needed tbh
                    break

        elif mainMenuOption == "2":

            while True:
                print("Enter name of file below or type exit to return to main menu")
                filename = input("Enter name of .txt file -> ")
                if filename == "exit":
                    break # to main menu
                print("This is the filename you entered " + filename)
                text = load(filename)
                print("Information of the text file from the start is as follows")
                print(text)
                if text != "DUMMY_VALUE":
                    option = input("(E -> encode or D -> decode")
                    if option == "e" or option == "E":
                        print('Your String reversed is \n\n->')
                        for sentence in text:
                            encode(sentence)
                    elif option == "d" or option == "D":
                        print('Your Decoded String is \n')
                        for sentence in text:
                            decode(sentence)


        elif mainMenuOption == "3" or mainMenuOption == "exit":
            break # out of the entire program


main()

# end of program
