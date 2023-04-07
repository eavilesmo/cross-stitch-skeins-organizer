class ThreadConverter:

    def convert_dmc_to_anchor(self, skein_number, conversion_list):
        for key, value in conversion_list.items():
            if value == skein_number:
                return key

    def convert_anchor_to_dmc(self, skein_number, conversion_list):
        return conversion_list[skein_number]

    def convert_dmc_to_anchor_in_bulk(self, file_path, conversion_list):
        with open(file_path, 'r') as skeins_file:
            for line in skeins_file:
                line = line.rstrip()
                self.convert_dmc_to_anchor(line, conversion_list)
                if not line:
                    continue