money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
n=0

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while True:
    month = money_capital + salary
    if month < spend:
        break
    money_capital = month - spend
    n+=1
    spend = spend * (1 + increase)
print("Количество месяцев, которое можно протянуть без долгов:", n)
