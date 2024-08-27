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

def main():
    h1 = House('ЖК Горский', 18)
    h2 = House('Домик в деревне', 2)
    h1.go_to(5)
    h2.go_to(10)
if __name__ == '__main__':
    main()