class  House:
    def __init__(self,name ,floor):
        self.name = name
        self.number_of_floors = floor
    def go_to (self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")



h1 = House('ЖК Горский', 18)

h2 = House('Домик в деревне', 2)

h3 = House('ЖК Эльбрус', 30)

h1.go_to(5)

h2.go_to(10)

h3.go_to(30)