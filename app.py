from flask import Flask, render_template

app = Flask(__name__)

food_items = [
    {
        "name": "Cheese Burger",
        "price": "$8.99",
        "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd"
    },
    {
        "name": "Italian Pizza",
        "price": "$12.50",
        "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591"
    },
    {
        "name": "Pasta Alfredo",
        "price": "$10.25",
        "image": "https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9"
    },
    {
        "name": "Fresh Salad",
        "price": "$6.75",
        "image": "https://images.unsplash.com/photo-1546793665-c74683f339c1"
    },
    {
        "name": "Chocolate Dessert",
        "price": "$5.99",
        "image": "https://images.unsplash.com/photo-1563805042-7684c019e1cb"
    },
    {
        "name": "Cold Coffee",
        "price": "$4.50",
        "image": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085"
    }
]

@app.route('/')
def home():
    return render_template('index.html', foods=food_items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
