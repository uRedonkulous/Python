from flask import Flask, render_template, session, redirect, request

app=Flask(__name__)

app.secret_key="Not a secret"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/form',methods=['POST'])
def form():
    session['name'] = request.form['name']
    session['dojolocation'] = request.form['dojolocation']
    session['language'] = request.form['language']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)
