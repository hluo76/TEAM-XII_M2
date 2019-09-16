from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, DateField, IntegerField, DateTimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired
type_choices = [('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard'), ('Hell level', 'Hell level')]
class LoadForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    type = SelectField('Type', choices=type_choices)
    search = SubmitField('Search')
    
