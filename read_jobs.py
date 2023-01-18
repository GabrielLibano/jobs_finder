import base64
import pandas as pd
from serpapi import GoogleSearch
from google.cloud import bigquery
import datetime
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import dotenv
import os
import json

df = pd.read_excel("jobs.xlsx")
dft = df.to_json(orient="records")
fp = open('jobs.json', 'w')
fp.write(dft)

dfsal = pd.read_excel("salarios.xlsx")
dftsal = dfsal.to_json(orient="index")
fp = open('jobsal.json', 'w')
fp.write(dftsal)