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
temp = 0
count = 0
RICH = 5_000_000
WEALTH_TAX = 0.1
ADDITIONAL_RATE = 0.03
MIN_COMMISION = 30
MAX_COMMISION = 600
COMMISION = 0.015
AMOUNT_LIMIT = 50
START_MINIMUM_LIMIT = 50
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
            print("Вам дополнительный доход - ", sum * ADDITIONAL_RATE)     
            print("Ваш баланс - ", sum)
    if command == "-" and sum >= START_MINIMUM_LIMIT:                
        count += 1
        money = int(input("Введите сумму: "))
        if sum < RICH:
            if money % AMOUNT_LIMIT == 0 and sum >= money:
                if money * COMMISION < MIN_COMMISION:
                    temp = sum - (money + MIN_COMMISION)
                    if temp > 0:
                        sum -= (money + MIN_COMMISION)
                    else: print ("Операция не возможна")
                    temp = 0
                elif money * COMMISION > MAX_COMMISION:
                    temp = sum - (money + MAX_COMMISION)
                    if temp > 0:
                        sum -= (money + MAX_COMMISION)
                    else: print ("Операция не возможна")
                    temp = 0 
                else:
                    temp = sum - (money * COMMISION)
                    if temp > 0:
                        sum -= (money * COMMISION)
                    else: print ("Операция не возможна")
                    temp = 0 
                print("Ваш баланс - ", sum)
            elif money % AMOUNT_LIMIT == 0 and sum < money :
                print("Недостаточно средств")
            else:
                print("сумма введена некорретно")
                if count % ADDITIONAL_RATE_PERIOD == 0:
                    sum += sum * ADDITIONAL_RATE
                    print("Вам дополнительный доход - ", sum * ADDITIONAL_RATE) 
                    print("Ваш баланс - ", sum)
        else:
            if money % AMOUNT_LIMIT == 0 and sum >= money:
                if money * COMMISION < MIN_COMMISION:             
                    sum -= (money + MIN_COMMISION) 
                    sum -= sum * WEALTH_TAX
                elif money * COMMISION > MAX_COMMISION:
                    temp = sum - ((money + MAX_COMMISION) + sum * WEALTH_TAX)
                    if temp > 0:
                        sum -= ((money + MAX_COMMISION) + sum * WEALTH_TAX)
                    else: print ("Операция не возможна")
                    temp = 0       
                else:
                    sum -= (money + (money * COMMISION))
                    sum -= sum * WEALTH_TAX
                print("Ваш баланс - ", sum)
            elif money % AMOUNT_LIMIT == 0 and sum < money :
                print("Недостаточно средств")
            else:
                print("сумма введена некорретно")
                if count % ADDITIONAL_RATE_PERIOD == 0:
                    sum += sum * ADDITIONAL_RATE
                    print("Вам дополнительный доход - ", sum * ADDITIONAL_RATE) 
                    print("Ваш баланс - ", sum)

    if command == "-" and sum < START_MINIMUM_LIMIT: 
        print ("На счету не достаточно средств для снятия")
    if command == "e":
        print("Ваш баланс - ", sum)
        break
    

    