import json
import requests
from pprint import pprint
import time
from datetime import date, datetime
from config import my_api_key


class Reporter:
    def __init__(self):
        self.url = ' https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        self.params = {'start': '1', 'limit': '100', 'convert': 'USD'}
        self.headers = {'Accepts': 'application/json',
                        'X-CMC_PRO_API_KEY': my_api_key}
        self.data = {}

    '''
    Fetch the top 100 ranked cryptos on coinmarketcap website 
    '''

    def fetchCurrenciesData(self):
        r = requests.get(url=self.url, headers=self.headers,
                         params=self.params).json()
        return r['data']

    '''
    Returns the 10 best cryptos (among the 100 fetched).
    The best factor is measured by taking into account the percent change
    of each crypto in the last 24 hours
    '''

    def fetchBestCryptos(self):
        currencies = self.fetchCurrenciesData()
        bestCryptos = {}
        done = False
        while(not done):
            bestCurrency = None
            for currency in currencies:
                found = 0
                if len(bestCryptos.keys()) != 0:
                    if currency['name'] in bestCryptos.keys():
                        found = 1
                if len(bestCryptos.keys()) == 0 or found == 0:
                    if bestCurrency == None or currency['quote']['USD']['percent_change_24h'] > bestCurrency['quote']['USD']['percent_change_24h']:
                        bestCurrency = currency

            if len(bestCryptos.keys()) < 10:
                bestCryptos[
                    bestCurrency['name']] = bestCurrency['quote']['USD']['percent_change_24h']
            else:
                done = True
                self.data['best_currencies'] = bestCryptos

    '''
    Similar to that above
    '''

    def fetchWorstCryptos(self):
        currencies = self.fetchCurrenciesData()
        worstCryptos = {}
        done = False
        while(not done):
            worstCurrency = None
            for currency in currencies:
                found = 0
                if len(worstCryptos.keys()) != 0:
                    if currency['name'] in worstCryptos.keys():
                        found = 1
                if len(worstCryptos.keys()) == 0 or found == 0:
                    if worstCurrency == None or currency['quote']['USD']['percent_change_24h'] < worstCurrency['quote']['USD']['percent_change_24h']:
                        worstCurrency = currency

            if len(worstCryptos.keys()) < 10:
                worstCryptos[
                    worstCurrency['name']] = worstCurrency['quote']['USD']['percent_change_24h']
            else:
                done = True
                self.data['worst_currencies'] = worstCryptos

    '''
    Retrieve the best crypto obtained through the last 24 hours volume
    '''

    def fetchHighestVolumeCrypto(self):
        currencies = self.fetchCurrenciesData()
        highestVolumeCurrency = None

        for currency in currencies:
            if not highestVolumeCurrency or highestVolumeCurrency['quote']['USD']['volume_24h'] < currency['quote']['USD']['volume_24h']:
                highestVolumeCurrency = currency

        self.data['highest_volume_currency'] = {
            highestVolumeCurrency['name']: highestVolumeCurrency['quote']['USD']['volume_24h']}

    '''
    Provides you an overview about how much you should spend in order to
    buy one unit of each of the top 20 ranked currencies
    '''

    def howMuchShouldISPend(self):
        currencies = self.fetchCurrenciesData()
        i = 0
        possibleTotalExpense = 0

        for currency in currencies:
            if i < 20:
                possibleTotalExpense += currency['quote']['USD']['price']
            else:
                break

        self.data['top_20_expense'] = possibleTotalExpense

    '''
    This method returns you the amount of money you should spend to buy
    one unit of each crypto whose market volume in the last 24 hours
    was above $76.000.000
    '''

    def moneyForHighestVolumeCryptos(self):
        currencies = self.fetchCurrenciesData()
        myVolume = 76000000
        possibleTopVolumeExpense = 0

        for currency in currencies:
            if currency['quote']['USD']['volume_24h'] > myVolume:
                possibleTopVolumeExpense += currency['quote']['USD']['price']

        self.data["top_volume_expense"] = possibleTopVolumeExpense

    '''
    Computes the total percentage that you would have got by buying 1 unit
    of each one of the first top 20 cryptos 1 day ago
    '''

    def computePercentage(self):
        currencies = self.fetchCurrenciesData()
        i = 0
        possiblePercentageChange = 0

        for currency in currencies:
            if i < 20:
                possiblePercentageChange += currency['quote']['USD']['percent_change_24h']
            else:
                break

        self.data['percentage_change'] = possiblePercentageChange


seconds = 60
minutes = 10

while(1):
    print('\nFetching data from CoinMArketCap, this may require a while...\n')
    myReporter = Reporter()
    myReporter.fetchBestCryptos()
    myReporter.fetchWorstCryptos()
    myReporter.fetchHighestVolumeCrypto()
    myReporter.howMuchShouldISPend()
    myReporter.moneyForHighestVolumeCryptos()
    myReporter.computePercentage()

    now = datetime.now()
    title = str(now) + '.json'

    with open(title, "w") as outfile:
        json.dump(myReporter.data, outfile)
    print('I wrote one report, go to check it out!\n')

    print('I\'ll wait 10 minutes...')
    time.sleep(seconds * minutes)
