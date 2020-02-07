from application import db


class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurantId = db.Column(db.Integer, db.ForeignKey('restaurant.id'),
                             nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=False)
    price = db.Column(db.Float, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    ##photo = db.Column(db.LargeBinary, nullable=False)
    orders = db.relationship('OrderMenuItem', backref='menuItem', lazy=True)

    def __init__(self, restaurantId, name, description, price, active):
        self.restaurantId = restaurantId
        self.name = name
        self.description = description
        self.price = price
        self.active = active