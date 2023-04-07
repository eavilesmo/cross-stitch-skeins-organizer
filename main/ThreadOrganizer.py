from main.ConversionListInitializer import ConversionListInitializer
from main.ThreadConverter import ThreadConverter
from main.Presenter import Presenter
from main.ThreadRepository import ThreadRepository

thread_converter = ThreadConverter()
thread_repository = ThreadRepository()

conversionListInitializer = ConversionListInitializer()
conversion_list = conversionListInitializer.initialize()

presenter = Presenter()
user_input = presenter.print_welcome()

if user_input == "1":
    skein_number = presenter.ask_for_skein_number()
    print(thread_converter.convert_dmc_to_anchor(skein_number, conversion_list))

elif user_input == "2":
    skein_number = presenter.ask_for_skein_number()
    print(thread_converter.convert_anchor_to_dmc(skein_number, conversion_list))

elif user_input == "3":
    file_path = presenter.ask_for_file_path()
    thread_converter.convert_dmc_to_anchor_in_bulk(file_path, conversion_list)

elif user_input == "4":
    skein_number = presenter.ask_for_skein_number()
    thread_repository.find_thread(skein_number)

elif user_input == "5":
    file_path = presenter.ask_for_file_path()
    thread_repository.find_thread_in_bulk(file_path)

