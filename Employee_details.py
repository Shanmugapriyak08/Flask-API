from  flask import Flask,request
from flask.templating import render_template
from database import insert_Record,select_Record,delete_Record,update_Location
from emoji import emojize
app=Flask(__name__)

@app.route("/")
def login():
    return render_template("employee_login.html")

@app.route("/home",methods=["POST"])
def home_page():
    if request.form['pass'] == "priya":
        return render_template("employee_home_page.html")
    else:
        return (f"InCorrect Password " + emojize(":unamused_face:"))

@app.route('/backhome')
def backhome():
    return render_template("employee_home_page.html")

@app.route("/add")
def add():
    return render_template("employee_add.html")

@app.route("/savedetails",methods=["POST"])
def savedetails():
    try:
        if request.method=='POST':
            id = request.form["id"]
            name=request.form["name"]
            email=request.form["email"]
            location=request.form["location"]
            salary=request.form["salary"]
            band=request.form["band"]
            try:
                insert=insert_Record(id,name,email,location,salary,band)
                msg="Employee successfully Added"
                return render_template("employee_success.html",op_msg=msg)
            except :
                errormsg="Employee ID is already present... (:"
                return render_template("employee_success.html",op_msg=errormsg)
    except Exception as e:
        raise Exception (f"(savedetails):Something went wrong on while saving details "+str(e))


@app.route("/view")
def view():
    rows=select_Record()
    return render_template("employee_view.html",rows=rows)

@app.route("/delete")
def delete():
   return render_template("employee_delete.html")

@app.route("/afterdelete",methods=['POST','GET'])
def after_delete():
    try:
        if request.method=='POST':
            id=request.form["id"]
            edelete=delete_Record(id)
            if edelete!=0:
                msg="Employee details Deleted successfully"
                return render_template("employee_after_delete.html",op_msg=msg)
            else:
                errormsg="Entered employee Id is not available (:"
                return render_template("employee_after_delete.html",op_msg=errormsg)
            
    except Exception as e:
        raise Exception (f"(after_delete):Something went wrong on while deleting record "+str(e))

@app.route("/update")
def update():
   return render_template("employee_update.html")

@app.route("/afterupdate",methods=['POST','GET'])
def after_update():
    try:
        if request.method=='POST':
            location=request.form["location"]
            id=request.form["id"]
            lupdate=update_Location(location,id)
            if lupdate!=0:
                msg="Employee details Updated successfully..."
                return render_template("employee_after_update.html",op_msg=msg)
            else:
                errormsg="Entered employee Id is not available (:"
                return render_template("employee_after_update.html",op_msg=errormsg) 
               
    except Exception as e:
        raise Exception (f"(after_update):Something went wrong on while updating record "+str(e))

if __name__=="__main__":
    app.run(debug=True)
