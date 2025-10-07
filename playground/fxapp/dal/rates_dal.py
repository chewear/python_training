from utils.file_util import read_json_as_dict

class RateDao:
    def __init__(self):
        self.fetched_currency = read_json_as_dict("rates.json")

    def get_rates(self):
        return self.fetched_currency
    
    def get_currency_rate(self, currency):
        rates = self.fetched_currency
        return rates["rates"][currency]
