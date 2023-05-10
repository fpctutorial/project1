# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 08:18:17 2022

@author: User
"""

import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import dash_daq as daq

dash.register_page(__name__, path='/', name='Home') # '/' is home page



dropdown = dbc.DropdownMenu(
    label="Menu",
    children=[
        dbc.DropdownMenuItem("Item 1"),
        dbc.DropdownMenuItem("Item 2"),
        dbc.DropdownMenuItem("Item 3"),
    ],
)

row_content = [
    dbc.Col(html.Div(children='Servers',
    style={'fontSize':35, 'textAlign': 'center'}), width=2),
    dbc.Col(html.Div(dropdown), width=2),
]
row_content2 = [
    dbc.Col(html.Div(children='Servers',
    style={'fontSize':35, 'textAlign': 'center'}), width=2),
    dbc.Col(html.Div(dropdown), width=2),
]


# Create Layout for the home page

layout = html.Div(
    [
        
        # First row   
        dbc.Row([
            # First Row, col one 
            dbc.Col([
                daq.Gauge(
                size = 200,
                showCurrentValue=True,
                id='my-gauge-1',
                color={"gradient":True,"ranges":{"green":[0,20],"yellow":[20,35],"red":[35,100]}},
                label="Download",
                
                value=0)
                
                ]),
            # First Row, col two 
            dbc.Col([
                daq.Gauge(
                    size = 200,
                    showCurrentValue=True,
                    id='my-gauge-2',
                    color={"gradient":True,"ranges":{"green":[0,20],"yellow":[20,35],"red":[35,100]}},
                    label="Uplaod",
                   
                    value=0)
                
                ])
        ]),
        # second row 
         
        dbc.Row([
            # Second Row, col one 
            dbc.Col([
                daq.Gauge(
                size = 200,
                showCurrentValue=True,
                id='my-gauge-3',
                color={"gradient":True,"ranges":{"green":[0,20],"yellow":[20,35],"red":[35,100]}},
                label="Ping",
                
                value=0)
                
                ]),
            # Second Row, col two 
            dbc.Col([
                daq.Gauge(
                    size = 200,
                    showCurrentValue=True,
                    id='my-gauge-4',
                    color={"gradient":True,"ranges":{"green":[0,20],"yellow":[20,35],"red":[35,100]}},
                    label="Jitter",
                   
                    value=0)
                
                ])
            
        ]),
        # Thrid Row 
        dbc.Row([
            dbc.Card(
                dbc.CardBody([
                    html.H4(children='Speed Test',
                    style={'fontSize':25, 'textAlign': 'center'}),
                    ]),
                
                )
        ]),
        # fourth row 
        dbc.Row(
            row_content,
            justify="center"
        ),
        
        # fifth row 
        dbc.Row([
            dbc.Button("Start", className="me-1")
            ])
        
        
    ]
)


