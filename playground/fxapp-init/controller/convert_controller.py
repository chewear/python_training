from bll.rates_bll import RatesBll

class ConvertMoney:
    def __init__(self):
        self.ratesbll = RatesBll()

    def convert(self, source: str, target: str, amount: float) -> float:
        return self.ratesbll.convert_amount(source, target, amount)
    
        