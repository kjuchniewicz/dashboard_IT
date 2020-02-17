from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
from flask import Flask

server = Flask(__name__)
app_dash = Dash(__name__, server=server, url_base_pathname='/dashboard/')
app_dash.layout = html.Div(
    children=[
        html.H1(children='Dashboard')
    ]
)


@server.route('/')
def index():
    return 'Hello Vuko'


if __name__ == '__main__':
    server.run()
