import sys
import logging
import src.rds_config
import pymysql
#import os
import requests
import json
import time
import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from datetime import datetime
 

rds_host = src.rds_config.db_endpoint
name = src.rds_config.db_username
password = src.rds_config.db_password
db_name = src.rds_config.db_name
port = 3306
logger = logging.getLogger()
logger.setLevel(logging.INFO)
APIKEY = "58c66e96f312aedb78f7f726e5da74ec7ade7e33"
NAME = "Dublin"
STATIONS_URL = "https://api.jcdecaux.com/vls/v1/stations"
try:
    conn = pymysql.connect(rds_host, user=name,
    passwd=password, db=db_name, connect_timeout=10000)
    test = True
    curs = conn.cursor()
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    test = False
    sys.exit()
    
while test == True:
    x = int(input('enter stop number'))
    sql = "SELECT * From dublin_bikes_dynamic WHERE number = {0} ORDER BY last_update DESC Limit 1;".format(x)
    curs.execute(sql)
    for row in curs.fetchall():
        print (row)
    
    
    
    labels = 'Available Bikes {0}'.format(row[4]), 'Unavailable Bikes {0}'.format(row[5])
    sizes = [row[4], row[5]]
    colors = ['yellowgreen', 'teal']
    plt.title('{0}, ({1}) \n Status:{2} \n {3}'.format(row[1], row[0], row[2], 3)) 
    
    plt.pie(sizes, labels=labels, colors=colors, autopct=None ,startangle=140)
    patches, texts = plt.pie(sizes, colors=colors)
    plt.legend(patches, labels, loc="best") 
    plt.axis('equal')
    plt.show()