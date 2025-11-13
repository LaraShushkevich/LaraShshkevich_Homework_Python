from address import  Address

class Mailing:
    cost = 0
    track = ''

    def __init__(self, track, from_address, to_address, cost):
        self.track = track
        self.from_address = from_address
        self.to_address = to_address
        self.cost = cost

    def __str__(self):
        return f"Отправление {self.track} из {self.from_address.index}, {self.from_address.city}, {self.from_address.street}, {self.from_address.house} - {self.from_address.apartment} в {self.to_address.index}, {self.to_address.city}, {self.to_address.street}, {self.to_address.house} - {self.to_address.apartment}. Стоимость {self.cost} рублей."



