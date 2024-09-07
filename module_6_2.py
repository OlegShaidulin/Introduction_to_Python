class Venicle:
    __COLOR_VARIANTS = ['blue', 'red', 'brown', 'yellow', 'silver']
    def __init__(self, owner: str, _model: str, __engine_power: int, __color: str):
        self.owner = owner
        self._model = _model
        self.__engine_power = __engine_power
        self.__color = __color
    def get_model(self, _model):
        return f'Модель: {self._model}'
    def get_horsepower(self, __engine_power):
        return f'Мощность двигателя: {__engine_power}'
    def get_color(self, __color):
        return f'Цвет: {__color}'
    def print_info(self):
        print(self.get_model, self.get_horsepower, self.get_color)
        print(f'Владелец: {self.owner}')
    def set_color(self, new_color: str):
        if new_color.lower in __COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Venicle):
    __PASSENGERS_LIMIT = 5
    
# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'brown', 'yellow', 'silver']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

    