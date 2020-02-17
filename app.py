from dash import Dash
import dash_html_components as html
import dash_daq as daq
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from ping3 import ping
from flask import Flask

server = Flask(__name__)

dash_params = {
    'indicator_width': 140,
}

ec_list = (
    '192.168.1.30',
    '192.168.1.31',
    '192.168.1.32',
    '192.168.9.33',
    # '192.168.1.34',
    # '192.168.1.35',
    # '192.168.1.36',
    # '192.168.1.37',
    # '192.168.1.38',
    # '192.168.1.39',
    # '192.168.1.40',
    # '192.168.1.41',
    # '192.168.1.42',
    # '192.168.1.44',
    # '192.168.1.45',
    # '192.168.1.46',
    # '192.168.1.47'
)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app_dash = Dash(__name__, server=server, external_stylesheets=external_stylesheets, url_base_pathname='/dashboard/')
app_dash.layout = html.Div(
    children=[
        html.Div(
            id='root_div',
            children=[
                html.Div(
                    id='ec_server_1_div',
                    children=[

                        daq.Indicator(
                            id='ec_server_1',
                            label='Serwerownia 1',
                            labelPosition='right',
                            style={'width': dash_params['indicator_width'], 'float': 'left'}
                        ),
                        html.A(
                            'Link',
                            id='ec_server_1_link',
                            href='http://192.168.1.30',
                            title='Link',
                            style={'margin-left': 20}
                        )
                    ],
                    style={'width': '100%', 'overflow': 'hidden'}
                ),
                html.Div(
                    id='ec_server_2_div',
                    children=[

                        daq.Indicator(
                            id='ec_server_2',
                            label='Serwerownia 2',
                            labelPosition='right',
                            style={'width': dash_params['indicator_width'], 'float': 'left'}
                        ),
                        html.A(
                            'Link',
                            id='ec_server_2_link',
                            href='http://192.168.1.31',
                            title='Link',
                            style={'margin-left': 20}
                        )
                    ],
                    style={'width': '100%', 'overflow': 'hidden'}
                ),
                html.Div(
                    id='ec_server_3_div',
                    children=[

                        daq.Indicator(
                            id='ec_server_3',
                            label='Serwerownia 3',
                            labelPosition='right',
                            style={'width': dash_params['indicator_width'], 'float': 'left'}
                        ),
                        html.A(
                            'Link',
                            id='ec_server_3_link',
                            href='http://192.168.1.32',
                            title='Link',
                            style={'margin-left': 20}
                        )
                    ],
                    style={'width': '100%', 'overflow': 'hidden'}
                ),
                html.Div(
                    id='ec_server_4_div',
                    children=[

                        daq.Indicator(
                            id='ec_server_4',
                            label='Serwerownia 4',
                            labelPosition='right',
                            style={'width': dash_params['indicator_width'], 'float': 'left'}
                        ),
                        html.A(
                            'Link',
                            id='ec_server_4_link',
                            href='http://192.168.1.33',
                            title='Link',
                            style={'margin-left': 20}
                        )
                    ],
                    style={'width': '100%', 'overflow': 'hidden'}
                ),
                html.Button(
                    'Sprawdź',
                    id='btn_sprawdz'
                )
            ]
        ),
        html.Div(id='test')
    ]
)


@app_dash.callback(
    [
        Output('ec_server_1', 'value'),
        Output('ec_server_2', 'value'),
        Output('ec_server_3', 'value'),
        Output('ec_server_4', 'value')
    ],
    [Input('btn_sprawdz', 'n_clicks')]
)
def update_status(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    status = []
    for ec_ip in ec_list:
        status.append(ping(ec_ip, timeout=6, unit='ms'))
    return status


@server.route('/')
def index():
    return 'Hello Vuko'


if __name__ == '__main__':
    server.run()
