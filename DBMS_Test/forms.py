from flask_wtf import FlaskForm
from wtforms import StringField,FileField, SubmitField
from wtforms.validators import InputRequired

class EditCriminalRecord(FlaskForm):
    Name = StringField("Criminal's Name", validators = [InputRequired()])
    gender = StringField("Criminal's Gender", validators = [InputRequired()])
    img = FileField("Criminal's Img")
    crime = StringField("Criminal's crime", validators = [InputRequired()])
    inJail = StringField("Criminal's status", validators = [InputRequired()])
    country = StringField("Criminal's country", validators = [InputRequired()])
    submit = SubmitField("Edit Criminal")

class AddCriminal(FlaskForm):
    Name = StringField("Criminal's Name", validators=[InputRequired()])
    gender = StringField("Criminal's Gender", validators=[InputRequired()])
    # photo = StringField("Criminal's Photo Name",validators=[InputRequired()])
    img = FileField("Criminal's Img",validators=[InputRequired()])
    fingerprintImg = FileField("Criminal's Fingerprint",validators=[InputRequired()])
    crime = StringField("Criminal's crime", validators=[InputRequired()])
    inJail = StringField("Criminal's status", validators=[InputRequired()])
    country = StringField("Criminal's country", validators=[InputRequired()])
    submit = SubmitField("Add Criminal")