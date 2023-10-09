"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, salary, hours = 0, commissionType = "", commission = 0, n_contracts = 0):
        self.name = name
        self.contract = contract
        self.salary = salary
        self.hours = hours
        self.commissionType = commissionType
        self.commission = commission
        self.n_contracts = n_contracts

    def get_pay(self):
        pay = 0
        if self.contract == "monthly":
            pay = self.salary
        else:
            pay = self.salary * self.hours

        if self.commissionType == "bonus":
            pay += self.commission
        elif self.commissionType == "contract":
            pay += self.commission * self.n_contracts
        else:
            pass
            
        return pay

    def __str__(self):
        answer = f"{self.name} works on a"
        if (self.contract == "monthly"):
            answer += f" monthly salary of {self.salary}"
        else:
            answer += f" contract of {self.hours} hours at {self.salary}/hour"
        if (self.commissionType == "bonus"):
            answer += f" and receives a bonus commission of {self.commission}"
        elif (self.commissionType == "contract"):
            answer += f" and receives a commission for {self.n_contracts} contract(s) at {self.commission}/contract"
        answer += "."
        answer += f" Their total pay is {self.get_pay()}."
        return answer


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "monthly", 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "hourly", 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "monthly", 3000, commissionType="contract", commission=200, n_contracts=4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', "hourly", 25, 150, "contract", 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "monthly", 2000, commissionType="bonus", commission=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "hourly", 30, 120, "bonus", 600)



