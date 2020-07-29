import re

class Error(Exception):
    pass
class InvalidInput(Error):
    pass


def generate_random_password():
    """
    This function takes two words from the user, generates a random password
    using the words and returns the password.
    """
    print("To generate a password please enter two words 4-6 characters long each.")
    while True:
        try:
            word1 = input("Enter the first word: ")
            if len(word1) < 4 or len(word1) > 6:
                raise InvalidInput
            word2 = input("Enter the second word: ")
            if len(word2) < 4 or len(word2) > 6:
                raise InvalidInput

            tempPswd = []
            temp = re.findall(r"\b.", word1)
            tempPswd = temp
            temp = re.findall(r"\b.", word2)
            tempPswd.extend(temp)
            temp = re.findall(r"\B.\B", word1)
            tempPswd.extend(temp)
            temp = re.findall(r"\B.\B", word2)
            tempPswd.extend(temp)
            temp = re.findall(r".\b", word1)
            tempPswd.extend(temp)
            temp = re.findall(r".\b", word2)
            tempPswd.extend(temp)

            password = str(tempPswd)
            return "Your password is {}".format(password)

        except InvalidInput:
            print("Invalid entry! Please enter a word that is 4-6 characters long")



print(generate_random_password())

