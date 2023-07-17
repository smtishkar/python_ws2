# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

sum = 0
count = 0

while True:
    command = input("введите действие: ")
    if command == "+":
        count += 1
        money = int(input("Введите сумму: "))
        if money % 50 == 0 and sum < 5_000_000:
            sum += money
            print(sum)
        elif money % 50 == 0 and sum > 5_000_000:
            sum =  (sum + money) - ((sum + money) * 0.1)          
            print(sum)
        else:
            print("сумма введена некорретно")
        if count % 3 == 0:
            sum -= sum * 0.03
            print("комиссия - ", sum * 0.03)
    if command == "-" and sum > 50:
        count += 1
        money = int(input("Введите сумму: "))
        if money % 50 == 0:
            if money * 0.015 < 30:
                sum -= (money + 30)

            elif money * 0.015 > 600:
                sum -= (money + 600)

            else:
                sum -= (money + (money * 0.015))
            print(sum)
        else:
            print("сумма введена некорретно")
            if count % 3 == 0:
                sum -= sum * 0.03
                print("комиссия - ", sum * 0.03)
    if command == "e":
        print(sum)
        break
    

    