from random import random
import webbrowser
import random
import time
webbrowser.Mozilla()

class Cards:
    '''Class for card functionality'''
    global cardList,cardListCopy,cardValues
    cardList = []
    cardListCopy = []
    cardValues = {}

    def __init__(self, card, suit, value):
        self.card = card
        self.suit = suit
        self.value = value
        #if self.card == "A":
        #    self.value = (1,11)
        cardList.append(suit+card)
        cardListCopy.append(suit+card)
        cardValues[suit+card] = self.value

    def checkBlackJack(card1,card2):
        if card1[-1] == "A":
            score = 11 + cardValues[card2]
        elif card2[-1] == "A":
            score = cardValues[card1] + 11
        else:
            score = cardValues[card1] + cardValues[card2]
        if score == 21:
            print("Blackjack!")
            return True
        else:
            return score

    
    def declare_cards():
        Spade2 = Cards("2","Spade",2)
        Spade3 = Cards("3","Spade",3)
        Spade4 = Cards("4","Spade",4)
        Spade5 = Cards("5","Spade",5)
        Spade6 = Cards("6","Spade",6)
        Spade7 = Cards("7","Spade",7)
        Spade8 = Cards("8","Spade",8)
        Spade9 = Cards("9","Spade",9)
        Spade10 = Cards("10","Spade",10)
        SpadeJack = Cards("J","Spade",10)
        SpadeQueen = Cards("Q","Spade",10)
        SpadeKing = Cards("K","Spade",10)
        SpadeAce = Cards("A","Spade",11)

        Clubs2 = Cards("2","Clubs",2)
        Clubs3 = Cards("3","Clubs",3)
        Clubs4 = Cards("4","Clubs",4)
        Clubs5 = Cards("5","Clubs",5)
        Clubs6 = Cards("6","Clubs",6)
        Clubs7 = Cards("7","Clubs",7)
        Clubs8 = Cards("8","Clubs",8)
        Clubs9 = Cards("9","Clubs",9)
        Clubs10 = Cards("10","Clubs",10)
        ClubsJack = Cards("J","Clubs",10)
        ClubsQueen = Cards("Q","Clubs",10)
        ClubsKing = Cards("K","Clubs",10)
        ClubsAce = Cards("A","Clubs",11)

        Hearts2 = Cards("2","Hearts",2)
        Hearts3 = Cards("3","Hearts",3)
        Hearts4 = Cards("4","Hearts",4)
        Hearts5 = Cards("5","Hearts",5)
        Hearts6 = Cards("6","Hearts",6)
        Hearts7 = Cards("7","Hearts",7)
        Hearts8 = Cards("8","Hearts",8)
        Hearts9 = Cards("9","Hearts",9)
        Hearts10 = Cards("10","Hearts",10)
        HeartsJack = Cards("J","Hearts",10)
        HeartsQueen = Cards("Q","Hearts",10)
        HeartsKing = Cards("K","Hearts",10)
        HeartsAce = Cards("A","Hearts",11)

        Diamonds2 = Cards("2","Diamonds",2)
        Diamonds3 = Cards("3","Diamonds",3)
        Diamonds4 = Cards("4","Diamonds",4)
        Diamonds5 = Cards("5","Diamonds",5)
        Diamonds6 = Cards("6","Diamonds",6)
        Diamonds7 = Cards("7","Diamonds",7)
        Diamonds8 = Cards("8","Diamonds",8)
        Diamonds9 = Cards("9","Diamonds",9)
        Diamonds10 = Cards("10","Diamonds",10)
        DiamondsJack = Cards("J","Diamonds",10)
        DiamondsQueen = Cards("Q","Diamonds",10)
        DiamondsKing = Cards("K","Diamonds",10)
        DiamondsAce = Cards("A","Diamonds",11)


class Blackjack:
    '''Class for blackjack game functionality'''

    def __init__(self,card1,card2):
        self.card1 = card1
        self.card2 = card2

    def getCards(self):
        return self.card1, self.card2

    def startGame():
        print("Welcome to Blackjack.")
        while True:
            userInput = input("Enter '1' to begin, '2' to exit, or 'Help' to get the rules of blackjack.\n")
            if userInput == "1":
                Blackjack.dealCards()
                break
            elif userInput == "2":
                quit()
            elif userInput.lower() == "help":
                webbrowser.open("https://bicyclecards.com/how-to-play/blackjack/",new=2)
                time.sleep(1)
                continue
            else:
                print("Invalid response, please try again.")
                userInput = input("Enter '1' to begin, '2' to exit, or 'Help' to get the rules of blackjack.\n")                
        
    def dealCards():
        n = 0
        dealtCards = []
        while n < 4:
            lstLength = len(cardListCopy)
            randIndex = random.randint(0,lstLength)
            random.shuffle(cardListCopy)
            #random.shuffle(cardListCopy)
            dealtCard = cardListCopy.pop(randIndex)
            dealtCards.append(dealtCard)
            n += 1
        random.shuffle(dealtCards)
        player = Blackjack(dealtCards[0],dealtCards[2])
        dealer = Blackjack(dealtCards[1],dealtCards[3])
        pcard1, pcard2 = player.getCards()
        playerScore = Cards.checkBlackJack(pcard1,pcard2)
        dcard1, dcard2 = dealer.getCards()
        dealerScore = Cards.checkBlackJack(dcard1,dcard2)
        if playerScore == True:
            print("Your cards: " + "(Score: 21)")
            print(pcard1,pcard2)
            print("You got blackjack, you win!")
        elif dealerScore == True:
            print("Your cards: " + "(Score: "+ str(playerScore) +")")
            print(pcard1,pcard2)
            print("Dealer's cards: " + "(Score: 21)")
            print(dcard1,dcard2)
            print("The dealer got blackjack, you lose!")
        else:
            Blackjack.game(player,dealer,playerScore,dealerScore)

    def hit():
        lstLength = len(cardListCopy)
        randIndex = random.randint(0,lstLength)
        random.shuffle(cardListCopy)
        dealtCard = cardListCopy.pop(randIndex)
        return dealtCard

    def game(player, dealer, pscore, dscore):
        pcard1,pcard2 = player.getCards()
        dcard1,dcard2 = dealer.getCards()
        playerCards = [pcard1,pcard2]
        dealerCards = [dcard1,dcard2]
        dchecked = False
        pchecked = False
        counter = 0
        print("Your cards: (Score:" , str(pscore) +")")
        for i in range(len(playerCards)):
            print(playerCards[i], end=', ')
        print("\nDealers Cards:" + "\n" + dcard1 , "?")
        playerChoice = input("Would you like to hit or stay?\n")
        while playerChoice.lower() != "stay":
            if playerChoice.lower() == "hit":
                newCard = Blackjack.hit()
                playerCards.append(newCard)
                pscore += cardValues[newCard]
                #if pscore < 21:
                print("Your cards: (Score:" , str(pscore) +")")
                for i in range(len(playerCards)):
                    print(playerCards[i], end=', ')
                if pscore > 21:
                    for cards in playerCards:
                        if cards[-1] == "A" and pchecked == False:
                            pscore -= 10
                            pchecked = True
                            counter = 0
                            break
                        else:
                            counter += 1
                            if counter == len(playerCards):
                                print("\nBust! You lose.")
                                quit()
                playerChoice = input("\nWould you like to hit or stay?\n")
        while dscore < 17:
            newCard = Blackjack.hit()
            dealerCards.append(newCard)
            dscore += cardValues[newCard]
            #print("Dealer cards: (Score:" , str(dscore) +")")
            #for i in range(len(dealerCards)):
            #    print(dealerCards[i], end=', ')
            if dscore > 21:
                for cards in dealerCards:
                    if cards[-1] == "A" and dchecked == False:
                        dscore -= 10
                        dchecked = True
                        counter = 0
                        break
                    else:
                        counter += 1
                        if counter == len(dealerCards):
                            print("\nDealer busts! You win!")
                            quit()
        
        for i in range(len(dealerCards)):
            print(dealerCards[i], end=', ')
        print("Dealer Score:", dscore)
        if dscore > pscore:
            print("Dealer wins!")
        elif pscore > dscore:
            print("You win!")
        elif pscore == dscore:
            print("Tie, it's a push.")

Cards.declare_cards()
Blackjack.startGame()