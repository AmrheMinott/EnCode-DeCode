'''

    This application created in pyhton was done for fun and aided in goal creation process.
    Variables (1)
        userInput: (String) -- this variable is what the user entered from the terminal

    What App Does:
        Takes a string passed in from the keyboard via user's input and encrpyts that value.
        There is also the ability of the app to decode the same thought and ideas that were added orignially.
'''



# string via user to encrpt is entered
userInput = input("\n\n\nEnter String to reverse: -> ")

option = input("\n\n\nDo you want to endode (y - encode n - decode). Enter option: -> ")


# encryption dictionary
# this dictionary is used to hold a few words that I personally know and use them in the encrptyion process
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


# the string that will be used to hold the values of the the string in the final result
builtString = " "

# if user does not enter exit as a value for the string
# then the loop will continue

# we encode here
if option == "y":
    # converts the string to lowercase
    userInput = userInput.lower();

    while userInput != "exit":
        # iterate through each word
        for word in userInput.split():
            # if the word is one of our encrypted word from memory then replace it from the origanl string
            if word in encrypt:
                builtString += (encrypt.get(word) + " ")
            else:
                builtString += (" E" + word + "E ")

        reverse = builtString[::-1]
        print(f"Your String reversed is \n\n-> {reverse}")
        userInput = input("\n\n\nEnter Another String to EnCode: -> ")
        userInput = userInput.lower();
        builtString = " "

else:
    # we decode here

    # infinite loop until user wants to leave
    while userInput != "exit":

        unverse = userInput.replace("E" , "")
        unverse = unverse.replace("$" , "")

        # filps the word backwards to undo reversing
        unverse = unverse[::-1]
        # iterate through each word
        for key, value in encrypt.items():
            for word in unverse.split():
                if word == value:
                    unverse = unverse.replace(word , value)

        print(f"Your Decoded String is \n {unverse}")

        userInput = input("\n\n\nEnter Another String to DeCode: -> ")
        userInput = userInput.lower();









# end of program
