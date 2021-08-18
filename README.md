# CryptoBotReporter #

A Python program that fetches specific data from [CoinmarketCap](https://coinmarketcap.com/) and saves in a .json file some useful information.

## What does the reporter retrieve ##

When started, the reporter will enter in an infinite cycle and every 10 minutes it will print onto a .json file the following data:

* #### best_currencies: ####a list containing the 10 best currencies for the last 24 hours, measured in percentage value change;
*
