class Presenter:
    def print_welcome(self):
        print("Welcome to the program! What would you like to do?")
        print("1. Convert a DMC thread to Anchor")
        print("2. Convert an Anchor thread to DMC")
        print("3. Know how many skeins I have for this color")
        return input()

    def ask_for_thread_number(self):
        print("Please enter the number of the skein you want to convert:")
        return input()
