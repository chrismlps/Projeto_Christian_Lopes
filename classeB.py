class B:
    def __init__(self):
        self.B1 = 0      # Atributo int [cite: 43]
        self.B2 = 0.0    # Atributo float [cite: 43]

    # Gets e Sets [cite: 45]
    def get_B1(self): return self.B1
    def set_B1(self, valor): self.B1 = valor

    def get_B2(self): return self.B2
    def set_B2(self, valor): self.B2 = valor

    # Métodos solicitados [cite: 46]
    def MB1(self):
        print("Método MB1") # Imprime nome do método [cite: 47]

    def MB2(self):
        print("Método MB2") # Imprime nome do método [cite: 47]
        