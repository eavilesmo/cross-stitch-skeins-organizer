class ConversionListInitializer:
    def initialize(self):
        with open('archivo.txt', 'r') as f:
            data = {}
            for line in f:
                parts = line.strip().split('\t')
                key = parts[0]
                value = parts[1]
                data[key] = value
        return data
