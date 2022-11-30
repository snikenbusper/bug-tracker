from lib import *

login = Blueprint("login", __name__, template_folder=template_dir, static_folder=static_dir)

@login.route('/login', methods=["POST", "GET"])
def loginPage():
    if request.method == "POST":
        #authenticate user
        email = request.form['email']
        password = request.form['password']
        user = Accounts.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                login_user(user)
                return redirect(url_for('home'))
        return "Invalid"
        
    else:
        print("LOGIN")
        return render_template('login.html')