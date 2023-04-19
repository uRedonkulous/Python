from flask import render_template, session, redirect, request
from flask_app import app
from flask_app.models.user import User
from flask_app.models.activity import Activity
from flask import flash


#  Activities Dashboard after Login/Registering
@app.route("/activities/dashboard") 
def activity_dash():
    if "user_id" not in session:
        flash("You must be logged in to view page")
        return redirect("/")
    user = User.get_by_id(session["user_id"])
    activities = Activity.get_all()
    activity = Activity.get_all_by_user(session["user_id"])
    return render_template("dashboard.html", user=user, activities=activities, activity=activity)

#  Get activity
@app.route('/activities/<int:activity_int>')
def activity_desc(activity_id):
    user=User.get_by_id(session['id'])
    activity=Activity.get_by_id(activity_id)
    return render_template('activity_desc.html',user=user,activity=activity)

#  Creating a Activity POST to form to INSERT into DB
@app.route('/activities/create')
def create_activity():
    if "user_id" not in session:
        return redirect('/')
    user = User.get_by_id(session["user_id"])
    return render_template("create_activity.html", user=user)


#  Create activity Validation
@app.route('/activities',methods=["POST"])
def create_activities():
    activity = {
        "activity": request.form["activity"],
        "duration":request.form["duration"], 
        "description":request.form["description"], 
        "user_id":session["user_id"]
    }
    valid_activity=Activity.create_activity(activity)
    if valid_activity:
        return redirect('/activities/dashboard')
    return redirect('/activities/create')


#  Edit activity
@app.route('/activities/edit/<int:activity_id>')
def edit_activity(activity_id):
    if "user_id" not in session:
        return redirect('/')
    activity=Activity.get_by_id(activity_id)
    user = User.get_by_id(session["user_id"])
    valid_activity=Activity.is_valid(activity_id, session["user_id"])
    if valid_activity:
        return render_template('/edit_activity.html', user=user, activity=activity)
    else:
        flash("You do not have permission to edit this activity.")
        return ('/activities/edit/<int:activity_id>')

# #  Update Activity
@app.route("/activities/<int:activity_id>", methods=["POST"])
def update_activity(activity_id):
    activity = {
        "id" : activity_id,
        "activity_name" : request.form["activity_name"],
        "duration" : request.form["duration"],
        "description" : request.form["description"]
    }
    valid_activity = Activity.update_activity(activity, session["user_id"])
    if not valid_activity:
        return redirect(f"/activities/edit/{activity_id}")
    return redirect(f"/activities/dashboard")

#  Delete activity
@app.route('/activities/delete/<int:activity_id>')
def delete_activity(activity_id):
    Activity.delete_activity_by_id(activity_id)
    return render_template('/activities/dashboard')

