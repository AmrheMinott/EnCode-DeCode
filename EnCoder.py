'''

    This application created in pyhton was done for fun and aided in goal creation process.
    Variables (1)
        userInput: (String) -- this variable is what the user entered from the terminal

    What App Does:
        Takes a string passed in from the keyboard via user's input and encrpyts that value.
        There is also the ability of the app to decode the same thought and ideas that were added orignially.
'''

import os
from datetime import datetime

# encryption dictionary
# this dictionary is used to hold a few words that I personally know and so I use them in the encrptyion process
encrypt = {

    "aspectos":"$aspectos$",

    "bien":"$bien$",

    "como":"$como$",
    "computador":"$computador$",
    "culturas":"$culturas$",

    "de":"$de$",
    "dinero":"$dinero$",

    "hablando":"$hablando$",

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

# get rid of and replace with regex
exitOptions = ['q', "quit", 'e', "exit"]

# this function takes a string as an input and applys the encoding procedure to the inputted string
def encode(userInput):
    # the string that will be used to hold the values of the the string in the final result
    builtString = " "

    # converts the string to lowercase
    userInput = userInput.lower()

    # iterate through each word
    for word in userInput.split():
        # if the word is one of our encrypted word from memory then replace it from the origanl string
        if word in encrypt:
            builtString += (encrypt.get(word) + " ")
        else:
            builtString += (" E" + word + "E ")

    # reverse the string and prints then returns it
    reverse = builtString[::-1]
    print(f"{reverse}")
    return reverse


# this function takes a string as an input and applys the encoding procedure in reverse to the inputted string
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

    # prints the decoded string and returns it
    print(f"{unverse}")
    return unverse


# this function takes a whole 
# str -> text       a whole text file as 
# str -> filename   the name of the file we got the orignial text from 
# int -> fileChoice and an integer that represents the file we are going to append to
def write_Decode_Encode(text, filename, fileChoice):

    now = datetime.now()

    # if the filename variable does not exists then we don't say the filename for the string var
    if filename == None:
        string = 'addition to was made on ' + str(now)
    else:
        string = 'addition to ' + filename + ' was made on ' + str(now)

    # this is the file we are going to open
    if fileChoice == 1:
        file = open('writeEncode.txt', 'a')
    else:
        file = open('writeDecode.txt', 'a')

    # we are writing the data in the file
    file.write(string)
    file.write('\n')
    file.write(text)
    file.write('end of addition \n\n')
    file.close()


def load(filename):
    path = os.getcwd()
    path = path + '/' + filename
    print(path)
    print(filename)

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
    mainMenuOption = ""
    userInput = ''

    while mainMenuOption != "3":

        print("Main Menu\n")

        mainMenuOption = input("strings (1) or a .txt file (2) or (3) to exit program ")

        # user enters string one by one
        if mainMenuOption == "1":

            while True:
                userInput = input("\n\n\nEnter String: -> ")
                if userInput.lower() == "exit": # if the user types and enters exit into the function we exit
                    break # to main menu
                option = input("(E -> encode or D -> decode or exit to return to main menu). Enter option: -> ")

                # since no text file was loaded then the parameter passed in None
                if option == "e" or option == "E":
                    write_Decode_Encode(encode(userInput), None, 1)
                elif option == "d" or option == "D":
                    write_Decode_Encode(decode(userInput), None, 2)
                elif option == 'exit':
                    break # to main menu


        # user loads an entire .txt file
        elif mainMenuOption == "2":

            while True:
                print("Enter name of file below or type exit to return to main menu")
                filename = input("Enter name of .txt file -> ")
                if filename.lower() in exitOptions: # if the user types and enters exit into the function we exit
                    break # to main menu
                print("This is the filename you entered " + filename)
                text = load(filename)
                

                # if the file does not exist then the 
                if text != "DUMMY_VALUE":
                    print("Information of the text file from the start is as follows")
                    print(text)
                    option = input("(E -> encode or D -> decode --> ")
                    # if user types in worng option we loop till they put in right option
                    while option != 'e' and option != 'E' and option != 'd' and option != 'D':
                        option = input("(E -> encode or D -> decode --> ")
                    result = ""
                    if option == "e" or option == "E":
                        print('Your String reversed is ->\n')
                        for sentence in text:
                            result += encode(sentence)
                            result += '\n'
                        write_Decode_Encode(result, filename, 1)
                    elif option == "d" or option == "D":
                        print('Your Decoded String is \n\n')
                        for sentence in text:
                            result += decode(sentence)
                            result += '\n'
                        write_Decode_Encode(result, filename, 2)
                else:
                    print("there is an error with the loading the file " + filename)


        elif mainMenuOption == "3" or mainMenuOption == "exit":
            break # out of the entire program


main()

# end of program
