import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import os

class CocktailMenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("The Night Cap")
        self.root.geometry("1024x768")
        
        # Set color scheme
        self.style = ttk.Style()
        self.style.configure("Custom.TFrame", background="#000000")
        self.style.configure("Custom.TLabel", 
                           background="#000000", 
                           foreground="#00FF9D")
        self.style.configure("Custom.TLabelframe", 
                           background="#000000", 
                           foreground="#00FF9D")
        self.style.configure("Custom.TLabelframe.Label", 
                           background="#000000", 
                           foreground="#00FF9D",
                           font=("Helvetica", 12, "bold"))
        
        # Welcome message and menu layout
        self.welcome_message = """
✨ Welcome to Casa de Danso ✨

Step into our cozy corner of mixology magic! We're thrilled to have you join us for an evening of crafted cocktails and warm hospitality. Each drink has been carefully selected and perfected to ensure your experience is nothing short of extraordinary.

Sit back, relax, and let us guide you through our carefully curated selection of libations.

With love,
The Dansos 🍸
"""

        self.menu_layout = """
📖 Menu Guide 📖

Our menu features signature cocktails across different spirit categories:

🍸 Premium Vodka Collection
   Expertly crafted vodka-based cocktails featuring GREY GOOSE®

🥃 Whiskey Classics
   Time-honored whiskey cocktails with a modern twist

🌿 Gin Botanicals
   Refreshing gin-based drinks celebrating natural flavors

✨ Each drink marked with a star (★) represents our premium selections

Cocktails can be customized to your preference - just ask! 
"""
        
        # Define cocktails data
        self.cocktails = [
            {
                "name": "Thanksgiving Martini",
                "category": "Vodka",
                "premium": True,
                "ingredients": [
                    "2½ oz GREY GOOSE® Vodka",
                    "½ oz NOILLY PRAT® Dry Vermouth",
                    "Orange and Star Anise Bitters (Optional)",
                    "Clementine",
                    "Star Anise"
                ],
                "instructions": "1. In a mixing glass, add GREY GOOSE® Vodka, NOILLY PRAT® Dry Vermouth, and bitters; stir with a barspoon\n2. Strain into a martini cocktail glass\n3. Garnish with a clementine round and star anise",
                "glassware": "Martini Glass",
                "description": "A seasonal twist on the classic martini with warming star anise notes"
            },
            {
                "name": "Lemon Drop",
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
                "instructions": "1. Rub lemon half around rim of cocktail glass and roll glass in sugar\n2. Fill a cocktail shaker with ice, add all ingredients and shake well\n3. Double strain into a chilled cocktail glass\n4. Garnish with a lemon twist",
                "glassware": "Cocktail Glass",
                "description": "A perfectly balanced sweet and sour cocktail"
            },
            {
                "name": "Cucumber Fizz",
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
                "instructions": "1. In a cocktail shaker, mix all ingredients\n2. Shake vigorously and double strain\n3. Serve in a highball glass with cubed ice and garnish with mint, cucumber slices and lemon zest\n4. Top with lemonade or club soda",
                "glassware": "Highball Glass",
                "description": "A refreshing blend of cucumber and elderflower"
            },
            {
                "name": "Sexy Strawberry",
                "category": "Vodka",
                "premium": True,
                "ingredients": [
                    "1½ oz GREY GOOSE® Essences Strawberry & Lemongrass",
                    "4½ oz Soda",
                    "Fresh Strawberries",
                    "Lemongrass",
                    "Lemon Twist"
                ],
                "instructions": "1. Fill a chilled glass with cubed ice and add GREY GOOSE® Essences Strawberry & Lemongrass\n2. Top with soda water\n3. Then simply garnish with lemongrass, fresh strawberry, and a lemon twist",
                "glassware": "Highball Glass",
                "description": "A light and fruity sparkling cocktail"
            },
            {
                "name": "Winter Espresso Martini",
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
                "instructions": "1. Combine all ingredients in a shaker with ice\n2. Shake vigorously until well-chilled and frothy\n3. Double strain into a chilled martini glass\n4. Garnish with three coffee beans and chocolate shavings",
                "glassware": "Martini Glass",
                "description": "A warming twist on the classic espresso martini with hints of cinnamon"
            },
            {
                "name": "Frosted Maple Manhattan",
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
                "instructions": "1. In a mixing glass filled with ice, combine bourbon, vermouth, maple syrup, and bitters\n2. Stir well until thoroughly chilled\n3. Strain into a coupe glass\n4. Garnish with orange peel and candied bacon",
                "glassware": "Coupe Glass",
                "description": "A warming cocktail with maple and bourbon notes"
            },
            {
                "name": "Emerald Knight",
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
                "instructions": "1. Muddle basil leaves in a shaker\n2. Add remaining ingredients and ice\n3. Shake vigorously\n4. Double strain into a coupe glass\n5. Garnish with a floating lime wheel and basil leaf",
                "glassware": "Coupe Glass",
                "description": "Our signature cocktail featuring herbal notes and bright citrus"
            },
            {
                "name": "Golden Sunset",
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
                "instructions": "1. Combine whisky, yuzu juice, honey syrup, and bitters in a shaker with ice\n2. Shake until well-chilled\n3. Strain into a highball glass filled with ice\n4. Top with ginger beer\n5. Garnish with candied ginger",
                "glassware": "Highball Glass",
                "description": "An elegant fusion of Japanese whisky and citrus with a spicy ginger finish"
            }
        ]
        
        self.setup_ui()
        
    def setup_ui(self):
        # Create main scrollable canvas
        self.canvas = tk.Canvas(self.root, bg='black')
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas, style="Custom.TFrame")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Title and Welcome Message
        title_frame = ttk.Frame(self.scrollable_frame, style="Custom.TFrame")
        title_frame.pack(pady=20, fill="x")
        
        title = ttk.Label(title_frame, 
                         text="The Night Cap",
                         font=("Helvetica", 36, "bold"),
                         style="Custom.TLabel")
        title.pack()

        # Welcome message
        welcome_label = ttk.Label(self.scrollable_frame,
                                text=self.welcome_message,
                                wraplength=800,
                                justify="center",
                                style="Custom.TLabel",
                                font=("Helvetica", 12))
        welcome_label.pack(pady=20)

        # Menu Layout
        menu_layout_label = ttk.Label(self.scrollable_frame,
                                    text=self.menu_layout,
                                    wraplength=800,
                                    justify="left",
                                    style="Custom.TLabel",
                                    font=("Helvetica", 12))
        menu_layout_label.pack(pady=20)

        # Create drinks display
        for drink in self.cocktails:
            self.create_drink_card(drink)

        # Pack canvas and scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def create_drink_card(self, drink):
        # Card creation code remains the same as in previous version
        card = ttk.LabelFrame(self.scrollable_frame,
                            text=drink['name'],
                            style="Custom.TLabelframe")
        card.pack(pady=10, padx=20, fill="x")

        content = ttk.Frame(card, style="Custom.TFrame")
        content.pack(padx=10, pady=10, fill="x")

        # Add placeholder image
        img_label = ttk.Label(content, style="Custom.TLabel")
        img_label.image = ImageTk.PhotoImage(Image.new('RGB', (200, 200), color='#1a1a1a'))
        img_label.configure(image=img_label.image)
        img_label.pack(side="left", padx=10)

        info_frame = ttk.Frame(content, style="Custom.TFrame")
        info_frame.pack(side="left", fill="x", expand=True, padx=10)

        if drink['premium']:
            premium_label = ttk.Label(info_frame,
                                    text="★ Premium Selection",
                                    style="Custom.TLabel",
                                    font=("Helvetica", 10, "italic"))
            premium_label.pack(anchor="w")

        desc_label = ttk.Label(info_frame,
                             text=drink['description'],
                             wraplength=400,
                             style="Custom.TLabel")
        desc_label.pack(anchor="w", pady=5)

        ing_frame = ttk.LabelFrame(info_frame,
                                 text="Ingredients",
                                 style="Custom.TLabelframe")
        ing_frame.pack(fill="x", pady=5)

        for ingredient in drink['ingredients']:
            ing_label = ttk.Label(ing_frame,
                                text=f"• {ingredient}",
                                style="Custom.TLabel")
            ing_label.pack(anchor="w")

        inst_frame = ttk.LabelFrame(info_frame,
                                  text="Instructions",
                                  style="Custom.TLabelframe")
        inst_frame.pack(fill="x", pady=5)

        inst_label = ttk.Label(inst_frame,
                             text=drink['instructions'],
                             wraplength=400,
                             style="Custom.TLabel")
        inst_label.pack(anchor="w")

def main():
    root = tk.Tk()
    root.configure(bg='black')
    app = CocktailMenuApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()