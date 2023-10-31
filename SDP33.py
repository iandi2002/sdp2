class CurrencyConverter:
    def convert_tenge_to_rubles(self, tenge_amount):
        rubles_amount = tenge_amount / 5
        return rubles_amount

class CurrencyConverterAdapter:
    def __init__(self, converter):
        self.converter = converter

    def convert_tenge_to_dollars(self, tenge_amount):
        rubles_amount = self.converter.convert_tenge_to_rubles(tenge_amount)
        dollars_amount = rubles_amount / 75  
        return dollars_amount

if __name__ == "__main__":
    converter = CurrencyConverter()
    adapter = CurrencyConverterAdapter(converter)

    tenge_amount = float(input("Введите сумму в тенге: "))
    rubles_amount = converter.convert_tenge_to_rubles(tenge_amount)
    dollars_amount = adapter.convert_tenge_to_dollars(tenge_amount)

    # Форматирование чисел с двумя знаками после запятой
    rubles_formatted = "{:.2f}".format(rubles_amount)
    dollars_formatted = "{:.2f}".format(dollars_amount)

    print(f"{tenge_amount} тенге равно {rubles_formatted} рублей.")
    print(f"{tenge_amount} тенге равно {dollars_formatted} долларам.")
