# Завдання: Створіть додаток для кав'ярні з кастомізацією напоїв.
# Використовуючи абстрактні базові класи, створіть наступні види напоїв:
#
# Лате
# Капучино
# Американо
# Мокка
#
# Кожен напій можна кастомізувати, додаючи різні добавки, такі як сиропи, молоко або вершки.
#
# Основна структура:
#
# Клас Drink: Базовий абстрактний клас, що містить основні методи для підготовки напою
# та абстрактний метод для його приготування.
#
# Класи Latte, Cappuccino, Americano, Mocha: Підкласи, що успадковують від Drink і реалізують
# специфіку кожного напою.
#
# Методи для додавання добавок:
# Методи, які дозволяють кастомізувати напій відповідно до вибору
# користувача.

from abc import ABC, abstractmethod


class Drink(ABC):

    def __init__(self, name):
        self.name = name
        self.add_ingr = []

    @abstractmethod
    def add_coffee(self):
        pass

    @abstractmethod
    def add_sugar(self):
        pass


class Latte(Drink):
    def __init__(self):
        super().__init__('Latte')

    def add_coffee(self):
        print('To add coffee to coffee machine')
        self.add_ingr.append('coffee')

    def add_sugar(self):
        print('Put sugar in cup')
        self.add_ingr.append('sugar')

    def add_milk(self):
        print('Add milk in cup')
        self.add_ingr.append('milk')

    def add_cream(self):
        print('Add cream in cup')
        self.add_ingr.append('cream')

    def add_syrup(self):
        print('Add syrup in cup')
        self.add_ingr.append('syrup')

    def prepare(self):
        print('Prepare Latte:')
        self.add_coffee()
        self.add_sugar()
        self.add_milk()
        self.add_cream()
        choice = input('Do you want to add syrup Y/N: ').lower()
        if choice == 'y':
            self.add_syrup()
        print(f'Ingredients: {self.add_ingr}')


class Cappuccino(Drink):
    def __init__(self):
        super().__init__('Cappuccino')

    def add_coffee(self):
        print('To add coffee to coffee machine')
        self.add_ingr.append('coffee')

    def add_sugar(self):
        print('Put sugar in cup')
        self.add_ingr.append('sugar')

    def add_milk(self):
        print('Add milk in cup')
        self.add_ingr.append('milk')

    def add_syrup(self):
        print('Add syrup in cup')
        self.add_ingr.append('syrup')

    def prepare(self):
        print('Prepare Cappuccino:')
        self.add_coffee()
        self.add_sugar()
        self.add_milk()
        choice = input('Do you want to add syrup Y/N: ').lower()
        if choice == 'y':
            self.add_syrup()
        print(f'Ingredients: {self.add_ingr}')


class Americano(Drink):
    def __init__(self):
        super().__init__('Americano')

    def add_coffee(self):
        print('To add coffee to coffee machine')
        self.add_ingr.append('coffee')

    def add_sugar(self):
        print('Put sugar in cup')
        self.add_ingr.append('sugar')

    def add_water(self):
        print('Add more water in cup')
        self.add_ingr.append('additional portion of water')

    def add_syrup(self):
        print('Add syrup in cup')
        self.add_ingr.append('syrup')

    def add_milk(self):
        print('Add milk in cup')
        self.add_ingr.append('milk')

    def prepare(self):
        print('Prepare Americano:')
        self.add_coffee()
        self.add_sugar()
        self.add_water()
        choice1 = input('Do you want to add milk Y/N: ').lower()
        if choice1 == 'y':
            self.add_milk()
        choice2 = input('Do you want to add syrup Y/N: ').lower()
        if choice2 == 'y':
            self.add_syrup()
        print(f'Ingredients: {self.add_ingr}')


class Mocha(Drink):
    def __init__(self):
        super().__init__('Moccaccino')

    def add_coffee(self):
        print('To add coffee to coffee machine')
        self.add_ingr.append('coffee')

    def add_sugar(self):
        print('Put sugar in cup')
        self.add_ingr.append('sugar')

    def add_chocolate(self):
        print('Put chocolate in cup')
        self.add_ingr.append('chocolate')

    def add_milk(self):
        print('Add milk in cup')
        self.add_ingr.append('milk')

    def add_syrup(self):
        print('Add syrup in cup')
        self.add_ingr.append('syrup')

    def prepare(self):
        print('Prepare Moccaccino:')
        self.add_coffee()
        self.add_sugar()
        self.add_chocolate()
        choice1 = input('Do you want to add milk Y/N: ').lower()
        if choice1 == 'y':
            self.add_milk()
        choice2 = input('Do you want to add syrup Y/N: ')
        if choice2 == 'y':
            self.add_syrup()

        print(f'Ingredients: {self.add_ingr}')


def coffee():
    try:
        while True:
            print('What type of coffee do you want?')
            print('1. Latte')
            print('2. Cappuccino')
            print('3. Americano')
            print('4. Moccaccino')
            print('5. Exit')
            choice = input('Enter your choice: ')
            if choice == '1':
                latte = Latte()
                latte.prepare()
            elif choice == '2':
                cappuccino = Cappuccino()
                cappuccino.prepare()
            elif choice == '3':
                americano = Americano()
                americano.prepare()
            elif choice == '4':
                mocha = Mocha()
                mocha.prepare()
            elif choice == '5':
                break
            else:
                print('Invalid choice. Please enter a number between 1 and 5.')
    except Exception as e:
        print('The error is: ', e)

coffee()