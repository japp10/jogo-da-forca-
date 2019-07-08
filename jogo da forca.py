from random import randint
class JF:
    def switch(self):
        #escolhe aleatoriamente uma das palavras
        self.rand = randint(0,9)
        self.palavra = ""
        if self.rand == 0:
            self.palavra ="palmeiras"
        elif self.rand == 1 :
            self.palavra ="santos"
        elif self.rand == 2:
            self.palavra ="corinthians"
        elif self.rand == 3:
            self.palavra ="cruzeiro"
        elif self.rand == 4:
            self.palavra ="internacional"
        elif self.rand == 5:
            self.palavra ="barcelona"
        elif self.rand == 6:
            self.palavra ="liverpool"
        elif self.rand == 7:
            self.palavra ="chelsea"
        elif self.rand == 8:
            self.palavra ="juventus"
        elif self.rand == 9:
            self.palavra ="paysandu"
    def play(self):
        self.switch()
        digitadas = []
        acertos = []
        erros = 0
        while True:
            #condição de vitória
             senha = ""
             for chute in self.palavra:
                 if chute in acertos:
                     senha += chute
                 else :
                     senha += "[ ]"
             print(senha)
             if senha == self.palavra:
                 print("Você acertou!")
                 break
             chute = input("\nDigite uma letra:").lower()
             if chute.isdigit() == True:
                 print("Esse chute foi invalido,por favor digite novamente")
                 chute = input("\nDigite uma letra:").lower()
             #checa se essa letra foi digitada
             if chute in digitadas:
                 print("Você já tentou esta letra!")
             else:
                 digitadas += chute
                 #checa se a letra está na palavra ou não
                 if chute in self.palavra:
                       acertos += chute
                 else:
                       erros += 1
                       print("Você errou!")
             print("")
             #desenha o boneco da forca
             if erros == 1:
                  print(" 0   ")
                  print(" |   ")
             elif erros == 2:
                  print(" 0   ")
                  print(" |   ")
                  print(" |   ")
             elif erros == 3:
                 print("  0   ")
                 print(" \|   ")
                 print("  |   ")
             elif erros == 4:
                 print("  0   ")
                 print(" \|/ ")
                 print("  |   ")
             elif erros == 5:
                 print("  0   ")
                 print(" \|/ ")
                 print("  |   ")
                 print(" /     ")
             elif erros == 6:
                 print("  0   ")
                 print(" \|/ ")
                 print("  |   ")
                 print(" / \ ")
            #checa se o jogador perdeu o jogo
             if erros == 6:
                 print("Enforcado!\n")
                 print(self.palavra)
                 break
#inicia o jogo
if __name__ == '__main__':
    jogo = JF()
    jogo.play()
