class User:
    company = "Django"
    __secretSalary = 10000

    def __init__(self, name):
        self.name = name

    def display_info(self):
        print("{} works for {}".format(self.name, self.company))

    def set_email(self, email):
        self.email = email


print(User.company)

user = User("Bob")
user.display_info()
user.set_email('bob@django.org')
print(user.email)

alice = User("Alice")
print(alice._User__secretSalary)
