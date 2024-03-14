from flask import Flask, render_template, request

app = Flask(__name__)

# Sample product data
products = {
    'mens': [
        {'name': 'Men\'s Shirt', 'price': 25.99},
        {'name': 'Men\'s Jeans', 'price': 39.99},
        {'name': 'Men\'s Shirt', 'price': 25.99},
        {'name': 'Men\'s Jeans', 'price': 39.99},
        {'name': 'Men\'s Shirt', 'price': 25.99},
        {'name': 'Men\'s Jeans', 'price': 39.99},
        # Add more items...
    ],
    'womens': [
        {'name': 'Women\'s Dress', 'price': 49.99},
        {'name': 'Women\'s Shoes', 'price': 29.99},
        {'name': 'Women\'s Dress', 'price': 49.99},
        {'name': 'Women\'s Shoes', 'price': 29.99},
        {'name': 'Women\'s Dress', 'price': 49.99},
        {'name': 'Women\'s Shoes', 'price': 29.99},
        # Add more items...
    ],
    'kids': [
        {'name': 'Kid\'s T-shirt', 'price': 19.99},
        {'name': 'Kid\'s Shorts', 'price': 14.99},
        {'name': 'Kid\'s T-shirt', 'price': 19.99},
        {'name': 'Kid\'s Shorts', 'price': 14.99},
        {'name': 'Kid\'s T-shirt', 'price': 19.99},
        {'name': 'Kid\'s Shorts', 'price': 14.99},
        # Add more items...
    ]
}

# Cart data
cart = []


@app.route('/')
def index():
    return render_template('index.html', products=products)


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    item = request.form['item']
    category = request.form['category']
    cart.append(products[category][int(item)])
    # return render_template('cart.html', cart=cart, total=get_cart_total(cart))
    return 'Item added to cart successfully!'


@app.route('/cart')
def view_cart():
    return render_template('cart.html', cart=cart, total=get_cart_total(cart))


def get_cart_total(cart):
    total = sum(item['price'] for item in cart)
    return total


if __name__ == '__main__':
    app.run(debug=True)
