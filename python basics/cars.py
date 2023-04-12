class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        
    def detail(self):
        print(f"name:{self.name} model:{self.model} year:{self.year}")

class Super_Car(Car):
    def __init__(self, name, model, year):
        super().__init__(name, model, year)
