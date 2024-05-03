# Дз про роботу з кількома класами

# Завдання 4

class Employee:
    def __init__(self, name=None, position=None, salary=None):
        self.name = name
        self.position = position
        self.salary = salary


class Department:
    def __init__(self):
        self.employee = []
        self.employee_positions = ""
        self.employee_names = ""


    def add_employee(self, *args):
        for employee in args:
            self.employee_positions += employee.position + ", "
            self.employee.append(employee)


    def subtract_employee(self, *args):
        for employee in args:
            self.employee.remove(employee)

    def print_employee_position(self):
        if self.employee:
            for employee in self.employee:
                print(employee.position, employee.name)
        else:
            print("Нікого нема!")

    def all_salary(self):
        return bohdan.salary + maksum.salary + igor.salary + artur.salary


bohdan = Employee("Bohdan", "director", 50000)
maksum = Employee("Maksum", "secretar", 40000)
igor = Employee("Igor", "programmer", 37000)
artur = Employee("Artur", "programmer", 37000)

department_1 = Department()

department_1.add_employee(bohdan)
department_1.add_employee(maksum)
department_1.add_employee(igor)
department_1.add_employee(artur)

department_1.print_employee_position()
print("Загальна зарплата:", department_1.all_salary())




