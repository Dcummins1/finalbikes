import os.path
from flask import Flask, Response
import sys
import logging
import pymysql
import os
import requests
import json
import time
import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from datetime import datetime


app = Flask(__name__)
app.config.from_object(__name__)


def root_dir():  
    return os.path.abspath(os.path.dirname(__file__))


def get_file(filename):
    try:
        src = os.path.join(root_dir(), filename)
        
        return open(src).read()
    except IOError as exc:
        return str(exc)


@app.route('/', methods=['GET', 'POST'])
def metrics():  
    content = get_file('templates/DublinBikes.html')
    return Response(content, mimetype="text/html")


# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def get_resource(path):  
#     mimetypes = {
#         ".css": "text/css",
#         ".html": "text/html",
#         ".js": "application/javascript",
#     }
#     complete_path = os.path.join(root_dir(), path)
#     ext = os.path.splitext(path)[1]
#     mimetype = mimetypes.get(ext, "text/html")
#     content = get_file(complete_path)
#     return Response(content, mimetype=mimetype)

@app.route("/availablebikes/<int:stand_no>")
def avail_bikes(stand_no):        
    #if test == True:
        #x = int(input('enter stop number'))
        #sql = "SELECT * From dublin_bikes_dynamic WHERE number = {0} ORDER BY last_update DESC Limit 1;".format(stand_no)
        #curs.execute(sql)
        #for row in curs.fetchall():
            #return 'Stand num: %d' % 4
    return 'hello &d' % stand_no
        
        
if __name__ == '__main__':  
    app.run(port=8080)
