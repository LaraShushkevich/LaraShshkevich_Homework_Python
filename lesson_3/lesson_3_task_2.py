from smartphone import  Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy A07", "+79112223344"),
    Smartphone("Apple", "iPhone 17Pro", "+79217776655"),
    Smartphone("HONOR", "X9d", "+79018901234"),
    Smartphone("Xiaomi", "Poco F17", "+79051234567"),
    Smartphone("OPPO", "A5x", "+79996662255")
]

for smartphone in catalog:
    print(f"{smartphone.mark} - {smartphone.model} . {smartphone.phone_num}")