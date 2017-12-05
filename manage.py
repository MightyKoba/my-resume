from flask_script import Manager
from myresume import app, db, Professor, Course


manager = Manager(app)


@manager.command
def deploy(): 
    db.drop_all()
    db.create_all()
    dianne_leipold = Professor(name='Dianne Leipold', department='Business Administration')
    demetrius_pinder = Professor(name='Demetrius Pinder', department='Management Information Systems')
    ryan_lowe = Professor(name='Ryan Lowe', department='Business Administration')
    pratyush_sharma = Professor(name='Pratyush Sharma', department='Management Information Systems')
    course1 = Course(name='Organizational Behavior BUAD', course_number=309, description="recognize, name, and describe organizational behavior (OB) theories and concepts in practice identify and apply the principles of OB theories and concepts to your own personal and work experiences analyze and apply these concepts and theories to the challenges of management.", professor=dianne_leipold)
    course2 = Course(name='Business Computing: Tools and Concepts MISY', course_number=160, description="Introduction to computers: components and operations. Introduction to management information/decision support systems and the system development process. Emphasis on microcomputers and software packages used in business.", professor=demetrius_pinder)
    course3 = Course(name='Introduction to Entrepreneurship BUAD', course_number=350, description="This course focuses on understanding the basic concepts, tools, and practices of entrepreneurship and the development of entrepreneurial skills. The entrepreneurial process (opportunity recognition, resource marshaling, and team building driven by communication, creativity, and leadership) and business planning are emphasized.", professor=ryan_lowe)
    course4 = Course(name='Database Design and Implementation: MISY', course_number=330, description="Covers the design and implementation of enterprise databases in the business environment. A networked setting and its effect on database management will be emphasized. PREREQ: MISY160 or CISC181. RESTRICTIONS: MIS majors and MIS and/or GET minors only. Not open to computer science majors in the MIS minor. Not open to students who double major in both accounting and management information systems.", professor=pratyush_sharma)
    db.session.add(dianne_leipold)
    db.session.add(demetrius_pinder)
    db.session.add(ryan_lowe)
    db.session.add(pratyush_sharma)
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.add(course4)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
