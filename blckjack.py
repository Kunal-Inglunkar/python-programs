import random
import tkinter


def load_img(card_image):
    suits = ["heart", "club", "diamond", "spade"]
    face_cards = ["jack", "queen", "king"]
    extension = "png"

    for suit in suits:
        for card in range(1, 11):
            name = 'cards\{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_image.append((card, image))
        for card in face_cards:
            name = 'cards\{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_image.append((10, image))


def deal_card(frame):
    next_card = deck.pop(0)
    deck.append(next_card)
    tkinter.Label(frame, image=next_card[1], relief="raised").pack(side="left")
    return next_card


def score_hand(hand):
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    # dealer_hand.append(deal_card(dealer_card))
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    # dealer_score_label.set(dealer_score)
    player_score = score_hand(palyer_hand)
    if player_score > 21:
        result_tet.set("DEALER WINS!!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_tet.set("Player WINS!!")
    elif dealer_score > player_score:
        result_tet.set("DEALER WINS!!")
    else:
        result_tet.set("DRAW")


def deal_player():
    # global player_score
    # global player_ace
    # card_value = deal_card(player_card_frame)[0]
    # if card_value == 1 and not player_ace:
    #     player_ace=True
    #     card_value = 11
    # player_score += card_value
    # if player_score > 21 and player_ace:
    #     player_score -= 10
    #     player_ace=False
    # player_score_label.set(player_score)
    # if player_score > 21:
    #     result_tet.set("dealer wins!!")
    # print(locals())
    palyer_hand.append((deal_card(player_card_frame)))
    player_score = score_hand(palyer_hand)
    player_score_label.set(player_score)
    if player_score > 21:
        result_tet.set("dealer Wins")


def new_game():
    # card_frame.destroy()
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global palyer_hand
    dealer_card_frame.destroy()
    player_card_frame.destroy()
    dealer_hand.clear()
    palyer_hand.clear()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)
    result_tet.set("")
    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()






mainwindow = tkinter.Tk()

mainwindow.title("Blackjack")
mainwindow.geometry("640x400")
mainwindow.configure(background="green")

result_tet = tkinter.StringVar()
result = tkinter.Label(mainwindow, textvariable=result_tet)
result.grid(row=0, column=0, columnspan=3)
card_frame = tkinter.Frame(mainwindow, relief='sunken', borderwidth=1, background='green')
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()
# player_score = 0
# player_ace = False
tkinter.Label(card_frame, text="player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=4, column=0)

player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

buttonframw = tkinter.Frame(mainwindow)
buttonframw.grid(row=3, column=0, sticky="w")
dealer_button = tkinter.Button(buttonframw, text="Dealer", width=5, command=deal_dealer)
dealer_button.grid(row=0, column=0, sticky="w")

player_button = tkinter.Button(buttonframw, text="Player", width=5, command=deal_player)
player_button.grid(row=0, column=1, sticky="w")

cards = []
load_img(cards)


deck = list(cards)
random.shuffle(deck)
dealer_hand = []
palyer_hand = []
deal_player()
dealer_hand.append(deal_card(dealer_card_frame))
dealer_score_label.set(score_hand(dealer_hand))
deal_player()
new_button = tkinter.Button(buttonframw, text="NEW GAME", width=10,command=new_game)
new_button.grid(row=0, column=3, sticky="w", columnspan=5)
mainwindow.mainloop()
