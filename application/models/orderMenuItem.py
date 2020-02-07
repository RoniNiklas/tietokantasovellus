from application import db

class OrderMenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    itemId = db.Column(db.Integer, db.ForeignKey(
        'menu_item.id'), nullable=False)
    orderId = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)

    def __init__(self, orderId, itemId):
        self.orderId = orderId
        self.itemId = itemId