class Bicicleta:

    # Construtor
    def __init__(self, cor, modelo, ano, valor):
        print(f"Criando objeto... Bicicleta {cor}")
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    # Desrutor
    def __del__(self):
        print(f"Destruindo objeto... Bicicleta {self.cor}")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def buzinar(self):
        print(f"Plim plim... Bicicleta {self.cor}")

##############################################################################################################################

def criar_bicicleta():
    b = Bicicleta("azul", "caloi", 2024, 1500)
    print(b.cor)
    return b

##############################################################################################################################

print()

# Construtor
b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b2 = criar_bicicleta()

print()

# Chamada de método
b1.buzinar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)
print(b1) # Comente o método __str__ e teste isso novamente...

print()

# Destrutor

print("Ola mundo")

del b2

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

print()