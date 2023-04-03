from main.ConversionListInitializer import ConversionListInitializer
from main.DmcToAnchorConversionList import dmc_to_anchor_list
from main.ThreadConverter import ThreadConverter
from main.Presenter import Presenter

thread_converter = ThreadConverter()

conversionListInitializer = ConversionListInitializer()
conversion_list = conversionListInitializer.initialize()

presenter = Presenter()
user_input = presenter.print_welcome()

if user_input == "1":
    thread_number = presenter.ask_for_thread_number()
    print(thread_converter.convert_dmc_to_anchor(thread_number, conversion_list))

elif user_input == "2":
    thread_number = presenter.ask_for_thread_number()
    print(thread_converter.convert_anchor_to_dmc(thread_number, conversion_list))


