#!usr/bin/python2.7

import sys
from Data_class import Price, Rate, Report

# index data
index_tup = {}
index_data = open("indices.csv", "r")
for index_line in index_data:
    index_line = index_line.strip("\n")
    indices = index_line.split(",")
    index_tup[indices[0]] = indices[1]

index_data.close()
# print(index_tup)

# portfolio data
portfolio_tup = {}
portfolio_data = open("portfolio.csv", "r")
for portfolio_line in portfolio_data:
    portfolio_line = portfolio_line.strip("\n")
    portfolios = portfolio_line.split(",")
    portfolio_tup[portfolios[0]] = portfolios[1]

portfolio_data.close()
# print(portfolio_tup)

# securities data
securities_tup = {}
securities_data = open("securities.csv", "r")
for securities_line in securities_data:
    securities_line = securities_line.strip("\n")
    securities = securities_line.split(",")
    securities_tup[securities[0]] = securities[1]

securities_data.close()
# print(securities_tup)


# price data
price_list = []
prices_data = open("prices.csv", "r")
for prices_line in prices_data:
    prices_line = prices_line.strip("\n")
    prices = prices_line.split(",")
    price1 = Price(prices[0], prices[1], prices[2])
    price_list.append(price1)

prices_data.close()
# print(price_list[1])


# rates data
rate_list = []
rates_data = open("Rates.csv", "r")
for rates_line in rates_data:
    rates_line = rates_line.strip("\n")
    rates = rates_line.split(",")
    rate1 = Rate(rates[0], rates[1], rates[2], rates[3])
    rate_list.append(rate1)

rates_data.close()
# print(rate_list[1])

# report
try:
    month = int(input("Please enter month(1-12): "))
except Exception:
    print("The inputted data is an error data! Please enter example 1, 2, ... , 11, 12")
    sys.exit(0)

if int(month) > 12 or int(month) < 0:
    print("The inputted data is an error data! Please enter example 1, 2, ... , 11, 12")
    sys.exit(0)

report_date = ""
if month < 10:
    report_date = "0" + str(month) + "/01/2017"
else:
    report_date = str(month) + "/01/2017"

report_list = []
for report_price_symbol in price_list:
    if report_price_symbol.get_date() == report_date:
        report_symbol = report_price_symbol.get_symbol()
        report_price = report_price_symbol.get_price()
        report_index = securities_tup[report_symbol]
        report_ccy = index_tup[report_index]
        report_qty = portfolio_tup[report_symbol]
        report_fx = 1
        for report_rate_data in rate_list:
            if report_rate_data.get_date() == report_date:
                if report_ccy == "JPY" and report_rate_data.get_term() == report_ccy:
                    report_fx = 1 / float(report_rate_data.get_fx())
                else:
                    if report_rate_data.get_base() == report_ccy:
                        report_fx = float(report_rate_data.get_fx())
        report_val = float(report_price) * int(report_qty) * float(report_fx)
        report1 = Report(report_symbol, report_price, report_qty, report_ccy, report_fx, report_val)
        report_list.append(report1)

print "Symbol\tPrice\tQty\tCCY\tFX Rate\tVal(USD)"
total_val = 0.0
for report in report_list:
    total_val = total_val + report.get_val()
    print (report)

print "\nTotal value on " + report_date + "  " + str(total_val) + " USD"
