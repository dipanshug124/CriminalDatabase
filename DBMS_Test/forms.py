from flask_wtf import FlaskForm
from wtforms import StringField,FileField, SubmitField, PasswordField,DateField
from wtforms.validators import InputRequired

class EditCriminalRecord(FlaskForm):
    Name = StringField("Criminal's Full Name", validators=[InputRequired()])
    caseno = StringField("Case No", validators=[InputRequired()])
    img = FileField("Criminal's Img")
    gender = StringField("Criminal's Gender", validators=[InputRequired()])
    address = StringField("Criminal's Address", validators=[InputRequired()])
    crime = StringField("Criminal's crime", validators=[InputRequired()])
    crimelocation = StringField("Crime Location", validators=[InputRequired()])
    prison = StringField("Prison Location", validators=[InputRequired()])
    courtname = StringField("Court Name", validators=[InputRequired()])
    dutypolice = StringField("Duty Police Name", validators=[InputRequired()])
    punishment = StringField("Punishment", validators=[InputRequired()])
    startdate = DateField("Start date of punishment", validators=[InputRequired()])
    enddate = DateField("End date of punishment", validators=[InputRequired()])
    submit = SubmitField("Edit Criminal")

class AddCriminal(FlaskForm):
    Name = StringField("Criminal's Full Name", validators=[InputRequired()])
    gender = StringField("Criminal's Gender", validators=[InputRequired()])
    # photo = StringField("Criminal's Photo Name",validators=[InputRequired()])
    img = FileField("Criminal's Img", validators=[InputRequired()])
    fingerprintImg = FileField("Criminal's Fingerprint", validators=[InputRequired()])
    crime = StringField("Criminal's crime", validators=[InputRequired()])
    caseno = StringField("Criminal's Case_No", validators=[InputRequired()])
    address = StringField("Criminal's Address", validators=[InputRequired()])
    crimelocation = StringField("Crime Location", validators=[InputRequired()])
    prison = StringField("Prison Location", validators=[InputRequired()])
    courtname = StringField("Court Name", validators=[InputRequired()])
    dutypolice = StringField("Duty Police", validators=[InputRequired()])
    punishment = StringField("Punishment", validators=[InputRequired()])
    startdate = DateField("Start date of punishment", validators=[InputRequired()])
    enddate = DateField("End date of punishment", validators=[InputRequired()])
    submit = SubmitField("Add Criminal")

class Login(FlaskForm):
    admin = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password",validators=[InputRequired()])
    submit = SubmitField("Login")

class AddAdmin(FlaskForm):
    admin = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password",validators=[InputRequired()])
    submit = SubmitField("Add Admin")

class AddGrievance(FlaskForm):
    name = StringField("Full Name",validators=[InputRequired()])
    address = StringField("Address",validators=[InputRequired()])
    description = StringField("Grievance Details",validators=[InputRequired()])
    submit = SubmitField("Add Grievance")