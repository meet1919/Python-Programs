class Employee:

    no_employee = 0
    raise_pay = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = '%s.%s@Blogpost.com' % (self.first, self.last)

        Employee.no_employee += 1

    def full_name(self):
        return '%s %s' % (self.first, self.last)

    def employee_details(self):
        return 'Name: %s %s\nEmail: %s\nSalary: %s' % (
            self.first, self.last, self.email, self.pay)

    def salary_raise(self):
        self.pay = int(self.pay * self.raise_pay)

    @classmethod
    def from_string(cls, string):
        first, last, pay = string.split('-')
        return cls(first, last, pay)



class Manager(Employee):

    def __init__(self, first, last, pay, employees):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emoployees(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        else:
            return ('Employee is already managed by %s' % (Manager.full_name(self)))

    def remove_employees(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        else:
            print(emp, 'not under %s management' % (Manager.full_name(self)))

    def display_employees(self):
        for emp in self.employees:
            print('--> %s' % (emp.full_name()))


emp1_string = 'Rahul-Rohida-10000'
emp1 = Employee('Rahul', 'Rohida', 10000)
#print(emp1.employee_details())

#new_emp1 = Employee.from_string(emp1_string)
#print(new_emp1.employee_details())

mgr1 = Manager('Jay', 'Tanna', '20000', [emp1])
print(mgr1.display_employees())
print(mgr1.employees)
