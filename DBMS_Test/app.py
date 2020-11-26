from os import abort
from flask import Flask, render_template, abort
from flask import session, redirect, url_for,request
from flask_sqlalchemy import SQLAlchemy
from forms import EditCriminalRecord,AddCriminal,Login,AddAdmin,AddGrievance
import sqlite3
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
#c1
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True;
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///criminals.db'


db = SQLAlchemy(app)

"""Is user Logged in"""
isLogin=False

"""Model for criminal."""
class Criminal(db.Model):
    class Criminal(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        caseno = db.Column(db.String, unique=True)
        photo = db.Column(db.String, unique=True)  # name of img
        fingerprint = db.Column(db.String, unique=True)  # name of fingerprintImg
        Name = db.Column(db.String, unique=True)
        address = db.Column(db.String)
        gender = db.Column(db.String)
        crimelocation = db.Column(db.String)
        prison = db.Column(db.String)
        courtname = db.Column(db.String)
        dutypolice = db.Column(db.String)
        punishment = db.Column(db.String)
        crime = db.Column(db.String)
        startdate = db.Column(db.Date)
        enddate = db.Column(db.Date)

"""Model for Admin"""
class Admins(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    admin = db.Column(db.String,unique=True)
    #Name = db.Column(db.String);
    password=db.Column(db.String,unique=True)

#model for Grievance
class Grievance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String)
    #Name = db.Column(db.String);
    address= db.Column(db.String)
    description = db.Column(db.String)
    #status = db.Column(db.String)

db.create_all()
superadmin="Police1234"
superpassword="1234"
currentadmin=""
# Police1234 is superadmin
#adminUser = Admins(admin="Police1234",password="1234")
#db.session.add(adminUser)
#db.session.commit()
# create all criminals

# domanic = Criminal(photo="1p", Name="Domanic", gender="Male", crime="Hacking", inJail ="Yes", country="Germany" )
# patty = Criminal(photo="2p", Name="Patty", gender="Male", crime="Terrorism", inJail ="Yes", country="Japan")
# inger = Criminal(photo="3p", Name="Inger", gender="Female", crime="Kidnapping", inJail ="Yes", country="New Zealand")
# harry = Criminal(photo="4p", Name="Harry", gender="Male", crime="Shoplifting", inJail ="Yes", country="Pakistan")
# jessy = Criminal(photo="5p", Name="Jessy", gender="Female", crime="Buglary", inJail ="No", country="Russia")

#add all pets to the session
# db.session.add(domanic)
# db.session.add(patty)
# db.session.add(inger)
# db.session.add(harry)
# db.session.add(jessy)

#Commit changes in the session
# try:
#     db.session.commit()
# except Exception as e:
#     db.session.rollback()
# finally:
#     db.session.close()

#Homepage
@app.route("/")
def homepage():
    # """View function for home page"""
    criminals = Criminal.query.all()
    type=""
    if isLogin==False:
        type="Login"

    else:
        type="Logout"
    return render_template("home.html", criminals = criminals,type=type)

#about
@app.route("/about")
def aboutpage():
    type=""
    if isLogin==False:
        type="Login"
    else:
        type="Logout"
    return render_template("about.html" ,type=type)

#Grievance Dashboard
@app.route("/dashboard",methods=["POST","GET"])
def usergrievancepage():
    grievance = Grievance.query.all()
    if isLogin == False:
         return render_template("usergrievance.html", grievance=grievance)
    return render_template("admingrievance.html",grievance=grievance)  

#Grievance
@app.route("/grievance", methods=["POST", "GET"])
def grievancepage():
    grievance=Grievance.query.all()
    if isLogin == False:
       
        #return redirect(url_for('grievancepage'))
        form = AddGrievance()
        if form.validate_on_submit():
            grievances = Grievance(name=form.name.data, address = form.address.data, description= form.description.data)
        # form.img.data.read() ->will give use raw data blob ;)
            db.session.add(grievances)
        # print(form.img.data.filename)
        # print("File:{}".format(form.img.data.read()))
            try:
                db.session.commit()
            except Exception as e:
                print(e)
                db.session.rollback()
                return render_template("grievance.html", form = form, message = "Grievance already exists!")
            finally:
                db.session.close()
                return render_template("grievance.html", message = "Grievance Added Successfully")
            return render_template("grievance.html", form = form)
        return render_template('grievance.html',form= form)
    else:
        return render_template('usergrievance.html',grievance=grievance)

#search
@app.route('/search')
def search():
    s = request.args.get('search')
    # criminals = Criminal.query.filter(Criminal.Name.like('%' + s + '%') )
    criminals = Criminal.query.filter(Criminal.crime.like('%' + s + '%'))
    # criminals += Criminal.query.filter(Criminal.dutypolice.like('%' + s + '%'))
    # criminals += Criminal.query.filter(Criminal.courtname.like('%' + s + '%'))
    # criminals += Criminal.query.filter(Criminal.prison.like('%' + s + '%'))
    # criminals += Criminal.query.filter(Criminal.gender.like('%' + s + '%'))
    #criminals = Criminal.query.filter(Criminal.caseno.like('%' + s + '%') )
    # criminals += Criminal.query.filter(Criminal.crimelocation.like('%' + s + '%'))
    type = ""
    if isLogin == False:
        type = "Login"
    else:
        type = "Logout"
    return render_template('home.html',criminals=criminals,type=type)

#login
@app.route("/login",methods=["POST","GET"])
def login():
    global isLogin
    global currentadmin
    if isLogin==True:
        # global isLogin
        isLogin=False
        currentadmin=""
        criminals = Criminal.query.all()
        return render_template("home.html", criminals=criminals, type="Login")
    form = Login()
    if form.validate_on_submit():
        username_entered = form.admin.data
        password_entered = form.password.data
        # check credentials is invalid
        user_object = Admins.query.filter_by(admin=username_entered).first()
        if user_object is None:
            return render_template("login.html",form = form,message="Username or password is incorrect")
        elif password_entered != user_object.password:
            return render_template("login.html",form = form,message="Username or password is incorrect")
        else:
            print("login sucessfully")
            # global isLogin
            isLogin=True
            currentadmin=username_entered
            print(currentadmin)
            criminals = Criminal.query.all()

            return render_template("home.html", criminals=criminals,type="Logout")
    return render_template("login.html",form = form)

#add admins by super admin
#add criminal
@app.route("/newuser",methods=["POST","GET"])
def newuser():
    print(currentadmin)
    if currentadmin==superadmin and isLogin==True:
        form=AddAdmin()
        print(currentadmin==superadmin," ", isLogin)
        if form.validate_on_submit():
            ad = Admins(admin=form.admin.data, password=form.password.data)
            db.session.add(ad)
            try:
                db.session.commit()
            except Exception as e:
                print(e)
                db.session.rollback()
                return render_template("newuser.html", form=form, message="username or password already exists", type="Logout")
            finally:
                db.session.close()
            return render_template("newuser.html", message="Admin Added Successfully", type="Logout")

        return render_template("newuser.html", form=form,message="Enter username and password ", type="Logout")
    else:
        return render_template("newuser.html", message="You are not authorized person to add new admin",
                               type="Logout")

@app.route("/add", methods=["POST", "GET"])
def addpage():
    if isLogin==False:
        #return render_template("login.html", message="You first Should Login")
        return redirect(url_for('login'))
    form = AddCriminal()
    if form.validate_on_submit():
        criminals = Criminal(photo=form.img.data.filename, fingerprint=form.fingerprintImg.data.filename,
                             Name=form.Name.data, gender=form.gender.data, crime=form.crime.data,
                             caseno=form.caseno.data, address=form.address.data, crimelocation=form.crimelocation.data,
                             prison=form.prison.data, courtname=form.courtname.data, dutypolice=form.dutypolice.data,
                             punishment=form.punishment.data, startdate=form.startdate.data, enddate=form.enddate.data)
        # form.img.data.read() ->will give use raw data blob ;)
        db.session.add(criminals)
        print(form.img.data.filename)
        # print("File:{}".format(form.img.data.read()))
        try:
          db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            return render_template("add.html",form=form, message="Criminal already exists!",type="Logout")
        finally:
            db.session.close()
        return render_template("add.html",message="Criminal Added Successfully",type="Logout")
    return render_template("add.html",form = form,type="Logout")

@app.route("/details/<int:criminal_id>", methods=["POST", "GET"])
def criminal_details(criminal_id):
    """View function for Showing Details of Each Pet."""
    if isLogin==False:
        return redirect(url_for('login'))
    #criminal = next((criminal for criminal in criminals if criminal["id"] == criminal_id), None)
    criminal = Criminal.query.get(criminal_id)

    form = EditCriminalRecord()
    if criminal is None:
        abort(404, description="No Criminal was Found with the given ID")
    if form.validate_on_submit():
        criminal.Name = form.Name.data
        if (len(form.img.data.filename) > 0):
            criminal.photo = form.img.data.filename
        criminal.gender = form.gender.data
        criminal.crime = form.crime.data
        criminal.caseno = form.caseno.data
        criminal.address = form.address.data
        criminal.crimelocation = form.crimelocation.data
        criminal.prison = form.prison.data
        criminal.courtname = form.courtname.data
        criminal.dutypolice = form.dutypolice.data
        criminal.punishment = form.punishment.data
        criminal.startdate = form.startdate.data
        criminal.enddate = form.enddate.data
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return render_template("details.html",criminal=criminal, form=form, message="A Criminal with name already exists!" ,type="Logout")
    return render_template("details.html", criminal=criminal, form = form, type="Logout")

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
