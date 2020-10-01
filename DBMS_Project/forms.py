from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField
from wtforms.validators import InputRequired

class EditCriminalRecord(FlaskForm):
    Name = StringField("Criminal's Name", validators = [InputRequired()])
    gender = StringField("Criminal's Gender", validators = [InputRequired()])
    crime = StringField("Criminal's crime", validators = [InputRequired()])
    inJail = StringField("Criminal's status", validators = [InputRequired()])
    country = StringField("Criminal's country", validators = [InputRequired()])
    submit = SubmitField("Edit Criminal")

class AddCriminal(FlaskForm):
    Name = StringField("Criminal's Name", validators=[InputRequired()])
    gender = StringField("Criminal's Gender", validators=[InputRequired()])
    photo = StringField("Criminal's Photo",validators=[InputRequired()])
    crime = StringField("Criminal's crime", validators=[InputRequired()])
    inJail = StringField("Criminal's status", validators=[InputRequired()])
    country = StringField("Criminal's country", validators=[InputRequired()])
    submit = SubmitField("Add Criminal")