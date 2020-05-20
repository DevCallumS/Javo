from webServer import db

class dataBase(db.Model):
    #_id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


def checkUser(username, password):
    usernameQuery = dataBase.query.filter_by(username=username).first()
    correctUser = usernameQuery.username
    correctPass = usernameQuery.password

    if username == correctUser and password == correctPass:
        return True
    else:
        return False


def checkForAccount(uip):
    found_user = dataBase.query.filter_by(username=uip).first()
    return found_user


def createAccount(email, uip, pip):
    accountStartupData = dataBase(email, uip, pip)
    db.session.add(accountStartupData)
    db.session.commit()


def createAccountForTesting():
    db.session.add("hypercodemarkup@gamil.com", "", "")
    db.session.commit()