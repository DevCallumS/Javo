from flask import Flask, render_template
from flask import redirect, url_for, request, session
from server import *
from sendEmailSystem import *
from flask_sqlalchemy import SQLAlchemy

web_server = Flask(__name__)
web_server.secret_key = "SecretKey"

web_server.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dataBase.sqlite3"
web_server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(web_server)

""" ROUTING """


@web_server.route("/")
@web_server.route("/home")
def index():
    return render_template("index.html")


@web_server.route("/sign-in", methods=["POST", "GET"])
def signIn():
    if request.method == "POST":
        uip = request.form["UIP"]
        pip = request.form["PIP"]

        # START PF DATABASE

        isAcct = checkForAccount(uip)
        if isAcct:
            isCorrect = checkUser(uip, pip)
            if isCorrect:
                print("WEB SERVER ANNOUNCEMENT--: CORRECT")
                return redirect(url_for("index"))
            else:
                print("WEB SERVER ANNOUNCEMENT--: INCORRECT")
                return render_template("signIn.html", incorrectPass="Wrong username or password.")
        else:
            return render_template("signIn.html", incorrectPass="That account was not registered.") #FOR TESTING ONLY
            # createAccount(uip, pip)
            # return render_template("signIn.html")

        # END OF DATABASE
    else:
        return render_template("signIn.html")

@web_server.route("/sign-up", methods=["POST", "GET"])
def signUp():
    if request.method == "POST":
        email = request.form["email"]
        uip = request.form["uip"]
        pip = request.form["pip"]

        isAcct = checkForAccount(uip)
        if isAcct:
            return render_template("signUp.html", incorrectData="Account is already registered with this username")
        else:
            return "none"
            # This will have the account creation data stuff

    else:
        return render_template("signUp.html")

@web_server.route("/sendE")
def sendE():
    sendEmail("hypercodemarkup@gmail.com", "Javo - Testing", "Test from Javo support system.")
    return render_template("index.html")


@web_server.route("/create")
def create():
    createAccountForTesting()
    return redirect(url_for("index"))


@web_server.route("/run<data>")
def run(data):
    print(data)
    return "none"


""" ERROR HANDLING """

@web_server.errorhandler(404)
def error404(error):
    return render_template("error.html", EC="Error! Page Not Found!"), 404


@web_server.errorhandler(500)
def error500(error):
    return render_template("error.html", EC="Error! Internal Server Issue!"), 500


if __name__ == "__main__":
    db.create_all()
    # server.run(host="192.168.1.80", port="3000") #For running on IP address
    web_server.run(port="3000")