from app import db
from app import app
from model import Product, Store, Price
from datetime import datetime

def insert_test_data():
    db.create_all()

    # 插入產品數據
    product1 = Product(name='iPhone 13', description='Apple smartphone', category='Electronics')
    product2 = Product(name='Samsung Galaxy S21', description='Samsung smartphone', category='Electronics')
    product3 = Product(name='Dell XPS 13', description='Dell laptop', category='Computers')

    # 插入商店數據
    store1 = Store(name='Best Buy', address='123 Main St', contact='(555) 123-4567')
    store2 = Store(name='Amazon', address='Online', contact='support@amazon.com')
    store3 = Store(name='Walmart', address='456 Elm St', contact='(555) 987-6543')

    db.session.add_all([product1, product2, product3, store1, store2, store3])
    db.session.commit()

    # 插入價格數據
    price1 = Price(product_id=product1.id, store_id=store1.id, price=799.99, updated_at=datetime.now())
    price2 = Price(product_id=product1.id, store_id=store2.id, price=789.99, updated_at=datetime.now())
    price3 = Price(product_id=product1.id, store_id=store3.id, price=799.00, updated_at=datetime.now())

    price4 = Price(product_id=product2.id, store_id=store1.id, price=699.99, updated_at=datetime.now())
    price5 = Price(product_id=product2.id, store_id=store2.id, price=689.99, updated_at=datetime.now())
    price6 = Price(product_id=product2.id, store_id=store3.id, price=695.00, updated_at=datetime.now())

    price7 = Price(product_id=product3.id, store_id=store1.id, price=999.99, updated_at=datetime.now())
    price8 = Price(product_id=product3.id, store_id=store2.id, price=979.99, updated_at=datetime.now())
    price9 = Price(product_id=product3.id, store_id=store3.id, price=999.00, updated_at=datetime.now())

    db.session.add_all([price1, price2, price3, price4, price5, price6, price7, price8, price9])
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        insert_test_data()
