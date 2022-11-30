from lib import *


signup = Blueprint("signup",__name__, template_folder=template_dir, static_folder=static_dir)


@signup.route('/signup', methods=['POST', 'GET'])
def signupPage():
    if request.method == 'POST':
        emailInput = request.form['email-input']
        passwordInput = request.form['password-input']
        usernameInput = request.form['username-input']
        id = uuid.uuid4().time_low
        print(id)
        new_account = Accounts(id=id, email=emailInput, password=passwordInput, username=usernameInput, bio="", profile_picture_metadata="")
        try:
            print("adding data")
            db.session.add(new_account)
            db.session.commit()
            print("Successful")
            return redirect('/login')
        except:
            return "Something went wrong"
    else:
        return render_template("signUp.html")