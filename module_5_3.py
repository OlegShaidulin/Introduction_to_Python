class House:
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
        if isinstance(other, House):
            return self.numbers_of_floors == other.numbers_of_floors
        elif isinstance(other, int):
            return self.numbers_of_floors == other
    def __lt__(self, other) -> bool:
        if isinstance(other, House):
            return self.numbers_of_floors < other.numbers_of_floors
        elif isinstance(other, int):
            return self.numbers_of_floors < other
    def __le__(self,other) -> bool:
        if isinstance(other, House):
            return self.numbers_of_floors <= other.numbers_of_floors
        elif isinstance(other, int):
            return self.numbers_of_floors <= other
    def __gt__(self,other) -> bool:
        if isinstance(other, House):
            return self.numbers_of_floors > other.numbers_of_floors
        elif isinstance(other, int):
            return self.numbers_of_floors > other
    def __ge__(self,other) -> bool:
        if isinstance(other, House):
            return self.numbers_of_floors >= other.numbers_of_floors
        elif isinstance(other, int):
            return self.numbers_of_floors >= other
    def __ne__(self, other) -> bool:
        if isinstance(other, House):
            return self.numbers_of_floors != other.numbers_of_floors
        elif isinstance(other, int):
            return self.numbers_of_floors != other
    def __add__(self, value) -> object:
        self.numbers_of_floors += value
        return self
    def __radd__(self, other: int):
        return self.__add__(other)
    def __iadd__(self, other: int):
        return self.__add__(other)
def main():
    h1 = House('ЖК Эльбрус', 10)
    h2 = House('ЖК Акация', 20)

    print(h1)
    print(h2)

    print(h1 == h2) # __eq__

    h1 = h1 + 10 # __add__
    print(h1)
    print(h1 == h2)

    h1 += 10 # __iadd__
    print(h1)

    h2 = 10 + h2 # __radd__
    print(h2)

    print(h1 > h2) # __gt__
    print(h1 >= h2) # __ge__
    print(h1 < h2) # __lt__
    print(h1 <= h2) # __le__
    print(h1 != h2) # __ne__
    
if __name__ == '__main__':
    main()