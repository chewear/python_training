from dal.rates_dal import RateDao

class RatesBll:
    def __init__(self):
        self.rateDao = RateDao()

    def get_rates_data(self):
        return self.rateDao.get_rates()


    def convert_amount(self, source: str, target: str, amount: float) -> float:
        source = source.upper()
        target = target.upper()
        rates = self.rateDao.get_rates()
        get_curr_rate =  self.rateDao.get_currency_rate

        if source == target:
            return float(amount)
        try:
            if source == "PHP":
                target_rate = get_curr_rate(target)
                return float(amount) / target_rate
            elif target == "PHP":
                source_rate = get_curr_rate(source)
                return float(amount) * source_rate
            else:
                source_rate = get_curr_rate(source)
                target_rate = get_curr_rate(target)

                php_amount = float(amount) * source_rate
                return php_amount / target_rate
        except KeyError:
            raise Exception(f"Invalid currency. Available currencies: {list(rates['rates'].keys())}")