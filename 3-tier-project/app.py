from flask import Flask, render_template, jsonify, request, redirect

from contacts_api import contacts_bp
from models import db
from settings import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(contacts_bp)

# Dummy data for demonstration
data_from_database = {"message": "Hello from the database!"}
contacts = [
    {
        "name": "basit",
        "phone": "03****02333"
    },
    {
        "name": "arham",
        "phone": "0332****333"
    }
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/data')
def get_data():
    return jsonify(data_from_database)


@app.route('/add_contact')
def view_add_contacts():
    return render_template('contacts/add.html')


@app.get('/api/contacts')
def get_all_contacts():
    return jsonify({"contacts": contacts})



@app.post('/api/contacts/search')
def search_contacts():
    input_ = request.form["name"]
    print(input_)
    return redirect('/contacts')


@app.route('/search')
def view_search_contacts():
    return render_template('contacts/search.html')


if __name__ == '__main__':
    app.run(debug=True, port=1234)
