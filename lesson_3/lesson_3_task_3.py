from address import  Address
from mailing import  Mailing

to_address = Address("197000", "Санкт-Петербург", "Бутлерова", 20, 28)
from_address = Address("187553", "Тихвин", "Советская", 48, 25)
my_mailing = Mailing("17955511101020578", from_address, to_address, 50)

print(my_mailing)