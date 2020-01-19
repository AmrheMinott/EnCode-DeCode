'''

    This application created in pyhton was done for fun and aided in goal creation process.
    Variables (1)
        userInput: (String) -- this variable is what the user entered from the terminal

    What App Does: Takes a string passed in from the keyboard via user's input and encrpyts that value.
'''



# string via user to encrpt is entered
userInput = input("\n\n\nEnter String to reverse: -> ")

option = input("\n\n\nDo you want to endode (y - encode n - decode). Enter option: -> ")



# encryption dictionary
encrypt = {
    "de":"$de$",
    "dinero":"$dinero$",
    "y":"$y$",
    "ninos":"$ninos$",
    "proteccion":"$proteccion$",
    "culturas":"$culturas$",
    "realizacion":"$realizacion$",
    "real":"$real$"
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
        builtString = " "

else:
    # we decode here

    while userInput != "exit":

        # EemanE  EymE  $euq$
        unverse = userInput.replace("E" , "")
        unverse = unverse.replace("$" , "")

        unverse = unverse[::-1]
        for key, value in encrypt.items():
            for word in unverse.split():
                if word == value:
                    unverse = unverse.replace(word , value)

        print(f"Your Decoded String is \n {unverse}")

        userInput = input("\n\n\nEnter Another String to DeCode: -> ")
