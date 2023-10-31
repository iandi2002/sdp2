
class ClothingStore:
    _instance = None 

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ClothingStore, cls).__new__(cls)
            cls._instance.init_store() 
        return cls._instance

    def init_store(self):
        self.inventory = {} 
        self.discount_strategy = None 

    def set_discount_strategy(self, strategy):
        self.discount_strategy = strategy

    def add_item(self, item_name, price):
        self.inventory[item_name] = price

    def calculate_discounted_price(self, item_name):
        if item_name in self.inventory:
            original_price = self.inventory[item_name]
            if self.discount_strategy:
                return self.discount_strategy.apply_discount(original_price)
            else:
                return original_price
        else:
            return None


class DiscountStrategy:
    def apply_discount(self, original_price):
        pass


class NoDiscountStrategy(DiscountStrategy):
    def apply_discount(self, original_price):
        return original_price


class PercentageDiscountStrategy(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, original_price):
        return original_price * (1 - self.percentage / 100)

def main():
    store = ClothingStore()

  
    store.add_item("Футболка", 20.0)
    store.add_item("Джинсы", 50.0)
    store.add_item("Платье", 80.0)
    store.add_item("Шорты", 10.0)
    store.add_item("Куртка", 30.0)
    store.add_item("Юбка", 150.0)
    store.add_item("Брюки", 70.0)
    store.add_item("Топ", 50.0)

   
    print("Доступные товары:")
    for item in store.inventory:
        print(f"{item}: ${store.inventory[item]:.2f}")

    
    discount_percentage = float(input("Введите процент скидки: "))
    store.set_discount_strategy(PercentageDiscountStrategy(discount_percentage))

   
    item_name = input("Введите название товара: ")
    discounted_price = store.calculate_discounted_price(item_name)
    if discounted_price is not None:
        print(f"Цена товара с учетом скидки: ${discounted_price:.2f}")
    else:
        print("Такой товар не найден")

if __name__ == "__main__":
    main()
