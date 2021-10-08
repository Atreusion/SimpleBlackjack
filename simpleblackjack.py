import random
import os
import sys

#pop(0) and append, top...bottom (draw from top, add to bottom)

class blackjack:
    def __init__(self):
        self.cardtuple = ("2c", "2d", "2h", "2s", "3c", "3d", "3h", "3s", "4c", "4d", "4h", "4s", "5c", "5d", "5h", "5s", "6c", "6d", "6h", "6s", "7c", "7d", "7h", "7s", "8c", "8d", "8h", "8s", "9c", "9d", "9h", "9s", "0c", "0d", "0h", "0s", "jc", "jd", "jh", "js", "qc", "qd", "qh", "qs", "kc", "kd", "kh", "ks", "ac", "ad", "ah", "as")
        self.numbernames = {"2" : "Two", "3" : "Three", "4" : "Four", "5" : "Five", "6" : "Six", "7" : "Seven", "8" : "Eight", "9" : "Nine", "0" : "Ten", "j" : "Jack", "q" : "Queen", "k" : "King", "a" : "Ace"}
        self.suitnames = {"c" : "Clubs", "d" : "Diamonds", "h" : "Hearts", "s" : "Spades"}
        self.roundactive = False
        self.humanhand = []
        self.dealerhand = []
    def prettify(self, card):
        prettyname = "%s of %s" % (self.numbernames[card[0]], self.suitnames[card[1]])
        return prettyname
    def gethandvalue(self, hand):
        value = 0
        aces = 0
        for card in hand:
            if card[0] in "0jqk": value += 10
            elif card[0] == "a":
                value += 11
                aces += 1
            else: value += int(card[0])
        if aces and value > 21:
            for i in range(aces):
                value -= 10
                if value <= 21: break
        return value
    def gethandstring(self, hand):
        handstring = ""
        for card in hand: handstring = handstring + self.prettify(card) + "\n"
        return handstring
    def action(self, startinput):
        if startinput == "d" and not self.roundactive:
            os.system('cls')
            self.deck = list(self.cardtuple)
            random.shuffle(self.deck)
            self.humanhand.append(self.deck.pop(0))
            self.humanhand.append(self.deck.pop(0))
            self.dealerhand.append(self.deck.pop(0))
            self.dealerhand.append(self.deck.pop(0))
            self.roundactive = True
            print("Dealer shows:\n[Card face down]\n%s\n\nYour cards:\n%s\nYour hand's total: %i\n" % (self.prettify(self.dealerhand[1]), self.gethandstring(self.humanhand), self.gethandvalue(self.humanhand)))
            if self.gethandvalue(self.humanhand) == 21:
                if self.gethandvalue(self.dealerhand) == 21:
                    print("Both player and dealer have blackjack! Push.")
                    self.__init__()
                else:
                    print("Player has blackjack! You win!")
                    self.__init__()
            elif self.gethandvalue(self.dealerhand) == 21:
                print("Dealer has blackjack! You lose!")
                self.__init__()
        elif startinput == "s" and self.roundactive:
            os.system('cls')
            print("Dealer reveals his hand.\n%s" % (self.gethandstring(self.dealerhand)))
            while self.gethandvalue(self.dealerhand) < 17: # dealer stand on 17
                newcard = self.deck.pop(0)
                self.dealerhand.append(newcard)
                print("Dealer draws %s." % (self.prettify(newcard)))
            if self.gethandvalue(self.dealerhand) > 21:
                print("Dealer hits %i and busts! You win!\n" % (self.gethandvalue(self.dealerhand)))
                self.__init__()
            elif self.gethandvalue(self.dealerhand) > self.gethandvalue(self.humanhand):
                print("Dealer hits %i! You had %i. You lose!\n" % (self.gethandvalue(self.dealerhand), self.gethandvalue(self.humanhand)))
                self.__init__()
            elif self.gethandvalue(self.dealerhand) < self.gethandvalue(self.humanhand):
                print("Dealer hits %i. You had %i! You win!\n" % (self.gethandvalue(self.dealerhand), self.gethandvalue(self.humanhand)))
                self.__init__()
            else:
                print("Dealer hits %i. You had %i. Push.\n" % (self.gethandvalue(self.dealerhand), self.gethandvalue(self.humanhand)))
                self.__init__()
        elif startinput == "h" and self.roundactive:
            os.system('cls')
            newcard = self.deck.pop(0)
            self.humanhand.append(newcard)
            print("Dealer shows:\n[Card face down]\n%s\n\nYou draw %s.\n\nYour new hand is:\n%s\nYour hand's total: %i\n" % (self.prettify(self.dealerhand[1]), self.prettify(newcard), self.gethandstring(self.humanhand), self.gethandvalue(self.humanhand)))
            if self.gethandvalue(self.humanhand) > 21:
                print("You hit %i and bust. You lose!\n" % (self.gethandvalue(self.humanhand)))
                self.__init__()
                
def main():
    bj = blackjack()
    os.system('cls')
    while True:
        startinput = input("Press d to deal, h to hit, s to stay.\n")
        bj.action(startinput)

if __name__ == "__main__":
    main()