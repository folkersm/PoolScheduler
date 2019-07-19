class Employee:

    raise_amount = 1.04
    employee_Amount = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@companyemail'

        Employee.employee_Amount += 1

    def fullname(self):
        return '{} {}{}{}'.format(self.first, self.last, self.first)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount




emp1 = Employee('herold', 'bob', 500)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
print(Employee.employee_Amount)
print(emp1.fullname())