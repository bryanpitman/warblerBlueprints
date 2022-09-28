from flask_wtf import FlaskForm
from wtforms import  TextAreaField
from wtforms.validators import DataRequired


class CSRFProtection(FlaskForm):
    """CSRFProtection form, intentionally left blank."""


class MessageForm(FlaskForm):
    """Form for adding/editing messages."""

    text = TextAreaField('text', validators=[DataRequired()])


