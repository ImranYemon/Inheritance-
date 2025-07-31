class Employee :
    salary = 20000
    incriment = 20
    @property
    def salaryafterincriment(self):
        return self.salary * self.salary *(self.incriment/100)


e = Employee()
print(e.salaryafterincriment)
