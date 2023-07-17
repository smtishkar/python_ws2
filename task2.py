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
RICH = 5_000_000
WEALTH_TAX = 0.1
ADDITIONAL_RATE = 0.03
MIN_COMMISION = 30
MAX_COMMISION = 600
COMMISION = 0.015
AMOUNT_LIMIT = 50
ADDITIONAL_RATE_PERIOD = 3

while True:
    command = input("введите действие: ")
    if command == "+":
        count += 1
        money = int(input("Введите сумму: "))
        if money % AMOUNT_LIMIT == 0 and sum < RICH:
            sum += money
            print("Ваш баланс - ", sum)
        elif money % AMOUNT_LIMIT == 0 and sum > RICH:
            sum =  (sum + money) - ((sum + money) * WEALTH_TAX)          
            print("Ваш баланс - ", sum)
        else:
            print("сумма введена некорретно")
        if count % ADDITIONAL_RATE_PERIOD == 0:
            sum += sum * ADDITIONAL_RATE
            print("Вам дополнительный доход - ", sum * ADDITIONAL_RATE)     #подумать нужно ли тут округление?
            print("Ваш баланс - ", sum)
    if command == "-" and sum > 50:                 # Уходим в минус и снимается еще деньги за операцию
        count += 1
        money = int(input("Введите сумму: "))
        if money % AMOUNT_LIMIT == 0 and sum >= money :
            if money * COMMISION < MIN_COMMISION:
                sum -= (money + MIN_COMMISION)

            elif money * COMMISION > MAX_COMMISION:
                sum -= (money + MAX_COMMISION)

            else:
                sum -= (money + (money * COMMISION))
            print("Ваш баланс - ", sum)
        elif money % AMOUNT_LIMIT == 0 and sum < money :
            print("Недостаточно средств")
        else:
            print("сумма введена некорретно")
            if count % ADDITIONAL_RATE_PERIOD == 0:
                sum += sum * ADDITIONAL_RATE
                print("Вам дополнительный доход - ", sum * ADDITIONAL_RATE)          #Сделать чтобы начилсяслись проценты, а не снимались
                print("Ваш баланс - ", sum)
    if command == "e":
        print("Ваш баланс - ", sum)
        break
    

    