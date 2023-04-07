from main.ConversionListInitializer import ConversionListInitializer


class SkeinConverter:
    conversionListInitializer = ConversionListInitializer()
    conversion_list = conversionListInitializer.initialize()

    def convert_dmc_to_anchor(self, skein_number):
        for key, value in self.conversion_list.items():
            if value == skein_number:
                return key

    def convert_anchor_to_dmc(self, skein_number):
        return self.conversion_list[skein_number]

    def convert_dmc_to_anchor_in_bulk(self, file_path):
        with open(file_path, 'r') as skeins_file:
            for line in skeins_file:
                line = line.rstrip()
                self.convert_dmc_to_anchor(line)
                if not line:
                    continue
