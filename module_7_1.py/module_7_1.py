
class Product():
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.caregory = category
    def __str__(self) -> str:
        return f'{self.name}, {self.weight}, {self.caregory}'
    
class Shop():
    __file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name, 'r')
        prod_str = file.read()
        file.close
        return prod_str
    def add(self, *products):
        file_get = self.get_products()
        for item in products:
            if self.get_products().find(f'{item.name},') == -1:
                file = open(self.__file_name, 'a')
                file.write(f'{item}\n')
                file.close()
            else:
                print(f'Продукт {item.name} уже есть в магазине')
                
shop1 = Shop()
product4 = Product('Apple1', 0.4,'Fruits')
product2 = Product('Apple', 0.3,'Fruits')
product1 = Product('Cucumber', 5.3,'Vegetables')
product3 = Product('Peach', 2, 'Fruits')
print(product2)
shop1.add(product1, product2, product3, product4, product2)
print(f'\n{shop1.get_product()}')
        