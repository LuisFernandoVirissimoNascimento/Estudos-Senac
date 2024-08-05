class Reino:
    def __init__(self, Reino, Filo, Classe, Ordem, Familia, Genero, Especie) -> None:
        self.Reino = Reino
        self.Filo = Filo
        self.Classe = Classe
        self.Ordem = Ordem
        self.Familia = Familia
        self.Genero = Genero
        self.Especie = Especie

############################################### Reino dos animais ###############################################
class Animalia(Reino): # pegue caracteristicas unicas q pertencem a todos os animais, TODOS. lembre que peixes não tem pernas kkkk
    # Caracteristicas únicas que todos os animais possuem :
    # Nutrição : Carnivoro, Herbivoro ou Omnivoro.
    # Terreno de Atuação : Terrestre, Aquático ou Aviário.
    # Peso médio
    # Categoria de tamanho : Minusculo (Ratos e abaixo), Pequeno (Gatos), Médio (Leões), Grandes (Rinocerontes) e Enormes (Elefantes e acima.)
    # Estilo de Caça : Proativo (Predador), Oportunista (Hienas), Passivo (Corais) ou Reativo (Ambush, Cobras e Aranhas).
    # Velocidade Média
    # Velocidade Máxima
    def __init__(self, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial) -> None:
        super().__init__(Reino, Filo, Classe, Ordem, Familia, Genero, Especie)
        self.Nutrição = Nutrição
        self.Terreno = Terreno
        self.PesoMédio = PesoMédio
        self.Tamanho = Tamanho
        self.EstiloDeCaça = EstiloDeCaça
        self.VelocidadeMédia = VelocidadeMédia
        self.VelocidadeMáxima = VelocidadeMáxima
        self.NomeColoquial = NomeColoquial

    # Agora temos 25 animais para fazer, cada um com suas caracteristicas. Tentar pelo menos 5 caracteristicas por animals. e também 5 movimentos (defs).
    # 2 Equinodermos, 2 Cnidários, 2 Anfíbios, 2 Crustáceos, 3 Peixes, 2 Reptéis, 2 Aracnideos, 2 Aves, 2 Insetos, 2 Moluscos, 4 Mamíferos.
    # Equinodermos - Ouriço do mar e Estrela do Mar
class OuriçoDoMar(Animalia): # 1
    # Nosso caso vai ser o Ouriço-de-fogo (Astropyga radiata)
    # https://pt.wikipedia.org/wiki/Astropyga_radiata
    # Comprimento dos espinhos = 5 Cm 
    # É Venenoso = Sim
    # Local da boca = Face Oral (Inferior)
    # Quantia de dentes = 5
    def __init__(self, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial, ComprimentoDosEspinhos, Venenoso, LocalDaBoca, QuantiaDeDentes) -> None:
        super().__init__(Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial)
        self.ComprimentoDosEspinhos = ComprimentoDosEspinhos
        self.Venenoso = Venenoso
        self.LocalDaBoca = LocalDaBoca
        self.QuantiaDeDentes = QuantiaDeDentes

    def GrudarSuperficie():
        print("Se gruda a superficie atual, isso contribue também para simbiose com certos caranguejos.")
    def MirarEspinhos():
        print("Mira os espinhos em certa direção, por ser sensível a luz pode usar isso tanto para ataque quanto para defesa.")
    def SoltarOvosOuEsperma():
        print("Sendo seu método de reprodução, dependendo do sexo pode soltar ovos ou espermas na água para criar larvas que crescem no mar.")
    def Movimento():
        print("Se move utilizando suas minusculas e inúmeras patas que também servem para grudar.")

class EstrelaDoMar(Animalia): # 2
    # Nosso caso vai ser a Royal Starfish
    # https://en.wikipedia.org/wiki/Astropecten_articulatus
    # Quantia de braços = 5
    # É invasor = Não
    # Tem Espinhos = Não
    # É Canibal = Não
    def __init__(self, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial,  QuantiaDeBraços, Invasor, Espinhuda, Canibal) -> None:
        super().__init__(Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima,  NomeColoquial)
        self.QuantiaDeBraços = QuantiaDeBraços
        self.Invasor = Invasor
        self.Espinhuda = Espinhuda
        self.Canibal = Canibal
    def Movimento():
        print("Usa um sistema hidráulico com adesão para se mover pela superficie da água, sugando e empurrando água pelos seus milhares de pés.")
    def Regeneração():
        print("Regenera partes perdidas do corpo.")
    def AutoDestruiçãoDistração():
        print("Corta um de seus braços e foge rapidamente, deixando o braço cortado para distrair o predador.")
    def ReproduçãoPorSeparação():
        print("Se separa em dois, cada metade regenerando para criar uma nova estrela do mar.")
    # Cnidários - Água-viva e Anêmona-do-mar
class AguaViva(Animalia): # 3
    # Nosso caso vai ser a Lion's mane jellyfish
    # https://en.wikipedia.org/wiki/Lion%27s_mane_jellyfish
    # Diâmetro da Cabeça = 210 cm
    # É Venenoso = Sim
    # Comprimento do tentaculo = 3600 cm
    # É Canibal = Sim
    def __init__(self, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial,  DiametroDaCabeça, Venenoso, ComprimentoDoTentaculo, Canibal) -> None:
        super().__init__(Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima,  NomeColoquial)
        self.DiametroDaCabeça = DiametroDaCabeça
        self.Venenoso = Venenoso
        self.ComprimentoDoTentaculo = ComprimentoDoTentaculo
        self.Canibal = Canibal

    def CapturarPresa():
        print("Captura presas com seus tentáculos e as puxa de volta para a cabeça.")
    def Movimento():
        print("Se movimenta por uma fraca propulsão, dependendo de corrente maritma para mover longas distâncias.")
    def ReproduçãoPorPlantação():
        print("Após fertilização, são plantadas ''sementes'' no chão do mar, que crescem em uma torre que se separa por camadas, cada camada virando uma nova água-viva.")

class AnemonaDoMar(Animalia): # 4
    # Nosso caso vai ser Bubble-tip anemone 
    # https://en.wikipedia.org/wiki/Bubble-tip_anemone
    # É simbionte = Sim
    # Móvel = Não
    # QuantiaMédiaDeTentáculos = 30
    def __init__(self, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial,  Simbionte, Movel, QuantiaMédiaDeTentáculos) -> None:
        super().__init__(Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima,  NomeColoquial)
        self.Simbionte = Simbionte
        self.Movel = Movel
        self.QuantiaMédiaDeTentáculos = QuantiaMédiaDeTentáculos

    def CapturarPresa(self):
        print("Captura presas com seus tentáculos e as puxa para sua boca.")
    def ReproduçãoPorSeparação(self):
        print("Se reproduzem separando pedaços do corpo mas também por métodos sexuais como fertilização.")


    # Anfíbios - Axolotl e Potato Fairy
class Axolote(Animalia): # 5
    # Nosso caso vai ser o Axolotl mexicano
    # https://en.wikipedia.org/wiki/Axolotl
    # Cor após amadurecimento = Albino
    def __init__(self, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial,  CorPosMadurecimento) -> None:
        super().__init__(Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima,  NomeColoquial)
        self.CorPosMadurecimento = CorPosMadurecimento
    def Movimento():
        print("Movimento por natação")
    def Regeneração():
        print("Regeneração avançada de até mesmo partes do cerebro")
class Sapo(Animalia): # 6
    # Nosso caso vai ser o common rain frog ou Potato Fairy
    # https://en.wikipedia.org/wiki/Breviceps_adspersus
    # Tamanho do pulo = 0 cm
    # É Venenoso = não
    # Tamanho da lingua = Não estica
    # Pé é Palmado = não
    def __init__(self, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima,  NomeColoquial, TamanhoDoPulo, Venenoso, TamanhoDaLingua, PéPalmado) -> None:
        super().__init__(Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima,  NomeColoquial)
        self.TamanhoDoPulo = TamanhoDoPulo
        self.Venenoso = Venenoso
        self.TamanhoDaLingua = TamanhoDaLingua
        self.PéPalmado = PéPalmado

    def Cavar():
        print("Cava buracos para sua segurança.")
    def Nadar():
        print("Quase todas as espécies de sapo nada.")
    def Croak():
        print("Som que são conhecidos por fazer, no japão é diferente, sendo KeroKeroKero.")
    def Movimento():
        print("Movimentam pulando ou caminhando.")

    # Crustáceos - Caranguejo e Camarão
class Camarão(Animalia): # 7
    # Nosso caso vai ser o Peacock Mantis Shrimp ou Boxing lil guy
    # https://en.wikipedia.org/wiki/Odontodactylus_scyllarus
    # Coloração : Arco iris ou Azul
    # 
    def __init__(self, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial, Coloração) -> None:
        super().__init__(Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial)
        self.Coloração = Coloração    
    def Nadar():
        print("Se movem nadando.")

class Caranguejo(Animalia): # 8
    # Nosso caso vai ser o Peacock Mantis Shrimp ou Boxing lil guy
    # https://en.wikipedia.org/wiki/Odontodactylus_scyllarus
    # Coloração : Arco iris ou Azul
    def __init__(self, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial) -> None:
        super().__init__(Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial)

    # Peixes - Carp, Baiacu and Shark
class Carpa(Animalia): # 9
    # Nosso caso vai ser os Koi
    # https://en.wikipedia.org/wiki/Koi
    def __init__(self, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial) -> None:
        super().__init__(Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial)
    def Nadar():
        print("Se movem nadando.")

class Baiacu(Animalia): # 10
    # Nosso caso vai Golden Puffer
    # https://en.wikipedia.org/wiki/Arothron_meleagris
    def __init__(self, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial) -> None:
        super().__init__(Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial)
    def Nadar():
        print("Se movem nadando.")

class Tubarão(Animalia): # 11
    # Nosso caso vai ser Tubarão Baleia
    # https://en.wikipedia.org/wiki/Whale_shark
    def __init__(self, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial) -> None:
        super().__init__(Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial)
    def Nadar():
        print("Se movem nadando.")

# Reptéis - Crocodilo e Lagarto Monitor (Komodo)
class LagartoMonitor(Animalia): # 12
    # Nosso caso vai ser o Dragão Komodo
    # https://en.wikipedia.org/wiki/Komodo_dragon
    def __init__(self, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial) -> None:
        super().__init__(Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial)

class Crocodilo(Animalia): # 13
    # Nosso caso vai ser o Crocodilo Americano
    # https://en.wikipedia.org/wiki/American_crocodile
    def __init__(self, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial) -> None:
        super().__init__(Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial)

# Aracnideos - Aranha e Escorpião
class Aranha(Animalia): # 14
    # Nosso caso vai Viúva Negra
    # https://pt.wikipedia.org/wiki/Latrodectus
    def __init__(self, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial) -> None:
        super().__init__(Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial)

class Escorpião(Animalia): # 15
    # Nosso caso vai ser o Emperor Scorpion
    # https://en.wikipedia.org/wiki/Emperor_scorpion
    def __init__(self, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial) -> None:
        super().__init__(Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial)

# Aves - Eagles and Pigeons
class Aguia(Animalia): # 16
    # Nosso caso vai ser a Philippine Eagle
    # https://en.wikipedia.org/wiki/Philippine_eagle
    def __init__(self, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial) -> None:
        super().__init__(Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial)

class Pombo(Animalia): # 17
    # Nosso caso vai ser a Lahore Pigeon
    # https://en.wikipedia.org/wiki/Lahore_pigeon
    def __init__(self, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial) -> None:
        super().__init__(Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial)
# Insetos - Bees and Beetles
class Abelha(Animalia): # 18
    # Nosso caso vai Abelha de mel
    # https://en.wikipedia.org/wiki/Honey_bee
    def __init__(self, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial) -> None:
        super().__init__(Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial)

class Besouro(Animalia): # 19
    # Nosso caso vai Besouro Hercules
    # https://en.wikipedia.org/wiki/Hercules_beetle
    def __init__(self, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial) -> None:
        super().__init__(Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial)

# Moluscos - Squids and Octopus,
class Polvo(Animalia): # 20
    # Nosso caso vai blue ringed octopus
    # https://en.wikipedia.org/wiki/Blue-ringed_octopus
    def __init__(self, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial) -> None:
        super().__init__(Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial)

class Lula(Animalia): # 21
    # Nosso caso vai Colossal Squid
    # https://en.wikipedia.org/wiki/Colossal_squid
    def __init__(self, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial) -> None:
        super().__init__(Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial)

# Mamiferos - Doggos, Bunnies, Catos, Horses
class Cachorros(Animalia): # 22
    # Nosso caso vai White Wolf
    # https://en.wikipedia.org/wiki/Arctic_wolf
    def __init__(self, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial) -> None:
        super().__init__(Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial)

class Coelho(Animalia): # 23
    # Nosso caso vai ser o Coelho Gigante de Flemish
    # https://en.wikipedia.org/wiki/Flemish_Giant_rabbit
    def __init__(self, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial) -> None:
        super().__init__(Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial)

class Gato(Animalia): # 24
    # Nosso caso vai Rusty Tiniest Cat
    # https://en.wikipedia.org/wiki/Rusty-spotted_cat
    def __init__(self, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial) -> None:
        super().__init__(Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial)

class Cavalo(Animalia): # 25
    # Nosso caso vai Shire
    # https://pt.wikipedia.org/wiki/Shire_(cavalo)
    def __init__(self, Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial) -> None:
        super().__init__(Reino, Filo, Classe, Ordem, Familia, Genero, Especie, Nutrição, Terreno, PesoMédio, Tamanho, EstiloDeCaça, VelocidadeMédia, VelocidadeMáxima, NomeColoquial)


############################################### Reino dos cogumelos ###############################################
# class Fungi(Reino):
#     def bah():
#         pass
# ############################################### Reino das plantas ###############################################
# class Plantae(Reino):
#     def bah():
#         pass
# ############################################### Reino dos Com Nûcleo(Protista) ###############################################
# class Protista(Reino):
#     def bah():
#         pass
# ############################################### Reino dos Sem Nûcleo (Monera) ###############################################
# class Monera(Reino):
#     def bah():
#         pass
