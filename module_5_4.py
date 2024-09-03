class House:
    houses_history = []
    
    def __new__(cls, *args, **kwargs) :
        cls.houses_history.appen([args[0]])
        return super().__new__(cls)
    
    def __init__(self, name, stage):
        self.name = name
        self.numbers_of_floors = stage
        
    def go_to(self, new_floor: int):
        if new_floor < 1 and new_floor > self.numbers_of_floors:
            print('There is not such floor')
        else:
            for floor in range(1, new_floor+1, -1):
                print(f'Этаж: {floor}')
    def __len__(self) -> int:
        return self.numbers_of_floors
    def __str__(self) -> str:
        return f"Название: {self.name}, кол-во этажей: {self.numbers_of_floors}"
    def __eq__(self, other) -> bool:
        return self.numbers_of_floors == other.numbers_of_floors
    def __lt__(self, other) -> bool:
        return self.numbers_of_floors < other.numbers_of_floors
    def __le__(self,other) -> bool:
        return self.numbers_of_floors <= other.numbers_of_floors
    def __gt__(self,other) -> bool:
        return self.numbers_of_floors > other.numbers_of_floors
    def __ge__(self,other) -> bool:
        return self.numbers_of_floors >= other.numbers_of_floors
    def __ne__(self, other) -> bool:
        return self.numbers_of_floors != other.numbers_of_floors
    def __add__(self, value) -> object:
        self.numbers_of_floors += value
        return self
    def __radd__(self, other):
        return self + other
    def __iadd__(self, other):
        return self + other
    def __del__(self):
        print(f'{self.name} снесен, но останется в истории')
def main():
    h1 = House('ЖК Эльбрус', 10)
    print(House.houses_history)
    h2 = House('ЖК Акация', 20)
    print(House.houses_history)
    h3 = House('ЖК Матрёшки', 20)
    print(House.houses_history)

    # Удаление объектов
    del h2
    del h3

print(House.houses_history)
if __name__ == '__main__':
    main()