from bll.rates_bll import RatesBll

class RatesController:
    def __init__(self):
        self.rates_bll = RatesBll()
    
    def retrieve_rates(self):
        return self.rates_bll.get_rates_data()
