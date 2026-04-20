class A:
    def __init__(self):
        self.A1 = 0      # Atributo int [cite: 42]
        self.A2 = 0.0    # Atributo float [cite: 42]

    # Gets e Sets [cite: 45]
    def get_A1(self): return self.A1
    def set_A1(self, valor): self.A1 = valor

    def get_A2(self): return self.A2
    def set_A2(self, valor): self.A2 = valor

    # Métodos solicitados [cite: 45]
    def MA1(self):
        print("Método MA1") # Imprime nome do método [cite: 47]

    def MA2(self):
        print("Método MA2") # Imprime nome do método [cite: 47]

    def MA3(self):
        print("Alteração a classe A partir do clone")
        