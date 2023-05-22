import datetime
import unittest

class ModernBank:
    def __init__(self, goal, deadline):
        # Целевая сумма накопления
        self.goal = goal
        # Дата, когда нужно достичь цели
        self.deadline = deadline
        # Текущий остаток на счете
        self.balance = 0
        # Процентная ставка в год
        self.interest_rate = 0.05

    def deposit(self, amount):
        # Пополнение счета на указанную сумму
        self.balance += amount

    def calculate_days_to_goal(self):
        # Определение количества дней до достижения цели
        days_to_goal = (self.deadline - datetime.date.today()).days
        return days_to_goal

    def calculate_months_to_goal(self):
        # Определение количества месяцев до достижения цели
        months_to_goal = round(self.calculate_days_to_goal() / 30)
        return months_to_goal

    def calculate_years_to_goal(self):
        # Определение количества лет до достижения цели
        years_to_goal = round(self.calculate_days_to_goal() / 365)
        return years_to_goal

    def calculate_interest(self):
        # Расчет процентной ставки на остаток
        interest = self.balance * self.interest_rate
        return interest

    def show_goal_deadline(self):
        # Вывод информации о цели и сроке достижения
        print("Целевая сумма: {} рублей".format(self.goal))
        print("Желаемая дата достижения цели: {}".format(self.deadline))

    def show_balance(self):
        # Вывод текущего остатка на счете
        print("Текущий остаток на счете: {} рублей".format(self.balance))

    def show_days_to_goal(self):
        # Вывод количества дней до достижения цели
        days_to_goal = self.calculate_days_to_goal()
        if days_to_goal > 0:
            print("Дней до достижения цели: {}".format(days_to_goal))
        else:
            print("Цель достигнута!")

    def show_months_to_goal(self):
        # Вывод количества месяцев до достижения цели
        months_to_goal = self.calculate_months_to_goal()
        if months_to_goal > 0:
            print("Месяцев до достижения цели: {}".format(months_to_goal))
        else:
            print("Цель достигнута!")

    def show_years_to_goal(self):
        # Вывод количества лет до достижения цели
        years_to_goal = self.calculate_years_to_goal()
        if years_to_goal > 0:
            print("Лет до достижения цели: {}".format(years_to_goal))
        else:
            print("Цель достигнута!")

    def show_interest(self):
        # Вывод процентной ставки на остаток
        interest = self.calculate_interest()
        print("Процентная ставка на остаток: {} рублей".format(interest))