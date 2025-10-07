from controller.convert_controller  import ConvertMoney

class ConvertMenu:
    def input_menu(self):
        print("-------------------------------")
        source_currency = input("Source Currency: ")
        target_currency = input("Target Currency: ")
        amount = float(input("Amount: "))
        result = ConvertMoney().convert(source_currency,target_currency,amount)
        print(f"Converted amount: {result}")


