from asyncio import Task
from lib import *

task = Blueprint("task", __name__, template_folder=template_dir, static_folder=static_dir)

@task.route("/createTask", methods=["GET", "POST"])
@login_required
def createTask(projectId):
    project = Projects.query.filter_by(id=projectId).first()
    if request.method == "POST":
        taskName = request.form['task-name']
        id = uuid.uuid4().time_low
        newTask = Tasks(id=id, name=taskName, project=project, state=False, description="")
        try:
            db.session.add(newTask)
            db.session.commit()
            return redirect(url_for("projectPage", projectId = project.id))
        except SQLAlchemyError as e:
            print(type(e))
            return "Something went wrong\n Try again"


@task.route('/<taskId>', methods=["GET", "POST"])
@login_required
def taskPage(projectId, taskId):
    task = Tasks.query.filter_by(id = taskId).first()
    project = Projects.query.filter_by(id=projectId).first()
    if request.method == "POST":
        members = request.form["members"].split(",")
        deassigned = request.form["deassigned"].split(",")
        print(task.workedOnBy)
        print(members)
        print(deassigned)
        try:
            for member in members:
                if member not in task.workedOnBy and member!="":
                    task.workedOnBy.append(Accounts.query.filter_by(id=int(member)).first())
            for member in deassigned:
                if member!='':
                    res = db.engine.execute(f"DELETE FROM task_user_relationship WHERE user_id = {int(member)} AND task_id = {taskId}")
            db.session.commit()
        except SQLAlchemyError as e:
            print(type(e))
            return "Something went wrong"
        return "Succesfully made changes"
    else:
        return render_template("taskPage.html", task=task, project=project, url=request.path)