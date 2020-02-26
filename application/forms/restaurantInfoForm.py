from flask_wtf import FlaskForm
from wtforms import TextAreaField
  
class restaurantInfoForm(FlaskForm):
    name = TextAreaField("Restaurant's name")
    description = TextAreaField("Description of the restaurant")
    address = TextAreaField("The address of the restaurant")
    phone = TextAreaField("Phone number of the restaurant")

    class Meta:
        csrf = False