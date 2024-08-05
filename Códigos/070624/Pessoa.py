class pessoa:
    def __init__(self, corDaPele, corDoCabelo, peso, altura , estaFeliz) -> None:
        self.corDaPele = corDaPele
        self.corDoCabelo = corDoCabelo
        self.peso = peso
        self.altura = altura
        self.estaFeliz = estaFeliz
        pass

    def pintarCabelo(self,strang):
        self.corDoCabelo = strang
    def imc(self):
        alturaTemp = self.altura * 2
        pesoTemp = self.peso
        return(pesoTemp / alturaTemp)
    def exercicio(self):
        self.peso -= 5
    def comer(self):
        self.peso += 10
    def jogaJogosDoEstudioBrasileiroOneShot(self,boolean):
        if(boolean):
            self.estaFeliz = True
        else:
            self.estaFeliz = False
def pog():
    print("pog")