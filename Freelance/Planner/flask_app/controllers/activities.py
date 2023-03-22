from flask import render_template, session, redirect, request
from flask_app import app
from flask_app.models.user import User
from flask_app.models.activity import Activity
from flask import flash


#  Activities Dashboard after Login/Registering
@app.route("/activities/dashboard") 
def activities_dash():
    if "user_id" not in session:
        flash("You must be logged in to view page")
        return redirect("/")
    user = User.get_by_id(session["user_id"])
    # activities= Activity.get_all()
    return render_template("dashboard.html", user=user)

#  Get activity
@app.route('/activities/<int:activity_int>')
def activity_desc(activity_id):
    user=User.get_by_id(session['id'])
    activity=Activity.get_by_id(activity_id)
    return render_template('activity_desc.html',user=user,activity=activity)

#  Create activity
@app.route('/activities/create', methods=['GET','POST'])
def create_activity():
    if request.method == "POST":
    
        valid_activity=Activity.create_valid_activity(request.form)
        if valid_activity:
            return redirect('/activities/dashboard')
    return render_template('create_activity.html')

#  Edit activity
@app.route('/activities/edit/<int:activity_id>')
def edit_activity(activity_id):
    activity=Activity.get_by_id(activity_id)
    return render_template('/edit_activity.html', activity=activity)

#  Delete activity
@app.route('/activities/delete/<int:activity_id>')
def delete_activity(activity_id):
    Activity.delete_activity_by_id(activity_id)
    return render_template('/activities/dashboard')

