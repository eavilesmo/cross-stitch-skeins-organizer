class SkeinRepository:
    dmc_skeins_available = {}
    anchor_skeins_available = {}

    def find_skein(self, skein_number):
        self.initialize_skein_collections()
        if skein_number in self.dmc_skeins_available:
            message = "You have the skein number {} for DMC and you have {} skeins available"
            print(message.format(skein_number, self.dmc_skeins_available[skein_number]))
        if skein_number in self.anchor_skeins_available:
            message = "You have the skein number {} for Anchor and you have {} skeins available"
            print(message.format(skein_number, self.anchor_skeins_available[skein_number]))

    def find_skeins_in_bulk(self, file_path):
        with open(file_path, 'r') as skeins_file:
            for line in skeins_file:
                line = line.rstrip()
                self.find_skein(line)
                if not line:
                    continue

    def initialize_skein_collections(self):
        with open('resources/dmc_skeins.txt', 'r') as dmc_skeins_file:
            for line in dmc_skeins_file:
                line = line.strip()
                if not line:
                    continue
                key, value = line.split(',')
                self.dmc_skeins_available[key] = value
        with open('resources/anchor_skeins.txt', 'r') as anchor_skeins_file:
            for line in anchor_skeins_file:
                line = line.strip()
                if not line:
                    continue
                key, value = line.split(',')
                self.anchor_skeins_available[key] = value
