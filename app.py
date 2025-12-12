from flask import Flask , render_template , request , redirect , url_for

app = Flask(__name__)


#login route
@app.route('/login' , methods=["GET" , "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        #check 
        if username == "admin" and password == "happysingh@example":
            return render_template("home.html")
        else:
            return render_template("login.html" , error="Invalid username or password")
    return render_template('login.html')

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)