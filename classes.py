class Pessoa():
    def __init__(self, nome, idade, comendo=False, falando=False, dormindo=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        self.dormindo = dormindo


    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def comer(self, comida):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        print(f'{self.nome} está comendo {comida}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def dormir(self):
        if self.dormindo:
            print(f"{self.nome} já está dormindo.")
            return

        if self.falando:
            print(f"{self.nome} não pode dormir falando.")
            return

        if self.comendo:
            print(f"{self.nome} não pode dormir se estiver comendo.")
            return

        print(f"{self.nome} está dormindo...")
        self.dormindo = True

    def parar_dormir(self):
        if not self.dormindo:
            print(f"{self.nome} não está dormindo.")
            return
        print(f"{self.nome} acordou.")
        self.dormindo = False
