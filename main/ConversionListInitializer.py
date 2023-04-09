class ConversionListInitializer:
    def initialize(self):
        with open('resources/conversion_list.txt', 'r') as conversion_file:
            conversion_list = {}
            for line in conversion_file:
                skein_numbers = line.strip().split('\t')
                anchor_skein = skein_numbers[0]
                dmc_skein = skein_numbers[1]
                conversion_list[anchor_skein] = dmc_skein
        return conversion_list
