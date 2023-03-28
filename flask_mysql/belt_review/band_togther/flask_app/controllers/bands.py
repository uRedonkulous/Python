from flask import render_template, session, redirect, request
from flask_app import app
from flask_app.models.user import User
from flask_app.models.band import Band
from flask import flash


#  Band Dashboard after Login/Registering
@app.route("/bands/dashboard") 
def band_dash():
    if "user_id" not in session:
        flash("You must be logged in to view page")
        return redirect("/")
    user = User.get_by_id(session["user_id"])
    bands = Band.get_all()
    band = Band.get_all_by_user(session["user_id"])
    return render_template("dashboard.html", user=user, bands=bands, band=band)

#  User Bands
@app.route('/bands/my_bands')
def band_info():
    if "user_id" not in session:
        return redirect('/')
    user=User.get_by_id(session['user_id'])
    bands=Band.get_all_by_user(session["user_id"])
    return render_template('my_bands.html',user=user,bands=bands)

#  Creating a Band POST to form to INSERT into DB
@app.route('/bands/create')
def create_band():
    if "user_id" not in session:
        return redirect('/')
    user = User.get_by_id(session["user_id"])
    return render_template("create_band.html", user=user)

#  Create Band Validation
@app.route('/bands',methods=["POST"])
def create_bands():
    band = {
        "band_name": request.form["band_name"],
        "genre":request.form["genre"], 
        "city":request.form["city"], 
        "user_id":session["user_id"]
    }
    valid_band=Band.create_valid_band(band)
    if valid_band:
        return redirect('/bands/dashboard')
    return redirect('/bands/create')

#  Edit Band
@app.route('/bands/edit/<int:band_id>')
def edit_band(band_id):
    if "user_id" not in session:
        return redirect('/')
    band=Band.get_by_id(band_id)
    user = User.get_by_id(session["user_id"])
    valid_band=Band.is_valid
    if valid_band:
        return render_template('edit_band.html', user=user, band=band)
    return ('/bands/edit/<int:band_id>')

# #  Update Band
@app.route("/bands/<int:band_id>", methods=["POST"])
def update_band(band_id):
    band = {
        "id" : band_id,
        "band_name" : request.form["band_name"],
        "genre" : request.form["genre"],
        "city" : request.form["city"]
    }
    valid_band = Band.update_band(band, session["user_id"])
    if not valid_band:
        return redirect(f"/bands/edit/{band_id}")
    return redirect(f"/bands/dashboard")

#  Delete Band
@app.route('/bands/delete/<int:band_id>')
def delete_band(band_id):
    Band.delete_band_by_id(band_id)
    return redirect('/bands/dashboard')
