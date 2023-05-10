# -*- coding: utf-8 -*-
"""

Created on Thu Dec  10 11:48:45 2021
#   - Code for dashbaord for the oil and gas pipeline parameters
@author: User
"""

import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc

import pandas as pd
from datetime import datetime as dt
import plotly.express as px
import dash_daq as daq
import random

from urllib.request import urlopen
import json

#import mysql.connector
#from mysql.connector import Error


dash.register_page(__name__, name='Dashboard')



# Create Page Layout
layout = html.Div(
    
    )
   


