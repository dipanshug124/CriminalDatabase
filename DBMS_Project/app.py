from os import abort
from flask import Flask, render_template, abort
from flask import session, redirect, url_for,request
from flask_sqlalchemy import SQLAlchemy
from forms import EditCriminalRecord,AddCriminal
import sqlite3
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
#c1
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True;
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///criminals.db'


db = SQLAlchemy(app)

"""Model for criminal."""
class Criminal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String, unique=True)
    Name = db.Column(db.String, unique=True)
    gender = db.Column(db.String)
    crime = db.Column(db.String)
    inJail = db.Column(db.String)
    country=db.Column(db.String)

db.create_all()
# search query Course.query.woosh_search('python').all()


# create all criminals

domanic = Criminal(photo="1p", Name="Domanic", gender="Male", crime="Hacking", inJail ="Yes", country="Germany" )
patty = Criminal(photo="2p", Name="Patty", gender="Male", crime="Terrorism", inJail ="Yes", country="Japan")
inger = Criminal(photo="3p", Name="Inger", gender="Female", crime="Kidnapping", inJail ="Yes", country="New Zealand")
harry = Criminal(photo="4p", Name="Harry", gender="Male", crime="Shoplifting", inJail ="Yes", country="Pakistan")
jessy = Criminal(photo="5p", Name="Jessy", gender="Female", crime="Buglary", inJail ="No", country="Russia")

#add all pets to the session
db.session.add(domanic)
db.session.add(patty)
db.session.add(inger)
db.session.add(harry)
db.session.add(jessy)

# Commit changes in the session
try:
    db.session.commit()
except Exception as e:
    db.session.rollback()
finally:
    db.session.close()

"""Information"""
# criminals = [
#     {"id": 1, "photo": "1p", "Name": "Domanic", "gender": "Male", "crime": "Hacking", "inJail": "Yes", "country": "Germany"},
#     {"id": 2, "photo": "2p",  "Name": "Patty", "gender": "Male", "crime": "Terrorism", "inJail": "Yes", "country": "Japan"},
#     {"id": 3,  "photo": "3p", "Name": "Inger", "gender": "Female", "crime": "Kidnapping", "inJail": "Yes", "country": "New Zealand"},
#     {"id": 4,  "photo": "4p", "Name": "Harry", "gender": "Male", "crime": "Shoplifting", "inJail": "Yes", "country": "Pakistan"},
#     {"id": 5,  "photo": "5p", "Name": "Jessy", "gender": "Female", "crime": "Buglary", "inJail": "No", "country": "Russia"},
# ]
#Homepage
@app.route("/")
def homepage():
    # """View function for home page"""
    criminals = Criminal.query.all()
    return render_template("home.html", criminals = criminals)

#about
@app.route("/about")
def aboutpage():
    return render_template("about.html")

#search
@app.route('/search')
def search():
    s=request.args.get('search')
    criminals = Criminal.query.filter(Criminal.Name.like('%'+s+'%'))
    return render_template('home.html',criminals=criminals)

#add criminal
@app.route("/add", methods=["POST", "GET"])
def addpage():
    form = AddCriminal()
    if form.validate_on_submit():
        criminal = Criminal(photo=form.photo.data, Name=form.Name.data, gender=form.gender.data, crime=form.crime.data,
                            inJail=form.inJail.data, country=form.country.data)
        db.session.add(criminal)
        try:
            db.session.commit()
        except Exception as e:
            #print(e)
            db.session.rollback()
            return render_template("add.html",form=form, message="Criminal already exists!")
        finally:
            db.session.close()
        return render_template("add.html",message="Criminal Added Successfully")
    return render_template("add.html",form = form)

@app.route("/details/<int:criminal_id>", methods=["POST", "GET"])
def criminal_details(criminal_id):
    """View function for Showing Details of Each Pet."""
    #criminal = next((criminal for criminal in criminals if criminal["id"] == criminal_id), None)
    criminal = Criminal.query.get(criminal_id)
    form = EditCriminalRecord()
    if criminal is None:
        abort(404, description="No Criminal was Found with the given ID")
    if form.validate_on_submit():
        criminal.Name=form.Name.data
        criminal.gender=form.gender.data
        criminal.crime=form.crime.data
        criminal.inJail=form.inJail.data
        criminal.country=form.country.data
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return render_template("details.html",criminal=criminal, form=form, message="A Criminal with name already exists!" )
    return render_template("details.html", criminal=criminal, form = form)

@app.route("/delete/<int:criminal_id>")
def delete_criminal(criminal_id):
    criminal = Criminal.query.get(criminal_id)
    if criminal is None:
        abort(404, description="No Criminal was Found with the given ID")
    db.session.delete(criminal)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
    return redirect(url_for('homepage', _scheme='https', _external=True))

if __name__ == "__main__":
    app.run(debug= True)
