from application import db


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=False)
    address = db.Column(db.String(144), nullable=False)
    phone = db.Column(db.String(144), nullable=False)
    menu = db.relationship('MenuItem', backref='restaurant',cascade='delete', lazy=True)
    orders = db.relationship('Order', backref='restaurant', cascade='delete', lazy=True)
    manager = db.relationship('User', backref='restaurant', cascade='delete', lazy=True)

    def __init__(self, name, description, address, phone):
        self.name = name
        self.description = description
        self.address = address
        self.phone = phone
        self.menu = []