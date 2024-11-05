from flask import Flask,render_template,request,jsonify,url_for,redirect,flash,session,Response
import webview
import calendar
from tkinter import *
import requests

import datetime
import webview.menu as wm
import os
import django

from tkinter import messagebox
import tkinter as tk
import httpx
from zk import ZK, const
import pandas as pd
import xlsxwriter
import time

import itertools
import threading








software_id = 1214
software_version = 1.0
software_name = "Hadi-Attendence-Tracking"


static = os.path.abspath("static")
templete = os.path.abspath("templete")


app = Flask(__name__, static_folder=static,template_folder=templete)
app.secret_key = "__secret_key__" 



# try:
# serverip = ServerIP.objects.all()[0]


    


@app.route('/' , methods =["GET", "POST"])
def home():
    return render_template('index.html')


@app.route('/save_contact' , methods =["GET", "POST"])
def save_contact():
    return render_template('save_contact.html')





if __name__ == '__main__':
    webview.settings['ALLOW_DOWNLOADS'] = True
    window = webview.create_window('HAT (Hadi Attendance Tracking)',
                                   app,text_select=True,width=1400, 
                                   height=700,min_size=(1400,700),
                                   focus=True) # min_size=(1200,700)
    
    webview.start(window,
        debug=False,
                  http_server=True
                  
                  )