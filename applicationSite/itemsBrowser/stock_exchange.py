import threading
import json
import requests
import psycopg2
from decouple import config
from datetime import datetime


def save_exchange(json_response):
    currencies = json.loads(json_response)
    currencies['SupEuro'] = 4.732
    currencies['PLN'] = 1.0
    currencies['JPY'] = 0.037

    for key in currencies:
        inserted_data = (key, currencies[key])
        print(inserted_data)

    try:
        connection = psycopg2.connect(user=config('DB_CURRENCY_UPDATER'),
                                      password=config('DB_CURRENCY_UPDATER_PASS'),
                                      port=config('DB_PORT'),
                                      database=config('DB_NAME'),
                                      host=config('DB_HOST'))
        cursor = connection.cursor()
        select_query = """SELECT * FROM "itemsBrowser_currencies" """
        cursor.execute(select_query)
        curr_values = cursor.fetchall()
        if not curr_values:
            insert_query = """INSERT INTO "itemsBrowser_currencies" (currency_name, exchange_rate_to_pln) VALUES  (%s, %s)"""
            for key in currencies:
                inserted_data = (key[:3], currencies[key])
                cursor.execute(insert_query, inserted_data)
            connection.commit()
        else:
            insert_query = """ UPDATE "itemsBrowser_currencies" SET "exchange_rate_to_pln"=%s WHERE "currency_name"=%s"""
            for key in currencies:
                inserted_data = (currencies[key], key[:3])
                cursor.execute(insert_query, inserted_data)
            connection.commit()
    except(Exception, psycopg2.Error) as insert_error:
        if (connection):
            print('Error occurred during inserting data to database in currency module', insert_error)
    finally:
        if (connection):
            cursor.close()
            connection.close()


class StockRequester(threading.Thread):
    def __init__(self, hour='8', minutes='55'):
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
            if datetime.now().strftime('%H:%M:%S') == f'{self.hour}:{self.minutes}:00' and not self.update:
                self.update = True
                response = requests.request("GET", self.url)
                print(response.text)
                save_exchange(response.text)


sr = StockRequester('16', '04')
sr.start()
