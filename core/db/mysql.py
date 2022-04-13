import mysql.connector
import sys
import boto3
import os
sys.path.append('..')
import csv
from datetime import datetime
import pandas as pd
from core.config.env import MYSQL_ENDPOINT, MYSQL_PORT, MYSQL_USR, MYSQL_REGION, MYSQL_DBNAME, MYSQL_PWD, MYSQL_SSL_CA, MYSQL_BOTOPROFILENAME

ENDPOINT=MYSQL_ENDPOINT
PORT=MYSQL_PORT
USR=MYSQL_USR
REGION=MYSQL_REGION
DBNAME=MYSQL_DBNAME
PWD=MYSQL_PWD
MYSQL_SSL_CA=MYSQL_SSL_CA
os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'

#gets the credentials from .aws/credentials
session = boto3.Session(profile_name=BOTOPROFILENAME)
client = session.client('rds')

token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USR, Region=REGION)


def run_sql(query, save):
    """
    Run a sql query to wyre prod DB 
    Parameters
    __________
    query: str
        string w/ query location
    save: str
        location of where you want data output to be saved
    """
    t0 = datetime.now()
    try:
        logging.info('Starting query')
        conn =  mysql.connector.connect(host=ENDPOINT, user=USR, passwd=token, port=PORT, database=DBNAME, ssl_ca=MYSQL_SSL_CA, password=PWD)
        cur = conn.cursor()
        with open(query, 'r') as q:
            query = q.read()
        
        cur.execute(query)
        
        field_names = [i[0] for i in cur.description]
        query_results = cur.fetchall()
        # print(field_names)
        # print(query_results)
        
        tquery = datetime.now() - t0

        t1 = datetime.now()
        with open(save, 'w') as dataout:
            writer = csv.writer(dataout)
            writer.writerow(field_names) 
            writer.writerows(query_results)
        
        tsave = datetime.now() - t1
        print("Data writen")
        size = 1e-6*os.path.getsize(save)
        print("Data Size: {0} MB\nTime Taken to execute query: {1}\nTime taken to save data: {2}".format(size, tquery.seconds/60, tsave.seconds/60))

    
        
    except Exception as e:
        print("Database connection failed due to {}".format(e))


def query_mysql(query):
    """
    Run a sql query to wyre prod DB 
    Parameters
    __________
    query: str
        docstring w/ query to execute
    """
    t0 = datetime.now()
    try:
        conn =  mysql.connector.connect(host=ENDPOINT, user=USR, passwd=token, port=PORT, database=DBNAME, ssl_ca=MYSQL_SSL_CA, password=PWD)
        cur = conn.cursor()
        cur.execute(query)
        
        field_names = [i[0] for i in cur.description]
        query_results = cur.fetchall()

        df = pd.DataFrame(data=query_results, columns = field_names)
        df = df.dropna(axis=0, how='all').dropna(axis=1, how='all')
        
        return df

    
        
    except Exception as e:
        print("Database connection failed due to {}".format(e))