from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi' , 'full_name' : 'Michael Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin' , 'full_name' : 'John Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen' , 'full_name' : 'Mark Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel' , 'full_name' : 'KB Tonel'}
    ]
    return render_template("index.html",users=users)



if __name__=="__main__":
    app.run(debug=True)