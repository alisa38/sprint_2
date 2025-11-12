class EmployeeSalary:
    # Почасовая ставка — общая для всех сотрудников (атрибут класса)
    hourly_payment = 400

    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    # Метод класса: рассчитывает часы, если они неизвестны
    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours is None and rest_days is not None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    # Метод класса: создаёт email, если он не указан
    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email is None:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    # Метод класса: изменяет почасовую оплату
    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    # Метод экземпляра: рассчитывает зарплату
    def salary(self):
        return self.hours * self.hourly_payment


# 🔹 Пример работы
# 1. Создаём сотрудника, у которого не указаны часы — считаем их по выходным
employee_1 = EmployeeSalary.get_hours('Иван', None, 2, 'ivan@email.com')
print(employee_1.hours)  # (7 - 2) * 8 = 40

# 2. Создаём сотрудника, у которого нет email
employee_2 = EmployeeSalary.get_email('Мария', 35, 1, None)
print(employee_2.email)  # "Мария@email.com"

# 3. Проверим расчёт зарплаты
print(employee_1.salary())  # 40 * 400 = 16000

# 4. Изменим ставку для всех
EmployeeSalary.set_hourly_payment(500)
print(employee_1.salary())  # 40 * 500 = 20000