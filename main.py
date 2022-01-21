from itertools import combinations, groupby
import collections
import tkinter as tk
from operator import itemgetter

class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.c_nums = [c.n for c in cards]
        self.points = 0
        self.dupes = []
        self.o = [c.order for c in cards]

    def app_flipped(self, c):
        self.cards.append(c)
        self.c_nums.append(c.n)

    def solve(self):
        combos = [list(combinations(self.c_nums, i)) for i in range(2, 6)]
        order = [list(combinations(self.o, i)) for i in range(3, 6)]

        count = 0
        n = len(self.cards)
        for i in range(n):
            for j in range(i + 1, n):
                if self.cards[i].n == self.cards[j].n:
                    self.points += 2
                    print('Pair for 2')

        # a = [item for item, count in collections.Counter(order).items() if count > 2]
        runs = []
        for item in order:
            for thing in item:
                if len(thing) == (max(thing) - min(thing) + 1) and len(thing) == len(set(thing)):
                    # self.points += len(thing)
                    # print(f'run of {len(thing)}')
                    runs.append(thing)
        if runs:
            self.points += len(max(runs)) * runs.count(max(runs))
            print(f'{runs.count(max(runs))} run(s) of {len(max(runs))}')

        # for k in range(len(order)):
        #     for i in range(len(order)):
        #         for j in range(i + 1, len(order)):
        #             try:
        #                 if all(item in order[j] for item in order[i]):
        #                     order.remove(order[i])
        #                     print(order)
        #                 else:
        #                     break
        #             except IndexError:
        #                 pass
        # for item in order:
        #     self.points += len(item)
        #     print(f'Item: {item}')

        for item in combos:
            for thing in item:
                try:
                    if sum(thing) == 15:
                        self.points += 2
                        print('15 for 2 ', thing)
                except TypeError:
                    if ('K' in thing and 5 in thing) or ('Q' in thing and 5 in thing) or ('J' in thing and 5 in thing):
                        if len(thing) == 2:
                            self.points += 2
                            print('15 for 2 ', thing)



        cs = set()
        for c in self.cards:
            cs.add(c.suit)
        if len(cs) == 1:
            self.points += 5
            print('Same suit for 5')

        for c in self.cards[:4]:
            if c.n == 'J':
                try:
                    if c.suit == self.cards[4].suit:
                        self.points += 1
                        print('Right Jack for 1')
                except IndexError:
                    pass

        return self.points


class Card:
    def __init__(self, n, suit):
        self.n = n
        self.suit = suit
        self.order = 0

    def assign_order(self, o):
        self.order = o

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
                    if len(item.get()) > 2:
                        a = int(item.get()[:2])
                    else:
                        a = int(item.get()[0])
                    cur = Card(a, item.get()[1])
                    cur.assign_order(a)
                    cards.append(cur)
                except ValueError:
                    cur = Card(item.get()[0].upper(), item.get()[1])
                    print(cur)
                    match item.get()[0].upper():
                        case 'J':
                            cur.assign_order(11)
                        case 'Q':
                            cur.assign_order(12)
                        case 'K':
                            cur.assign_order(13)
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
