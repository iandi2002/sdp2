class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.product.price * item.quantity
        return total

def print_catalog(catalog):
    print("Каталог товаров:")
    for name, price in catalog.items():
        print(f"{name}: {price} тнг")

def print_cart(cart):
    print("Товары в корзине:")
    for item in cart.items:
        print(f"{item.product.name}: {item.quantity} шт.")

def main():
    catalog = {
        "Футболка": 1000.0,
        "Юбка": 2000.0,
        "Шорты": 3000.0,
        "Брюки": 10500.0,
        "Топ": 200.0,
        "Джинсы": 5000.0,
        "Рубашка": 11000.0,
        "Кофта": 1200.0,
    }

    print_catalog(catalog)

    cart = ShoppingCart()

    while True:
        print("Меню:")
        print("1. Добавить товар в корзину")
        print("2. Просмотреть корзину")
        print("3. Рассчитать итоговую сумму")
        print("4. Выйти из программы")

        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Введите название товара: ")
            if name in catalog:
                quantity = int(input("Введите количество: "))
                price = catalog[name]
                product = Product(name, price)
                item = CartItem(product, quantity)
                cart.add_item(item)
                print(f"{quantity} {name} добавлено в корзину.")
            else:
                print("Такой товар не найден в каталоге.")

        elif choice == "2":
            print_cart(cart)

        elif choice == "3":
            total = cart.calculate_total()
            print(f"Итоговая сумма: {total} тнг")

        elif choice == "4":
            print("Спасибо за покупки!")
            break

        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
