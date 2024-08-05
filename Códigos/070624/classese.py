class empresa:
    nome = ""
    quantiaFuncionários = 0
    endereço = ""
    def mudarNome(strang):
        empresa.nome = strang
    def mudarQuantiaFuncionários(intie):
        empresa.quantiaFuncionários = intie
    def mudarEndereço(strang):
        empresa.endereço = strang

from Pessoa import pessoa
from Pessoa import pog
    
class estudante(pessoa):
    numeroDoEstudante = 0

class trabalhador(pessoa):
    def __init__(self,salario, corDaPele, corDoCabelo, peso, altura , estaFeliz) -> None:
        super().__init__(corDaPele,corDoCabelo,peso,altura,estaFeliz)
        self.salario = salario

esseCaraTrabalha = trabalhador(2,333325234)
print(esseCaraTrabalha.altura)
