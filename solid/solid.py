from abc import ABC, abstractmethod


class Towar:
    def __init__(self):
        self.price = price

    def group(self, price):
        self.price = price

    def accept_rabat(group.price, rabat):
        try:
            if group.price:
                group.price = group.price - (group.price * rabat)
                print("New price is {}".format(group.price) )
            else:
                self.price *= rabat
        except Error as e:
            print("Some problems here \n {}".format(e))


