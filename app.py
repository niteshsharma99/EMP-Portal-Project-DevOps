from models import models
from flask import Flask, request, render_template, redirect

DATABASE = 'emp_db.db'
app = Flask(__name__)
#SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+DATABASE
app.config.from_object(__name__)
db = models.db
db.init_app(app)
db.app = app


with app.app_context():
    db.create_all()


# the application's main/index page
@app.route('/')
def index():
    employees = models.Employee.query.order_by(models.Employee.id).all()
    return render_template('index.html', employees=employees)


# add page; to add a new employee
@app.route('/add', methods=['POST', 'GET'])
def add():

    if request.method == 'POST':
        form_data = request.form
        obj = models.Employee(name=form_data['name'],
                              gender=form_data['gender'],
                              address=form_data['address'],
                              phone=form_data['phone'],
                              salary=form_data['salary'],
                              department=form_data['department'])

        try:
            db.session.add(obj)
            db.session.commit()
            return redirect('/')
        except Exception:
            return 'There was an error'

    else:
        return render_template('add.html')


# deleted page; to delete the employee
@app.route('/delete', methods=['POST'])
def delete():

    if request.method == 'POST':
        id = request.form['emp_id']
        obj = models.Employee.query.filter_by(id=int(id)).first()
        if obj:
            try:
                db.session.delete(obj)
                db.session.commit()
                return redirect('/')
            except Exception as e:
                print(e)
                return "There was an error"
        else:
            return render_template('index.html',
                                   error='Sorry, the employee does not exist.')


# edit page; to edit the information of an employee
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    obj = models.Employee.query.filter_by(id=int(id)).first()
    if obj:
        if request.method == 'POST':
            form_data = request.form
            obj.name = form_data['name']
            obj.gender = form_data['gender']
            obj.address = form_data['address']
            obj.phone = form_data['phone']
            obj.salary = form_data['salary']
            obj.department = form_data['department']

            try:
                db.session.commit()
                return redirect('/')
            except Exception:
                return 'There was an error'
        else:
            return render_template('edit.html', emp=obj)
    else:
        return render_template('edit.html',
                               error='Sorry, the employee does not exist.')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

