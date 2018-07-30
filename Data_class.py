#!usr/bin/python2.7


# price class
class Price:

    def __init__(self, symbol, date, price):
        self.symbol = symbol
        self.date = date
        self.price = price

    def __str__(self):
        return "symbol: " + self.symbol + " date: " + self.date + " price: " + self.price

    def get_symbol(self):
        return self.symbol

    def get_price(self):
        return self.price

    def get_date(self):
        return self.date


# rate class
class Rate:

    def __init__(self, base, term, date, fx_rate):
        self.base = base
        self.term = term
        self.date = date
        self.fx_rate = fx_rate

    def __str__(self):
        return "base: " + self.base + " term: " + self.term + " date: " + self.date + " fx_rate: " + self.fx_rate

    def get_base(self):
        return self.base

    def get_term(self):
        return self.term

    def get_date(self):
        return self.date

    def get_fx(self):
        return self.fx_rate


# report class
class Report:

    def __init__(self, report_symbol, report_price, report_qty, report_ccy, report_fx, report_val):
        self.symbol = report_symbol
        self.price = report_price
        self.qty = report_qty
        self.ccy = report_ccy
        self.fx = report_fx
        self.val = report_val

    def __str__(self):
        # return self.symbol + "\t\t" + str(self.price) + "\t" + str(self.qty) + "\t" + self.ccy + "\t" + str(self.fx) + "\t" + str(self.val)
        return "%6s\t%.2f\t%d\t% 6s\t%f\t%.2f" % (self.symbol, float(self.price), int(self.qty), self.ccy, float(self.fx), float(self.val))

    def get_symbol(self):
        return self.symbol

    def get_price(self):
        return self.price

    def get_qty(self):
        return self.qty

    def get_ccy(self):
        return self.ccy

    def get_fx(self):
        return self.fx

    def get_val(self):
        return self.val
