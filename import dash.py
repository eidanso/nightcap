import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import qrcode
import base64
from io import BytesIO
import socket

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
server = app.server

# Function to get the local IP
def get_local_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

# Function to generate a QR code for a given URL
def generate_qr(menu_type):
    local_ip = get_local_ip()
    url = f"http://{local_ip}:8050/{menu_type}"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    qr_image = qr.make_image(fill_color="#00FF9D", back_color="black")
    buffered = BytesIO()
    qr_image.save(buffered, format="PNG")
    qr_base64 = base64.b64encode(buffered.getvalue()).decode()
    return f'data:image/png;base64,{qr_base64}'

# Define styles
styles = {
    'title': {'color': '#00FF9D', 'textAlign': 'center', 'marginTop': '20px'},
    'section_title': {'color': '#FFFFFF', 'textAlign': 'center', 'marginTop': '20px'},
    'menu_item': {'color': '#FFFFFF', 'margin': '10px'},
    'container': {'padding': '20px'},
    'page': {'backgroundColor': '#121212', 'height': '100vh'}
}

# Menu data
menus = {
    "cocktail": ["Mojito", "Martini", "Margarita"],
    "mocktail": ["Virgin Mojito", "Lemon Cooler", "Berry Delight"],
    "wine": ["Merlot", "Chardonnay", "Cabernet Sauvignon"]
}

# Layout for each menu
def menu_layout(menu_type, items):
    return html.Div([
        html.H2(f"{menu_type.capitalize()} Menu", style=styles['section_title']),
        html.Ul([html.Li(item, style=styles['menu_item']) for item in items], style={'textAlign': 'center'}),
        html.Img(src=generate_qr(menu_type), style={'margin': '20px auto', 'display': 'block', 'maxWidth': '200px'}),
        html.P(f"Scan this QR code to view the {menu_type} menu", 
               style={'color': '#00FF9D', 'textAlign': 'center', 'marginTop': '20px'})
    ], style={'marginTop': '40px', 'marginBottom': '40px'})

# Main layout
app.layout = html.Div([
    html.H1("The Night Cap", style=styles['title']),
    dcc.Tabs(id="menu-tabs", value='cocktail', children=[
        dcc.Tab(label='Cocktail Menu', value='cocktail', style={'color': '#FFFFFF'}),
        dcc.Tab(label='Mocktail Menu', value='mocktail', style={'color': '#FFFFFF'}),
        dcc.Tab(label='Wine Menu', value='wine', style={'color': '#FFFFFF'}),
    ], style={'marginTop': '20px'}),
    html.Div(id='menu-content')
], style=styles['page'])

# Callback to update content based on tab
@app.callback(
    Output('menu-content', 'children'),
    [Input('menu-tabs', 'value')]
)
def update_menu(tab):
    return menu_layout(tab, menus[tab])

# Run the app
if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)
