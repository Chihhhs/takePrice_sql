from flask import Flask, render_template, jsonify, request
from model import db, Product, Store, Price
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pricing.db'
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/products')
def get_products():
    products = Product.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'category': p.category} for p in products])

@app.route('/api/prices/<int:product_id>')
def get_prices(product_id):
    prices = Price.query.filter_by(product_id=product_id).all()
    return jsonify([{
        'store': p.store.name,
        'price': p.price,
        'updated_at': p.updated_at.strftime('%Y-%m-%d %H:%M:%S')
    } for p in prices])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
