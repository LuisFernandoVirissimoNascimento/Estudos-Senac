class Habilitacao:
    def __init__(self, tipo, descricao):
        self.tipo = tipo
        self.descricao = descricao

class Veiculo:
    def __init__(self, nome, tipo, habilitacao_necessaria=None):
        self.nome = nome
        self.tipo = tipo
        self.habilitacao_necessaria = habilitacao_necessaria
    
    def __str__(self):
        return f"{self.nome} - Tipo: {self.tipo}"

# Exemplo de uso:
# Vamos criar alguns tipos de habilitação comuns:
hab_b = Habilitacao("B", "Carro de passeio")
hab_a = Habilitacao("A", "Motocicleta")
hab_c = Habilitacao("C", "Caminhão")

# Agora vamos criar alguns veículos:
veiculos = [
    Veiculo("Civic", "Carro de passeio", habilitacao_necessaria=hab_b),
    Veiculo("CB 300", "Motocicleta", habilitacao_necessaria=hab_a),
    Veiculo("HRV", "Carro de passeio", habilitacao_necessaria=hab_b),
    Veiculo("Fusca", "Carro de passeio", habilitacao_necessaria=hab_b),
    Veiculo("BMW R 1250 GS", "Motocicleta", habilitacao_necessaria=hab_a),
    Veiculo("F-4000", "Caminhão", habilitacao_necessaria=hab_c),
    Veiculo("Uno", "Carro de passeio", habilitacao_necessaria=hab_b),
    Veiculo("PCX 150", "Motocicleta", habilitacao_necessaria=hab_a),
    Veiculo("Gol", "Carro de passeio", habilitacao_necessaria=hab_b),
    Veiculo("CG 160", "Motocicleta", habilitacao_necessaria=hab_a),
    Veiculo("Sprinter", "Caminhão", habilitacao_necessaria=hab_c),
    Veiculo("Onix", "Carro de passeio", habilitacao_necessaria=hab_b),
    Veiculo("Harley-Davidson Fat Boy", "Motocicleta", habilitacao_necessaria=hab_a),
    Veiculo("Ford Cargo", "Caminhão", habilitacao_necessaria=hab_c),
    Veiculo("Corolla", "Carro de passeio", habilitacao_necessaria=hab_b),
    Veiculo("XRE 300", "Motocicleta", habilitacao_necessaria=hab_a),
    Veiculo("Hilux", "Carro de passeio", habilitacao_necessaria=hab_b),
    Veiculo("CB 500X", "Motocicleta", habilitacao_necessaria=hab_a),
    Veiculo("Volvo FH", "Caminhão", habilitacao_necessaria=hab_c),
    Veiculo("Palio", "Carro de passeio", habilitacao_necessaria=hab_b),
    Veiculo("Andar","Humano")
]

# Exemplo de iteração para listar todos os veículos:
for veiculo in veiculos:
    print(veiculo)

# Exemplo de busca por veículos que requerem habilitação tipo A:
# print("\nVeículos que requerem habilitação tipo A:")
# for veiculo in veiculos:
#     if veiculo.habilitacao_necessaria and veiculo.habilitacao_necessaria.tipo == "A":
#         print(veiculo)
print("Selecione o veiculo que você quer e vá comprar !")
