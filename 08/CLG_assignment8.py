class SmartDevice:

    def __init__(self, model_number, brand, screen_size, app_list=[]):
        self.model_number = model_number
        self.brand = brand
        self.screen_size = screen_size
        self.app_list = app_list
        # Added a datatype check here to ensure app_list arg is provided in list format (otherwise list methods will fail)
        if type(self.app_list) != list: 
            raise TypeError("Error! Argument 'app_list' must be of datatype list")

    def report(self):
        print("This is " + str(self.model_number) + " from " + self.brand)

    def install_app(self, app_name='Demo App'):
        # Added if/else clause to avoid duplicates
        if app_name not in self.app_list:
            print(f"Installing {app_name}...")
            self.app_list.append(app_name)
        else:
            print(f"{app_name} is already installed")
        return self.app_list
    
    def delete_app(self, app_to_delete):
        if app_to_delete in self.app_list:
            print(f"Deleting {app_to_delete}...")
            self.app_list.remove(app_to_delete)
        else:
            print(f"{app_to_delete} is not installed")
        return self.app_list

# Initialising 2 Smart Device objects (one with starting app_list value and one using default app_list argument)
laptop_a = SmartDevice(12345, 'Windows', 10,['minesweeper','task scheduler'])
laptop_b = SmartDevice(12346, 'Linux', 9)

# Checking that methods work on both objects
for device in [laptop_a,laptop_b]:
    print(f"Checking object: {device}")
    device.report()
    print(f"Starting apps: {device.app_list}")

    print("test 1: install new app (specified)")
    device.install_app('arcgis pro')
    print(device.app_list)

    print("test 2: install default (unspecified) app")
    device.install_app()
    print(device.app_list)

    print("test 3: install unspecified app again (check duplicate handling)")
    device.install_app()
    print(laptop_a.app_list)

    print("test 4: delete existing app")
    device.delete_app('arcgis pro')
    print(device.app_list)

    print("test 5: delete non-existant app")
    device.delete_app('ultimate app')
    print(device.app_list)

# Testing datatype exception
bootleg_laptop = SmartDevice(12347, 'Wind0wsXP', 12, 'spyware')

