import json
import requests
import psycopg2
from decouple import config
from datetime import datetime


def update_exchange_rates(json_response):
    currencies = json.loads(json_response)
    currencies['SupEuro'] = currencies['EUR_PLN'] + 0.3
    currencies['PLN'] = 1.0
    currencies['JPY'] = currencies['USD_PLN'] / 102

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


class StockRequester():
    def __init__(self):
        self.url = f'https://free.currconv.com/api/v7/convert?q=USD_PLN,EUR_PLN&compact=ultra&apiKey=' + \
                   f'{config("CURRENCY_API_KEY")}'
        self.request_time = datetime.now().strftime('%H:%M')
        self.request_flag = False
        self.date = datetime.now()

    def is_applicable(self):
        if self.request_time != datetime.now().strftime('%H:%M'):
            self.request_time = datetime.now().strftime('%H:%M')
            self.request_flag = True
        if self.request_flag:
            self.request_flag = False
            self.send_request()

    def send_request(self):
        response = requests.request("GET", self.url)
        update_exchange_rates(response.text)

