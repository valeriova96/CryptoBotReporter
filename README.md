# CryptoBotReporter #

A Python program that fetches specific data from [Coin Market Cap](https://coinmarketcap.com/) and saves in a .json file some useful information.

## What does the reporter retrieve ##

When started, the reporter will enter in an infinite cycle and every 10 minutes it will print onto a .json file the following data:

* _best_currencies_: a list containing the 10 best currencies for the last 24 hours, measured in percentage value change;
* _worst_currencies_: a list containing the 10 worst currencies for the last 24 hours, measured in percentage value change;
* _highest_volume_currency_: the currency having the highest volume (in $) for the last 24 hours;
* _top_20_expense_: the amount of money needed to buy one unit of each of the top 20 currencies (according to [Coin Market Cap's](https://coinmarketcap.com/) ranking)
* _top_volume_expense_: the amount of money needed to buy one unit of each currency having a volume larger than $76.000.000;
* _percentage_change_: the overall percentage (positive or negative) obtained by the possible purchase of each one of the top 20 currencies [Coin Market Cap's](https://coinmarketcap.com/) of the last 24 hours (we imagine that the purchase happened the day before);
