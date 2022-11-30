from lib import *
from signup import signup
from login import login
from task import task


app.register_blueprint(signup, url_prefix="")
app.register_blueprint(login, url_prefix="")
app.register_blueprint(task, url_prefix="/project/<projectId>/task")


@app.route('/', methods=["GET"])
@app.route('/home', methods=["GET"])
@login_required
def home():
    return render_template("home.html", name=current_user.username)


@app.route('/logout', methods=["GET"])
@login_required
def logout():
    flash("You have been logged out") #this gets flashed to otehr messages
    logout_user()
    return redirect('/login')

@app.route('/projects', methods=['GET', 'POST'])
@login_required
def projectList():
    joinPopUp = False
    if "joinPopUp" in session:
        joinPopUp = session["joinPopUp"]
        session["joinPopUp"] = False

    return render_template("projects.html", projectAmount=len(current_user.onProject), projects=current_user.onProject, joinPopUp = joinPopUp)

@app.route('/project/<projectId>', methods=['GET', "POST"])
@login_required
def projectPage(projectId):
    project = Projects.query.filter_by(id=projectId).first()
    print(project)
    if(project):
        return render_template("projectPage.html", project=project)
    else:
        return "Project not found"
    

@app.route('/createProject', methods=['POST'])
@login_required
def createProject():
    projectName = request.form['project-name']
    id = uuid.uuid4().time_low
    project = Projects(id=id, name=projectName, owner=current_user)
    print(project)
    try:
        db.session.add(project)
        current_user.onProject.append(project)
        db.session.commit()
        projectUrl = "/project/"+str(project.id)
        project.url = projectUrl
        db.session.commit()
        return redirect(url_for('projectList'))
    except SQLAlchemyError as e:
        print(type(e))
        return "Something went wrong"


@app.route('/joinProject', methods=["POST"])
@login_required
def joinProject():
    id = request.form['project-id']
    project = Projects.query.filter_by(id=id).first()
    if project:
        try:
            print(current_user.onProject)
            current_user.onProject.append(project)
            db.session.commit()
            return "Succesfully joined project"
        
        except SQLAlchemyError as e:
            return "Something went wrong , Please try"
        
    else:
        flash("Invalid project id", "error")
        session["joinPopUp"] = True
        return redirect(url_for("projectList"))

@app.route('/profile', methods=["GET", "POST"])
@login_required
def profile():
    if request.method=="POST":
        if request.form["type"] == "username":
            newUsername = request.form["username"]
            if newUsername != current_user.username:
                current_user.username = newUsername
                db.session.commit()

            return render_template("profile.html", user=current_user)
        elif request.form["type"] == "image":
            print("Image recieved")
            image = request.files["profile-picture"]
            if image.filename=="":
                return "No file chosen"
            elif allowedFileExtensions(image.filename):
                filename = secure_filename(image.filename)
                filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

                try:
                    current_user.profile_picture_metadata = os.path.join("/static/profilePictures", filename)
                    db.session.commit()
                    image.save(filepath)
                except SQLAlchemyError as e:
                    print(e)
                    return "Something went wrong"
                
                return "file successfuly uploaded"
    
    return render_template("profile.html", user=current_user, path=current_user.profile_picture_metadata)

@app.route("/profileView/<userId>", methods=["GET"])
def profileView(userId):
    user = Accounts.query.filter_by(id=userId).first()
    return render_template("profileView.html", user = user)

if __name__ == "__main__":
    app.run(debug=True)