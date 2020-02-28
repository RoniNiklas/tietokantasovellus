from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, validators


class SignUpForm(FlaskForm):
    name = StringField("Nickname", validators=[
        validators.DataRequired(),
        validators.Length(min=3, max=144, message=(
            u"Your name has to be between 3 and 144 characters"))
    ])
    newusername = StringField("Username", validators=[
        validators.DataRequired(),
        validators.Length(min=3, max=144, message=(
            u"Your username has to be between 3 and 144 characters"))
    ])
    newpassword = PasswordField("Password", validators=[
        validators.DataRequired(),
        validators.Length(min=3, max=60, message=(
            u"Password has to be between 3 and 60 characters"))
    ])
    restaurantname = TextAreaField("Restaurant's name", validators=[
        validators.DataRequired(),
        validators.Length(min=3, max=144, message=(
            u"The name has to be between 3 and 144 characters"))
    ])
    restaurantdescription = TextAreaField(
        "Description of the restaurant", validators=[
        validators.DataRequired(),
        validators.Length(min=3, max=144, message=(
            u"The description has to be between 3 and 144 characters"))
    ])
    restaurantaddress = TextAreaField(
        "The address of the restaurant", validators=[
        validators.DataRequired(),
        validators.Length(min=3, max=144, message=(
            u"The address has to be between 3 and 144 characters"))
    ])
    restaurantphone = TextAreaField("Phone number of the restaurant", validators=[
        validators.DataRequired(),
        validators.Length(min=3, max=144, message=(
            u"The phone number has to be between 3 and 144 characters"))
    ])

    class Meta:
        csrf = False
