class CurrencyConverterService:
    def convert(self, amount, from_currency, to_currency):
        exchange_rate = {
    'USD': {'RUB': 75.0, 'KZ': 433.0},
    'RUB': {'USD': 0.0133, 'KZ': 5.77},
    'KZ': {'USD': 0.0023, 'RUB': 0.173}
}
        return amount * exchange_rate[from_currency][to_currency]

class Adapter:
    def __init__(self):
        self.service = CurrencyConverterService()

    def convert(self, amount, from_currency, to_currency):
        return self.service.convert(amount, from_currency, to_currency)

class CurrencyConverter:
    def __init__(self, adapter):
        self.adapter = adapter

    def convert(self, amount, from_currency, to_currency):
        return self.adapter.convert(amount, from_currency, to_currency)

if __name__ == "__main__":
    adapter = Adapter()
    converter = CurrencyConverter(adapter)

    amount = float(input("Введите сумму: "))
    from_currency = input("Исходная валюта: ").upper()
    to_currency = input("Целевая валюта: ").upper()

    converted_amount = converter.convert(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} = {converted_amount} {to_currency}")
