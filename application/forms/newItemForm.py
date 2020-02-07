from flask_wtf import FlaskForm
from wtforms import TextAreaField, DecimalField, validators
from decimal import ROUND_HALF_UP
import decimal


class BetterDecimalField(DecimalField):
    """
    Magically copied from stackoverflow:
    https://stackoverflow.com/questions/27781926/decimal-field-rounding-in-wtforms
    """

    def __init__(self, label=None, validators=None, places=2, rounding=None,
                 round_always=False, **kwargs):
        super(BetterDecimalField, self).__init__(
            label=label, validators=validators, places=places, rounding=rounding, **kwargs)
        self.round_always = round_always

    def process_formdata(self, valuelist):
        if valuelist:
            try:
                self.data = decimal.Decimal(valuelist[0])
                if self.round_always and hasattr(self.data, 'quantize'):
                    exp = decimal.Decimal('.1') ** self.places
                    if self.rounding is None:
                        quantized = self.data.quantize(exp)
                    else:
                        quantized = self.data.quantize(
                            exp, rounding=self.rounding)
                    self.data = quantized
            except (decimal.InvalidOperation, ValueError):
                self.data = None
                raise ValueError(self.gettext('Not a valid decimal value'))


class NewItemForm (FlaskForm):
    name = TextAreaField("Item name", validators=[
        validators.DataRequired(),
        validators.Length(min=3, max=144, message=(u"Name has to be between 3 and 144 characters"))])
    description = TextAreaField(
        "Item description", validators=[
            validators.DataRequired(),
            validators.Length(min=3, max=144, message=(
                u"Name has to be between 3 and 144 characters"))
        ])
    price = BetterDecimalField(round_always=True, validators=[
        validators.DataRequired()])

    class Meta:
        csrf = False
