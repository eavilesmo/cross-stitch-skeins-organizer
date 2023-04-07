class Presenter:
    def print_welcome(self):
        print("Welcome to the program! What would you like to do?")
        print("1. Convert a DMC skein to Anchor")
        print("2. Convert an Anchor skein to DMC")
        print("3. Convert many DMC skeins to Anchor")
        print("3. Check if I have this skein available (only one skein)")
        print("4. Check if I have these skeins available (many skeins)")
        return input()

    def ask_for_skein_number(self):
        print("Please enter the number of the skein you want to convert:")
        return input()

    def ask_for_file_path(self):
        print("Please enter path to the file with the skeins' number")
        return input()

    def invalid_option(self):
        print("Sorry, that is not a valid option")
