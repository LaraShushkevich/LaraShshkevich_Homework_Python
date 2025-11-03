def is_year_leap (year):
    if year % 4 == 0:
        return True
    else:
        return False

choosen_year = 1976
result = is_year_leap(choosen_year)
print(f"год {choosen_year}:{result}")


