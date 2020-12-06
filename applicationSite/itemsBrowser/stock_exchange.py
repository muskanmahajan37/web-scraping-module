import threading
import json
import requests
from decouple import config
from datetime import datetime


def save_exchange(response):
    with open('currencies.txt', 'w+') as output_file:
        output_file.write(response)


class StockRequester(threading.Thread):
    def __init__(self, hour=8, minutes=55):
        threading.Thread.__init__(self)
        self.url = f'https://free.currconv.com/api/v7/convert?q=USD_PLN,EUR_PLN&compact=ultra&apiKey=' + \
                   f'{config("CURRENCY_API_KEY")}'
        self.hour = hour
        self.minutes = minutes
        self.update = False
        self.date_day = datetime.now().strftime('%D')

    def run(self):
        while True:
            if self.date_day != datetime.now().strftime('%D'):
                self.update = False
                self.date_day = datetime.now().strftime('%D')
                print("Day Changed")
            if datetime.now().strftime('%H:%M:%S') == f'{self.hour}:{self.minutes}:20' and not self.update:
                self.update = True
                response = requests.request("GET", self.url)
                save_exchange(response.text)
                print(response.text)


stock_req = StockRequester(23, 18)
stock_req.start()
