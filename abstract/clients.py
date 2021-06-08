class klient_firmowy:
    def __init__(self, firm_name, nip, miasto):
        self.firm_name = firm_name
        self.nip = nip
        self.miasto = miasto

    def show_info(self):
        print('{}'.format(self.firm_name).upper())
        print('Companies NIP: {}'.format(self.nip))
        print('From: {}'.format(self.miasto))

class klient_indywidualny:
    def __init__(self, name, surname, nip, ):
        self.name = name
        self.surname = surname
        self.nip = nip