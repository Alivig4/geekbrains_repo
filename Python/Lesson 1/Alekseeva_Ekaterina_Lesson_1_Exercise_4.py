n = int(input("Введите целое положительное число:"))
max = 0
while n > 10:
    last_digit = n % 10
    if last_digit > max:
        max = last_digit
    n = int(n / 10)

if n > max:
    max = n

print("Максимальная цифра = ", max)