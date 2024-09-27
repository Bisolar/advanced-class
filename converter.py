message = print("Currency Exchange options:\n1. GBP to NGN\n2. USD to NGN\n3. AUD to NGN\n4. EUR to NGN\n5. CAD to NGN\n6. JPY to NGN ")
user_choice= int(input("\nPlease choose an option from (1-6)\n>>"))
value = int(input("\nEnter amount: "))

class CurrencyEx:
    def __init__(self, value):
        self.value = value
        self.gbp = 2182
        self.usd = 1636
        self.aud = 1114
        self.eur = 1829
        self.cad = 1204
        self.jpy = 11

    def converter(self):
        if user_choice == 1:
            cal = self.value * self.gbp
            return cal
        elif user_choice ==2:   
            cal1 = self.value * self.usd
            return cal1
        elif user_choice ==3:
            cal2 = self.value * self.aud
            return cal2
        elif user_choice ==4:
            cal3 = self.value * self.eur
            return cal3
        elif user_choice ==5:
            cal4 = self.value * self.cad
            return cal4
        elif user_choice == 6:
            cal5 = self.value * self.jpy
            return cal5
        else:
            print("The option you entered is invalid")
    
amount = CurrencyEx(value)
new_amount= amount.converter()
print(new_amount)