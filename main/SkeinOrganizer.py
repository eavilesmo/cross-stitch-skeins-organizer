import sys

from main.SkeinConverter import SkeinConverter
from main.Presenter import Presenter
from main.SkeinRepository import SkeinRepository

skein_converter = SkeinConverter()
skein_repository = SkeinRepository()
presenter = Presenter()

while True:
    user_input = presenter.print_welcome()

    if user_input == "1":
        skein_number = presenter.ask_for_skein_number()
        print(skein_converter.convert_dmc_to_anchor(skein_number))
    elif user_input == "2":
        skein_number = presenter.ask_for_skein_number()
        print(skein_converter.convert_anchor_to_dmc(skein_number))
    elif user_input == "3":
        file_path = presenter.ask_for_file_path()
        skein_converter.convert_dmc_to_anchor_in_bulk(file_path)
    elif user_input == "4":
        skein_number = presenter.ask_for_skein_number()
        skein_repository.find_skein(skein_number)
    elif user_input == "5":
        file_path = presenter.ask_for_file_path()
        skein_repository.find_skeins_in_bulk(file_path)
    elif user_input == "6":
        sys.exit()
    else:
        presenter.invalid_option()
