# -*- coding: utf-8 -*-
"""

Created on Thu Dec  10 15:48:45 2021
#   code to create a submission form for setting the threshold for parameters

@author: User
"""

import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

dropdown_network = dbc.DropdownMenu(
    label="Select network",
    children=[
        dbc.DropdownMenuItem("Glo Nigeria"),
        dbc.DropdownMenuItem("MTN Nigeria"),
        dbc.DropdownMenuItem("Airtel Nigeria")
    ],
)

dropdown_para = dbc.DropdownMenu(
    label="Select ",
    children=[
        dbc.DropdownMenuItem("Uplaod"),
        dbc.DropdownMenuItem("Download"),
        dbc.DropdownMenuItem("Latency"),
        dbc.DropdownMenuItem("Jitter")
    ],
)
button = dbc.Button("View Map", className="me-1"), 



dash.register_page(__name__, name='View Map')

layout = html.Div(
    [
    # Row one
    dbc.Row([
        dbc.Col(html.Div(dropdown_network), width=6, lg=3),
        dbc.Col(html.Div(dropdown_para), width=6, lg=3),
        dbc.Col(html.Div(button), width=6, lg=3),
        
        #form
        ],justify="center", ),
    
    # row two 
       dbc.Row([]) 
    ]
)

