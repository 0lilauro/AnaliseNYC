# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 10:57:45 2019

@author: Lauro Oliveira <0lilauro7@gmail.com>
"""

import psycopg2
from psycopg2.extras import execute_values 
import json 
import requests
from pprint import pprint
from multiprocessing import Process
from datetime import datetime

URLS = [
    'https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2009-json_corrigido.json',
     'https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2010-json_corrigido.json',
     'https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2011-json_corrigido.json',
     'https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2012-json_corrigido.json'
]

def timerize(f):
    def remake_func(*args, **kwargs):
        start_time = datetime.now()
        f(*args, **kwargs)
        delta = datetime.now() - start_time
        pprint("Finish function {}. - time ellipsed: {}".format(f.__name__, delta))
    return remake_func


def get_connection():
    DB_HOST = 'xxxxxxx.cyy2ldnhnbji.xxxxxxxx.redshift.amazonaws.com'
    DB_USERNAME = 'populator'
    DB_PORT = '5439'
    DB_DATABASE = 'analyze'
    DB_PASSWORD = 'XXXXXXXXXXXXXX'
    
    try:
        connection = psycopg2.connect(
            host = DB_HOST,
            user = DB_USERNAME,
            password = DB_PASSWORD,
            port = int(DB_PORT),
            dbname = DB_DATABASE
        )
        return connection 
        
    except Exception as exception_connection: 
        print(str(exception_connection))
        exit("Was impossible to connect on {} database".format(DB_DATABASE))
        return None

def insert(values, con): 
    command = """
        INSERT 
        INTO NYC.TRIP (
            DROPOFF_DATETIME,
            DROPOFF_LATITUDE,
            DROPOFF_LONGITUDE,
            FARE_AMOUNT,
            PASSENGER_COUNT,
            PAYMENT_TYPE,
            PICKUP_DATETIME,
            PICKUP_LATITUDE,
            PICKUP_LONGITUDE,
            RATE_CODE,
            STORE_AND_FWD_FLAG,
            SURCHARGE,
            TIP_AMOUNT,
            TOLLS_AMOUNT,
            TOTAL_AMOUNT,
            TRIP_DISTANCE,
            VENDOR_ID
        ) VALUES %s """
        
    try:
        execute_values(con.cursor(), command, values)
    except:
        print(" ======= An erro ocurred !!")
    finally:
        con.commit()

def process_lines(url):
    con = get_connection()
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        i = 0
        counter = 0
        insertion_values = []
        for chunk in r.iter_lines(decode_unicode=True):
            if chunk:
                try:
                    chunk_dict = json.loads(chunk)
                    insertion_values.append(
                        (
                            chunk_dict['dropoff_datetime'],
                            chunk_dict['dropoff_latitude'],
                            chunk_dict['dropoff_longitude'],
                            chunk_dict['fare_amount'],
                            chunk_dict['passenger_count'],
                            chunk_dict['payment_type'],
                            chunk_dict['pickup_datetime'],
                            chunk_dict['pickup_latitude'],
                            chunk_dict['pickup_longitude'],
                            chunk_dict['rate_code'],
                            chunk_dict['store_and_fwd_flag'],
                            chunk_dict['surcharge'],
                            chunk_dict['tip_amount'],
                            chunk_dict['tolls_amount'],
                            chunk_dict['total_amount'],
                            chunk_dict['trip_distance'],
                            chunk_dict['vendor_id'],    
                        )
                    )
                    counter+= 1
                    i+= 1
                except Exception as ex : 
                    print(ex)
                    
            pprint(i)
            
            if counter >= 4000:
                insert(insertion_values, con)
                counter = 0
                insertion_values = []
            
@timerize
def pool_function(urls): 
    for url in urls:
        proc = Process(target=process_lines, args=(url,))
        proc.start()
    proc.join()

if __name__ == '__main__':
    pool_function(URLS)
    # Casa haja algum erro, foi
    # porque o arquivo corrigido ficou
    # no EC2 da Amazon.