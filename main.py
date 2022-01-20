from itertools import combinations
import collections
import tkinter as tk

class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.c_nums = [c.n for c in cards]
        self.points = 0
        self.dupes = []

    def app_flipped(self, c):
        self.cards.append(c)
        self.c_nums.append(c.n)

    def solve(self):
        combos = [list(combinations(self.c_nums, i)) for i in range(2, 6)]

        for i in range(2, 5):
            t = [item for item, count in collections.Counter(self.c_nums).items() if count == i]
            if t:
                for item in t:
                    self.points += i * (i - 1)

        for item in combos:
            for thing in item:
                if sorted(thing) == list(range(min(thing), max(thing) + 1)):
                    if len(thing) > 2:
                        self.points += len(thing)
                if sum(thing) == 15:
                    self.points += 2

        for c in self.cards:
            cs = set()
            cs.add(c.suit)
            if len(cs) == 5:
                self.points += 5

        for c in self.cards[:4]:
            if c.sub_card == 'J':
                if c.suit == self.cards[4].suit:
                    self.points += 1

        return self.points


class Card:
    def __init__(self, n, suit):
        self.n = n
        self.suit = suit
        self.sub_card = ''

    def assign_sc(self, sc):
        self.n = 10
        self.sub_card = sc

    def __repr__(self):
        return f'{self.n}{self.suit}'

win = tk.Tk()
win.geometry('400x260+5+5')
win.resizable(False, False)
main = tk.Label(win,text='Use \'d\',\'h\',\'s\',\'c\' to denote the suit of the card (i.e. 5d)')
c1, c2, c3, c4, c5 = tk.Entry(win, width=3), tk.Entry(win, width=3), tk.Entry(win, width=3), tk.Entry(win, width=3), tk.Entry(win, width=3)
c1.place(x=0, y=40)
c2.place(x=40, y=40)
c3.place(x=80, y=40)
c4.place(x=120, y=40)
c5.place(x=0, y=80)
main.place(x=0, y=0)

def submit():
    c_inputs = [c1, c2, c3, c4, c5]
    cns = []
    css = []
    cards = []
    run = True

    while run:
        for item in c_inputs:

            try:
                try:
                    a = int(item.get()[0])
                    cards.append(Card(int(item.get()[0]), item.get()[1]))
                except ValueError:
                    match item.get()[0].upper():
                        case 'J':
                            cns.append(item.get()[0])
                            css.append(item.get()[1])
                            cur = Card(item.get()[0], item.get()[1])
                            cur.assign_sc('J')
                            cards.append(cur)
                        case 'Q':
                            cns.append(item.get()[0])
                            css.append(item.get()[1])
                            cur = Card(item.get()[0], item.get()[1])
                            cur.assign_sc('Q')
                            cards.append(cur)
                        case 'K':
                            cns.append(item.get()[0])
                            css.append(item.get()[1])
                            cur = Card(item.get()[0], item.get()[1])
                            cur.assign_sc('J')
                            cards.append(cur)
                h = Hand(cards)
                run = False

            except IndexError:
                print(f'No input on {item}')

    print(h.solve())

sbmt = tk.Button(win, text='Submit', command=submit)
sbmt.place(x=0, y=120)

def main():
    win.mainloop()

if __name__ == '__main__':
    main()
