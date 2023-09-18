from forex_python.converter import CurrencyCodes, CurrencyRates, RatesNotAvailableError

rates = CurrencyRates()
codes = CurrencyCodes()


def check_currency_code(code):
   

    return codes.get_currency_name(code) is not None


def convert_to_pretty(code_from, code_to, amt):


    try:
        amt = f"{rates.convert(code_from, code_to, amt):.2f}"
    except RatesNotAvailableError:
        return None

    symbol = codes.get_symbol(code_to)
    return f"{symbol} {amt}"
