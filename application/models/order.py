from application import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurantId = db.Column(db.Integer, db.ForeignKey('restaurant.id'),
                             nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())
    name = db.Column(db.String(144), nullable=False)
    address = db.Column(db.String(144), nullable=False)
    phone = db.Column(db.String(144), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    items = db.relationship('OrderMenuItem', backref='order', lazy=True)

    def __init__(self, restaurantId, name, address, phone, price):
        self.restaurantId = restaurantId
        self.name = name
        self.address = address
        self.phone = phone
        self.price = price