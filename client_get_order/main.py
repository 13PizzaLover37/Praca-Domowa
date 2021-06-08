
class Order:
    global deliver_status
    def __init__(self):
        pass
    def delivering(self):
        if Order.deliver_status == '0':
            print('Unready')
        else:
            print('Your item sended \nWait please')
    def information(self):
        make_order.get_info(self)


class make_order:
    global deliver_status

    def __init__(self, name):
        self.name = name

    def get_info(self):
        global info
        info = []
        id = 0

        mark = input('Which mark do u want? \n')
        info.append(mark)
        model = input('Which model? \n')
        info.append(model)
        color = input('Which color? \n')
        info.append(color)
        money = input("Next step?(Y/N): ")
        if money =='Y':
            make_order.get_money(self)
        else:
            print('Sad :(')
        id += 1
    def get_money(self):
        global status
        ask = input("Are u ready for paying now?(Y/N): ")
        if ask == 'Y':
            status = True
            Order.deliver_status = 1
        elif ask == 'N':
            status = False
            Order.deliver_status = 0
        info.append(status)
        Order.delivering(self)

sams = Order()
sams.information()

