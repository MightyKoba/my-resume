import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'this should be a secret key'


# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)



class Professor(db.Model):
    __tablename__ = 'professors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    department = db.Column(db.Text)
    courses = db.relationship('Course', backref='professor')



class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    course_number = db.Column(db.Integer)
    description = db.Column(db.Text)
    professor_id = db.Column(db.Integer, db.ForeignKey('professors.id'))





@app.route('/')
def index():
    # return HTML
    # return "<h1>this is the index page!<h1>"
    return render_template('index.html')


@app.route('/professors')
def show_all_professors():
    professors = Professor.query.all()
    return render_template('professor-all.html', professors=professors)



@app.route('/professor/add', methods=['GET', 'POST'])
def add_professors():
    if request.method == 'GET':
        return render_template('professor-add.html')
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        department = request.form['department']

        # insert the data into the database
        professor = Professor(name=name, description=description)
        db.session.add(professor)
        db.session.commit()
        return redirect(url_for('show_all_professors'))




@app.route('/professor/edit/<int:id>', methods=['GET', 'POST'])
def edit_professor(id):
    professor = Professor.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('professor-edit.html', professor=professor)
    if request.method == 'POST':
        # update data based on the form data
        professor.name = request.form['name']
        professor.department = request.form['department']
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_professors'))





@app.route('/about')
def about():
    return render_template('about.html')




@app.route('/course/add', methods=['GET', 'POST'])
def add_courses():
    if request.method == 'GET':
        professors = Professor.query.all()
        return render_template('course-add.html', professors=professors)
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        course_number = request.form['course_number']
        description = request.form['description']
        professor_name = request.form['professor']
        professor = Professor.query.filter_by(name=professor_name).first()
        course = Course(name=name, course_number=course_number, description=description, professor=professor)

# insert the data into the database
        db.session.add(course)
        db.session.commit()
        return redirect(url_for('show_all_courses'))


@app.route('/course-directory')
def show_all_courses():
    courses = Course.query.all()
    return render_template('course-all.html', courses=courses)


@app.route('/course/edit/<int:id>', methods=['GET', 'POST'])
def edit_course(id):
    course = Course.query.filter_by(id=id).first()
    professors = Professor.query.all()
    if request.method == 'GET':
        return render_template('course-edit.html', course=course, professors=professors)
    if request.method == 'POST':
        # update data based on the form data
        course.name = request.form['course']
        course.course_number = request.form['course_number']
        course.description = request.form['description']
        professor_name = request.form['professor']
        professor = Professor.query.filter_by(name=professor_name).first()
        course.professor = professor
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_courses'))



@app.route('/course/<int:id>/')
def get_course_id(id):
    # return "This song's ID is " + str(id)
    return "Hi, this is %s and the course's id is %d" % ('administrator', id)


# https://goo.gl/Pc39w8 explains the following line
if __name__ == '__main__':

    # activates the debugger and the reloader during development
    # app.run(debug=True)
    app.run()

    # make the server publicly available on port 80
    # note that Ports below 1024 can be opened only by root
    # you need to use sudo for the following conmmand
    # app.run(host='0.0.0.0', port=80)
