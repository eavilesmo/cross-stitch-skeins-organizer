class ThreadConverter:

    def convert_dmc_to_anchor(self, thread_number, conversion_list):
        for clave, valor in conversion_list.items():
            if valor == thread_number:
                return clave

    def convert_anchor_to_dmc(self, thread_number, conversion_list):
        return conversion_list[thread_number]

