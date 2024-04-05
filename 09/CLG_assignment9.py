class KitchenAppliance:

    def __init__(self, model_number, brand):
        self.model_number = model_number
        self.brand = brand

    def report(self):
        print("This is " + str(self.model_number) + " from " + self.brand)


class SmartCoffeeMachine(KitchenAppliance):

    def __init__(self, model_number, brand, coffee_menu=['latte', 'cappuccino', 'flat white']):
        KitchenAppliance.__init__(self, model_number, brand)
        self.coffee_menu = coffee_menu

    def update_menu(self, new_coffee):
        if new_coffee not in self.coffee_menu:
            self.coffee_menu.append(new_coffee)
            print(f'{new_coffee} has now been added to the menu\n{self.coffee_menu}')
        else:
            print(f'You\'re in luck! {new_coffee} is already on the menu')
        
    def make_coffee(self, coffee_type):
        if coffee_type not in self.coffee_menu:
            print(f'I\'m sorry, I don\'t know how to make {coffee_type}. Please choose a drink from the menu below and try again:\n{self.coffee_menu}')
        else:
            print(f'Preparing your coffee... \nYour {coffee_type} is ready!')
        

my_coffee_machine = SmartCoffeeMachine(12334254, 'Ragdoll')
my_coffee_machine.report()
my_coffee_machine.update_menu('latte')
my_coffee_machine.update_menu('hazelnut latte')
my_coffee_machine.make_coffee('hazelnut latte')
my_coffee_machine.make_coffee('salted caramel latte')