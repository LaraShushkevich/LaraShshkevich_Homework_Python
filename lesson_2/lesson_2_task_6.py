lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

# числа выводятся в столбик
for n in lst:
    if (n <30) and (n % 3 == 0):
        print(n)

# числа выводятся списком

result = [n for n in lst if n < 30 and n % 3 == 0]
print(result)