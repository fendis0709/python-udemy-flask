class School:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.isOpen = True

    def __str__(self):
        return f'{self.name} located in {self.city}'

    def closed(self):
        self.isOpen = False


class Library(School):
    def __init__(self, name, city, capacity):
        super().__init__(name, city)
        self.capacity = capacity

    def visit(self, students=1):
        if(self.isOpen):
            self.capacity -= students
            print('Welcome. Have a nice reading.')
        else:
            print('Sorry, we are closed now.')


library = Library('SMA 1 Gondang', 'Nganjuk', 100)
library.visit(3)
print(f'Remaining seat: {library.capacity}')
library.closed()
library.visit()
