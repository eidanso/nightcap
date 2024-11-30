import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import os

# Initialize the Dash app with a dark theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
server = app.server

# Define the mocktails data
mocktails = [
    {
        "name": "Virgin Mojito Sparkle",
        "image": "virgin-mojito",
        "category": "Mocktail",
        "premium": True,
        "ingredients": [
            "Fresh Mint Leaves",
            "1 oz Fresh Lime Juice",
            "1 oz Simple Syrup",
            "Club Soda",
            "Crushed Ice",
            "Lime Wheels",
            "Mint Sprig for Garnish"
        ],
        "instructions": [
            "1. Muddle mint leaves with simple syrup in a glass",
            "2. Add fresh lime juice and fill glass with crushed ice",
            "3. Top with club soda and stir gently",
            "4. Garnish with lime wheels and mint sprig"
        ],
        "glassware": "Highball Glass",
        "description": "A refreshing alcohol-free version of the classic mojito with bright citrus and mint notes"
    },
    {
        "name": "Berry Hibiscus Fizz",
        "image": "berry-hibiscus",
        "category": "Mocktail",
        "premium": True,
        "ingredients": [
            "2 oz Hibiscus Tea (chilled)",
            "1 oz Mixed Berry Puree",
            "½ oz Fresh Lemon Juice",
            "½ oz Vanilla Syrup",
            "Fever-Tree Elderflower Tonic",
            "Fresh Berries for Garnish"
        ],
        "instructions": [
            "1. Combine hibiscus tea, berry puree, lemon juice, and vanilla syrup in a shaker",
            "2. Shake well with ice",
            "3. Strain into a glass filled with ice",
            "4. Top with elderflower tonic",
            "5. Garnish with fresh berries"
        ],
        "glassware": "Collins Glass",
        "description": "A sophisticated blend of floral hibiscus, sweet berries, and elegant elderflower"
    },
    {
        "name": "Spiced Apple Cider Punch",
        "image": "apple-cider",
        "category": "Mocktail",
        "premium": True,
        "ingredients": [
            "3 oz Fresh Apple Cider",
            "1 oz Cinnamon Syrup",
            "½ oz Fresh Lemon Juice",
            "Ginger Beer",
            "Cinnamon Stick",
            "Apple Slice for Garnish"
        ],
        "instructions": [
            "1. Combine apple cider, cinnamon syrup, and lemon juice in a shaker with ice",
            "2. Shake until well-chilled",
            "3. Strain into a glass filled with ice",
            "4. Top with ginger beer",
            "5. Garnish with cinnamon stick and apple slice"
        ],
        "glassware": "Rocks Glass",
        "description": "A warming blend of autumn flavors with a spicy ginger kick"
    },
    {
        "name": "Passion Fruit Paradise",
        "image": "passion-fruit",
        "category": "Mocktail",
        "premium": True,
        "ingredients": [
            "2 oz Passion Fruit Puree",
            "1 oz Coconut Cream",
            "½ oz Fresh Lime Juice",
            "½ oz Vanilla Syrup",
            "Club Soda",
            "Edible Flower for Garnish"
        ],
        "instructions": [
            "1. Combine passion fruit puree, coconut cream, lime juice, and vanilla syrup in a shaker",
            "2. Shake vigorously with ice",
            "3. Strain into a glass filled with crushed ice",
            "4. Top with club soda",
            "5. Garnish with edible flower"
        ],
        "glassware": "Hurricane Glass",
        "description": "A tropical paradise in a glass with sweet passion fruit and creamy coconut"
    }
]

# Define the cocktails data
cocktails = [
    {
        "name": "Thanksgiving Martini",
        "image": "/assets/thanksgiving-martini.jpg",
        "category": "Vodka",
        "premium": True,
        "ingredients": [
            "2½ oz GREY GOOSE® Vodka",
            "½ oz NOILLY PRAT® Dry Vermouth",
            "Orange and Star Anise Bitters (Optional)",
            "Clementine",
            "Star Anise"
        ],
        "instructions": [
            "1. In a mixing glass, add GREY GOOSE® Vodka, NOILLY PRAT® Dry Vermouth, and bitters; stir with a barspoon.",
            "2. Strain into a martini cocktail glass.",
            "3. Garnish with a clementine round and star anise."
        ],
        "glassware": "Martini Glass",
        "description": "A seasonal twist on the classic martini with warming star anise notes."
    },
    {
        "name": "Spicy Blushing Bride",
        "image": "lemon-drop",
        "category": "Ginger Magarita Mocktail",
        "premium": True,
        "ingredients": [
            "3 oz Ginger Beer (Gosling's)",
            "1 oz Fresh Lime Juice",
            "1 oz Simply Watermelon Juice",
            "½ oz Spicy Ginger Syrup",
            "½ Non-Alcoholic Triple Sec",
            "Q Mixer Hibiscus Ginger Beer - splash for color",
            "Garnish Candy & Lime wedge on a tootpick"
        ],
        "instructions": [
            "1. Fill glass about a quarter of the way with ice.",
            "2. Squeeze lime juice into the glass.",
            "3. Add ginger beer, triple sec, ginger syrup, and watermelon juice.",
            "4. Stir.",
            "5. Add a splash of the mixer for color (Do no stir so that the color can float)."
        ],
        "glassware": "Rocks Glass",
        "description": "Spicy ginger and fruity watermelon meet in this mocktail that refreshes the palette and warms the soul."
    },
    {
        "name": "Drunk in Love",
        "image": "cucumber-fizz",
        "category": "Vodka",
        "premium": True,
        "ingredients": [
            "1 oz Peach Syrup",
            "1 oz Fresh Lime Juice",
            "2 oz Tito's Vodka",
            "Jelapeno slices",
            "Garnish with Lime wedge on a glass"
        ],
        "instructions": [
            "1. In a cocktail shaker, mix all ingredients",
            "2. Shake vigorously and double strain",
            "3. Serve in a Martini glass with cubed ice and garnish lime wedge on a glass"
        ],
        "glassware": "Martini Glass",
        "description": "A refreshing blend sweet and heat."
    },
    {
        "name": "Lemon Drop",
        "image": "lemon-drop",
        "category": "Vodka",
        "premium": True,
        "ingredients": [
            "2 oz GREY GOOSE® Le Citron Flavored Vodka",
            "¾ oz Triple Sec",
            "¾ oz Fresh Lemon Juice",
            "½ oz Simple Syrup",
            "Sugar for rim",
            "Lemon Twist for garnish"
        ],
        "instructions": [
            "1. Rub a lemon half around the rim of a cocktail glass and roll the glass in sugar.",
            "2. Fill a cocktail shaker with ice, add all ingredients, and shake well.",
            "3. Double strain into a chilled cocktail glass.",
            "4. Garnish with a lemon twist."
        ],
        "glassware": "Cocktail Glass",
        "description": "A perfectly balanced sweet and sour cocktail."
    },
    {
        "name": "Cucumber Fizz",
        "image": "cucumber-fizz",
        "category": "Vodka",
        "premium": True,
        "ingredients": [
            "1½ oz GREY GOOSE® La Poire Flavored Vodka",
            "½ oz ST-GERMAIN® Elderflower Liqueur",
            "2 oz Juiced Cucumber",
            "½ oz Lemon Juice",
            "½ oz Simple Syrup",
            "Soda Water",
            "Mint, cucumber slices, and lemon zest for garnish"
        ],
        "instructions": [
            "1. In a cocktail shaker, mix all ingredients",
            "2. Shake vigorously and double strain",
            "3. Serve in a highball glass with cubed ice and garnish with mint, cucumber slices and lemon zest",
            "4. Top with lemonade or club soda"
        ],
        "glassware": "Highball Glass",
        "description": "A refreshing blend of cucumber and elderflower"
    },
    {
        "name": "Sexy Strawberry",
        "image": "/assets/sexy-strawberry.jpg",
        "category": "Vodka",
        "premium": True,
        "ingredients": [
            "1½ oz GREY GOOSE® Essences Strawberry & Lemongrass",
            "4½ oz Soda",
            "Fresh Strawberries",
            "Lemongrass",
            "Lemon Twist"
        ],
        "instructions": ["1. Fill a chilled glass with cubed ice and add GREY GOOSE® Essences Strawberry & Lemongrass",
                         "2. Top with soda water",
                         "3. Then simply garnish with lemongrass, fresh strawberry, and a lemon twist"
        ],
        "glassware": "Highball Glass",
        "description": "A light and fruity sparkling cocktail"
    },
    {
        "name": "Winter Espresso Martini",
        "image": "/assets/winter-expresso-martini.jpg",
        "category": "Vodka",
        "premium": True,
        "ingredients": [
            "2 oz GREY GOOSE® Vodka",
            "1 oz Fresh Espresso",
            "¾ oz Kahlúa",
            "¼ oz Cinnamon Syrup",
            "Chocolate Shavings",
            "Coffee Beans"
        ],
        "instructions": ["1. Combine all ingredients in a shaker with ice",
                         "2. Shake vigorously until well-chilled and frothy",
                         "3. Double strain into a chilled martini glass",
                         "4. Garnish with three coffee beans and chocolate shavings"
        ],
        "glassware": "Martini Glass",
        "description": "A warming twist on the classic espresso martini with hints of cinnamon"
    },
    {
        "name": "Frosted Maple Manhattan",
        "image": "/assets/frosted-maple-manhattan.jpg",
        "category": "Whiskey",
        "premium": True,
        "ingredients": [
            "2 oz Premium Bourbon",
            "1 oz Sweet Vermouth",
            "½ oz Pure Maple Syrup",
            "2 dashes Aromatic Bitters",
            "Orange Peel",
            "Candied Bacon"
        ],
        "instructions": ["1. In a mixing glass filled with ice, combine bourbon, vermouth, maple syrup, and bitters",
                        "2. Stir well until thoroughly chilled",
                        "3. Strain into a coupe glass",
                        "4. Garnish with orange peel and candied bacon"
        ],
        "glassware": "Coupe Glass",
        "description": "A warming cocktail with maple and bourbon notes"
    },
    {
        "name": "Emerald Knight",
        "image": "/assets/emerald-knight.jpg",
        "category": "Gin",
        "premium": True,
        "ingredients": [
            "2 oz Premium Gin",
            "1 oz Green Chartreuse",
            "¾ oz Lime Juice",
            "½ oz Simple Syrup",
            "Fresh Basil Leaves",
            "Lime Wheel"
        ],
        "instructions": ["1. Muddle basil leaves in a shaker",
                         "2. Add remaining ingredients and ice",
                         "3. Shake vigorously",
                         "4. Double strain into a coupe glass",
                         "5. Garnish with a floating lime wheel and basil leaf"
        ],
        "glassware": "Coupe Glass",
        "description": "Our signature cocktail featuring herbal notes and bright citrus"
    },
    {
        "name": "Golden Sunset",
        "image": "/assets/golden-sunset.jpg",
        "category": "Whiskey",
        "premium": True,
        "ingredients": [
            "2 oz Japanese Whisky",
            "½ oz Yuzu Juice",
            "½ oz Honey Syrup",
            "2 dashes Orange Bitters",
            "Ginger Beer",
            "Candied Ginger"
        ],
        "instructions": ["1. Combine whisky, yuzu juice, honey syrup, and bitters in a shaker with ice",
                         "2. Shake until well-chilled",
                         "3. Strain into a highball glass filled with ice",
                         "4. Top with ginger beer",
                         "5. Garnish with candied ginger"
        ],
        "glassware": "Highball Glass",
        "description": "An elegant fusion of Japanese whisky and citrus with a spicy ginger finish"
    }
]

# Define the wines data
wines = [
    {
        "name": "Château Margaux",
        "image": "margaux",
        "category": "Red Wine",
        "premium": True,
        "vintage": "2015",
        "region": "Bordeaux, France",
        "varietal": "Cabernet Sauvignon Blend",
        "description": "An exceptional vintage with perfect balance, showing notes of black fruits, violets, and subtle oak. The palate is pure elegance with silky tannins and remarkable length.",
        "tasting_notes": [
            "Blackcurrant",
            "Violet",
            "Cedar",
            "Tobacco",
            "Dark Chocolate"
        ],
        "pairing": [
            "Prime Rib",
            "Lamb Chops",
            "Aged Cheeses"
        ],
        "glass": "6 oz",
        "bottle": "750 ml"
    },
    {
        "name": "Dom Pérignon",
        "image": "dom-perignon",
        "category": "Champagne",
        "premium": True,
        "vintage": "2012",
        "region": "Champagne, France",
        "varietal": "Chardonnay & Pinot Noir",
        "description": "Luminous and sophisticated champagne with intense minerality. The nose reveals notes of white flowers, citrus, and stone fruits.",
        "tasting_notes": [
            "White Peach",
            "Citrus",
            "Brioche",
            "Mineral",
            "Almond"
        ],
        "pairing": [
            "Oysters",
            "Caviar",
            "Soft Cheeses"
        ],
        "glass": "5 oz",
        "bottle": "750 ml"
    },
    {
        "name": "Opus One",
        "image": "opus-one",
        "category": "Red Wine",
        "premium": True,
        "vintage": "2018",
        "region": "Napa Valley, USA",
        "varietal": "Cabernet Sauvignon Blend",
        "description": "A masterful blend showing the best of Napa Valley. Rich and complex with perfect structure and incredible aging potential.",
        "tasting_notes": [
            "Cassis",
            "Black Cherry",
            "Espresso",
            "Vanilla",
            "Herbs"
        ],
        "pairing": [
            "Filet Mignon",
            "Truffle Dishes",
            "Dark Chocolate"
        ],
        "glass": "6 oz",
        "bottle": "750 ml"
    },
    {
        "name": "Château Margaux",
        "image": "margaux",
        "category": "Red Wine",
        "premium": True,
        "vintage": "2015",
        "region": "Bordeaux, France",
        "varietal": "Cabernet Sauvignon Blend",
        "description": "An exceptional vintage with perfect balance, showing notes of black fruits, violets, and subtle oak. The palate is pure elegance with silky tannins and remarkable length.",
        "tasting_notes": [
            "Blackcurrant",
            "Violet",
            "Cedar",
            "Tobacco",
            "Dark Chocolate"
        ],
        "pairing": [
            "Prime Rib",
            "Lamb Chops",
            "Aged Cheeses"
        ],
        "glass": "6 oz",
        "bottle": "750 ml"
    },
    {
        "name": "Dom Pérignon",
        "image": "dom-perignon",
        "category": "Champagne",
        "premium": True,
        "vintage": "2012",
        "region": "Champagne, France",
        "varietal": "Chardonnay & Pinot Noir",
        "description": "Luminous and sophisticated champagne with intense minerality. The nose reveals notes of white flowers, citrus, and stone fruits.",
        "tasting_notes": [
            "White Peach",
            "Citrus",
            "Brioche",
            "Mineral",
            "Almond"
        ],
        "pairing": [
            "Oysters",
            "Caviar",
            "Soft Cheeses"
        ],
        "glass": "5 oz",
        "bottle": "750 ml"
    },
    {
        "name": "Opus One",
        "image": "opus-one",
        "category": "Red Wine",
        "premium": True,
        "vintage": "2018",
        "region": "Napa Valley, USA",
        "varietal": "Cabernet Sauvignon Blend",
        "description": "A masterful blend showing the best of Napa Valley. Rich and complex with perfect structure and incredible aging potential.",
        "tasting_notes": [
            "Cassis",
            "Black Cherry",
            "Espresso",
            "Vanilla",
            "Herbs"
        ],
        "pairing": [
            "Filet Mignon",
            "Truffle Dishes",
            "Dark Chocolate"
        ],
        "glass": "6 oz",
        "bottle": "750 ml"
    }
]


# Custom styles
styles = {
    'page': {
        'backgroundColor': 'black',
        'color': '#00FF9D',
        'minHeight': '100vh',
        'padding': '20px'
    },
    'container': {
        'maxWidth': '1200px',
        'margin': '0 auto'
    },
    'title': {
        'textAlign': 'center',
        'fontSize': '48px',
        'fontWeight': 'bold',
        'marginBottom': '30px',
        'color': '#00FF9D'
    },
    'welcome': {
        'textAlign': 'center',
        'whiteSpace': 'pre-line',
        'marginBottom': '30px',
        'color': '#00FF9D'
    },
    'menu_guide': {
        'whiteSpace': 'pre-line',
        'marginBottom': '40px',
        'color': '#00FF9D'
    },
    'card': {
        'backgroundColor': 'black',
        'border': '1px solid #00FF9D',
        'borderRadius': '8px',
        'marginBottom': '20px',
        'padding': '20px',
        'color': '#00FF9D'
    },
    'image': {
        'width': '100%',
        'height': '300px',
        'objectFit': 'cover',
        'borderRadius': '8px',
        'marginBottom': '20px'
    },
    'dropdown': {
        'backgroundColor': 'black',
        'color': '#00FF9D',
        'border': '1px solid #00FF9D',
        'marginBottom': '20px'
    }
}

welcome_message = """✨ Welcome to Château Danso ✨

Step into our cozy corner of mixology magic! We're thrilled to have you join us for an evening of crafted cocktails, mocktails, and fine wines. Each drink has been carefully selected and perfected to ensure your experience is nothing short of extraordinary.

Sit back, relax, and let us guide you through our carefully curated selection of libations.

With love,
The Dansos 🍸"""

menu_layout = """📖 Menu Guide 📖

Our menu features signature cocktails across different spirit categories:

🍸 Premium Vodka Collection
   Expertly crafted vodka-based cocktails featuring GREY GOOSE®

🥃 Whiskey Classics
   Time-honored whiskey cocktails with a modern twist

🌿 Gin Botanicals
   Refreshing gin-based drinks celebrating natural flavors

✨ Each drink marked with a star (★) represents our premium selections.

Cocktails can be customized to your preference - just ask!"""

# Add a mocktails guide
mocktails_guide = """📖 Mocktail Selection Guide 📖

Our alcohol-free creations are crafted with the same care and creativity as our cocktails:

🌿 Fresh & Herbal
   Refreshing combinations with garden-fresh herbs

🍓 Fruit Forward
   Bold and vibrant fruit-based beverages

✨ Each drink marked with a star (★) represents our premium selections.

All mocktails can be customized to your taste preferences!"""


def get_image_path(image_name):
    """Helper function to handle image paths"""
    if not image_name.startswith('/assets/'):
        image_name = f"/assets/{image_name}.jpg"
    return image_name

def create_drink_card(drink):
    image_path = get_image_path(drink['image'])
    return dbc.Card(
        [
            dbc.CardHeader(
                [
                    html.H3(
                        [
                            drink['name'],
                            html.Span(" ★ Premium Selection", className="ms-2", style={'fontSize': '14px', 'fontStyle': 'italic'}) if drink['premium'] else None
                        ],
                        className="card-title"
                    )
                ],
                style={'backgroundColor': 'black', 'color': '#00FF9D', 'borderBottom': '1px solid #00FF9D'}
            ),
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Img(
                                    src=image_path,
                                    style=styles['image'],
                                    alt=f"{drink['name']} cocktail"
                                ),
                                md=6
                            ),
                            dbc.Col(
                                [
                                    html.P(drink['description'], className="mb-3"),
                                    html.Div(
                                        [
                                            html.H4("Ingredients", className="mb-2"),
                                            html.Ul([html.Li(ingredient) for ingredient in drink['ingredients']], className="mb-3")
                                        ]
                                    ),
                                    html.Div(
                                        [
                                            html.H4("Instructions", className="mb-2"),
                                            html.Ul([html.Li(step) for step in drink['instructions']])
                                        ]
                                    )
                                ],
                                md=6
                            )
                        ]
                    )
                ],
                style={'backgroundColor': 'black', 'color': '#00FF9D'}
            )
        ],
        className="mb-4",
        style=styles['card']
    )

def create_wine_card(wine):
    image_path = get_image_path(wine['image'])
    return dbc.Card(
        [
            dbc.CardHeader(
                [
                    html.H3(
                        [
                            wine['name'],
                            html.Span(" ★ Premium Selection", className="ms-2", style={'fontSize': '14px', 'fontStyle': 'italic'}) if wine['premium'] else None
                        ],
                        className="card-title"
                    )
                ],
                style={'backgroundColor': 'black', 'color': '#00FF9D', 'borderBottom': '1px solid #00FF9D'}
            ),
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Img(
                                    src=image_path,
                                    style=styles['image'],
                                    alt=f"{wine['name']} wine"
                                ),
                                md=6
                            ),
                            dbc.Col(
                                [
                                    html.P(wine['description'], className="mb-3"),
                                    html.Div(
                                        [
                                            html.H4("Details", className="mb-2"),
                                            html.P(f"Vintage: {wine['vintage']}", className="mb-1"),
                                            html.P(f"Region: {wine['region']}", className="mb-1"),
                                            html.P(f"Varietal: {wine['varietal']}", className="mb-1"),
                                        ],
                                        className="mb-3"
                                    ),
                                    html.Div(
                                        [
                                            html.H4("Tasting Notes", className="mb-2"),
                                            html.Ul([html.Li(note) for note in wine['tasting_notes']], className="mb-3")
                                        ]
                                    ),
                                    html.Div(
                                        [
                                            html.H4("Food Pairing", className="mb-2"),
                                            html.Ul([html.Li(pairing) for pairing in wine['pairing']])
                                        ]
                                    )
                                ],
                                md=6
                            )
                        ]
                    )
                ],
                style={'backgroundColor': 'black', 'color': '#00FF9D'}
            )
        ],
        className="mb-4",
        style=styles['card']
    )


def create_mocktail_card(mocktail):
    """Helper function to create mocktail cards"""
    image_path = get_image_path(mocktail['image'])
    return dbc.Card(
        [
            dbc.CardHeader(
                [
                    html.H3(
                        [
                            mocktail['name'],
                            html.Span(" ★ Premium Selection", className="ms-2", style={'fontSize': '14px', 'fontStyle': 'italic'}) if mocktail['premium'] else None
                        ],
                        className="card-title"
                    )
                ],
                style={'backgroundColor': 'black', 'color': '#00FF9D', 'borderBottom': '1px solid #00FF9D'}
            ),
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Img(
                                    src=image_path,
                                    style=styles['image'],
                                    alt=f"{mocktail['name']} mocktail"
                                ),
                                md=6
                            ),
                            dbc.Col(
                                [
                                    html.P(mocktail['description'], className="mb-3"),
                                    html.Div(
                                        [
                                            html.H4("Ingredients", className="mb-2"),
                                            html.Ul([html.Li(ingredient) for ingredient in mocktail['ingredients']], className="mb-3")
                                        ]
                                    ),
                                    html.Div(
                                        [
                                            html.H4("Instructions", className="mb-2"),
                                            html.Ul([html.Li(step) for step in mocktail['instructions']])
                                        ]
                                    )
                                ],
                                md=6
                            )
                        ]
                    )
                ],
                style={'backgroundColor': 'black', 'color': '#00FF9D'}
            )
        ],
        className="mb-4",
        style=styles['card']
    )

# App layout
app.layout = html.Div(
    [
        html.Div(
            [
                html.H1("The Night Cap", style=styles['title']),
                html.Div(welcome_message, style=styles['welcome']),
                
                # Updated menu selection dropdown
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Label("Select Menu Type:", style={'color': '#00FF9D', 'marginBottom': '10px'}),
                                dcc.Dropdown(
                                    id='menu-type-dropdown',
                                    options=[
                                        {'label': 'Cocktails', 'value': 'cocktails'},
                                        {'label': 'Mocktails', 'value': 'mocktails'},
                                        {'label': 'Wines', 'value': 'wines'}
                                    ],
                                    value='cocktails',
                                    style=styles['dropdown']
                                )
                            ],
                            width=6,
                            className="mb-4"
                        )
                    ],
                    justify="center"
                ),
                
                # Dynamic menu guide
                html.Div(id='dynamic-menu-guide', style=styles['menu_guide']),
                
                # Dynamic content area
                html.Div(id='dynamic-content', style={'marginTop': '40px'})
            ],
            style=styles['container']
        )
    ],
    style=styles['page']
)

# Updated callback for menu guide
@app.callback(
    Output('dynamic-menu-guide', 'children'),
    [Input('menu-type-dropdown', 'value')]
)
def update_menu_guide(selected_menu):
    if selected_menu == 'cocktails':
        return menu_layout
    elif selected_menu == 'mocktails':
        return mocktails_guide
    else:
        return """📖 Wine Selection Guide 📖

Our carefully curated wine list features exceptional selections from renowned regions:

🍷 Red Wines
   Bold and elegant selections from premier vineyards

🥂 Champagne & Sparkling
   Prestigious champagnes and sparkling wines

✨ Each wine marked with a star (★) represents our premium selections.

Our sommelier is available to help with your selection and food pairings."""

# Updated callback for content
@app.callback(
    Output('dynamic-content', 'children'),
    [Input('menu-type-dropdown', 'value')]
)
def update_content(selected_menu):
    if selected_menu == 'cocktails':
        return [create_drink_card(drink) for drink in cocktails]
    elif selected_menu == 'mocktails':
        return [create_mocktail_card(mocktail) for mocktail in mocktails]
    else:
        return [create_wine_card(wine) for wine in wines]

if __name__ == '__main__':
    app.run_server(debug=True, host='192.168.12.105', port=8050)