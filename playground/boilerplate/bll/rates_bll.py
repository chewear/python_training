from dal.abstract_rates import RateABC
from dal.dal_factory import RatesFactory
from util.logger import enable_logger
from domain.rates import Rates 

class RatesBll:
    __rate_dao: RateABC

    def __init__(self, data_source: str):
        self.__rate_dao = RatesFactory().create_instance(data_source)

    @enable_logger
    def get_rates_data(self, base: str) -> Rates:
        return self._convert_rates_to_base(self.__rate_dao.get_rates(), base)

    def _convert_rates_to_base(self, rates_data: dict, new_base: str) -> Rates:
        new_base = new_base.upper()
        
        if new_base not in rates_data["rates"]:
            raise ValueError(f"Currency '{new_base}' not found in available rates")
        
        new_base_rate = rates_data["rates"][new_base]

        converted_rates = {}
        for currency, rate in rates_data["rates"].items():
            converted_rates[currency] = round(rate / new_base_rate, 6)
        
        return {
            "base": new_base,
            "date": rates_data["date"],
            "rates": converted_rates
        }


    @enable_logger
    def convert_amount(self, source: str, target: str, amount: float):
        if (amount <= 0):
            raise ValueError("Amount must be greater than zero.")

        source = source.upper()
        target = target.upper()
        get_rate = self.__rate_dao.get_currency_rate
        converted_amount = 0.0

        
        source_rate = get_rate(source)
        target_rate = get_rate(target)

        base_amount = float(amount) * source_rate
        converted_amount = round(base_amount / target_rate, 2)

        return {
            "source_currency": source,
            "target_currency": target,
            "amount_to_be_converted": amount,
            "converted_amount": converted_amount
        }
