class Heroi:
    def __init__(self, tipo, ataque):
        self.tipo = tipo
        self.ataque = ataque     
    def escrever(self):
        print(f'O {self.tipo} atacou usando {self.ataque}')


selecao = input("Informe o seu tipo de Herói: ")
arma = "não selecionada"

if selecao == "guerreiro":
    arma = "espada"
else:
    if selecao == "mago":
        arma = "magia"
    else:
        if selecao == "monge":
            arma = "artes marciais"
        else:
            arma = "shuriken"
           
heroi = Heroi(selecao, arma)

heroi.escrever()