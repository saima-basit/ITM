from flask import Flask, render_template, jsonify, request, redirect

from models import db, Contact
from settings import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
db.init_app(app)
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('contacts/list.html', **{"contacts": contacts})


@app.route('/add_contact')
def view_add_contacts():
    return render_template('contacts/add.html')


@app.post('/api/contacts')
def add_contacts():
    contact = Contact()
    contact.name = request.form["name"]
    contact.phone = request.form["phone"]
    db.session.add(contact)
    db.session.commit()
    return redirect('/')


@app.delete('/api/contacts/<int:contact_id>')
def delete_contacts(contact_id):
    contact = Contact.query.filter_by(id=contact_id).first()
    db.session.delete(contact)
    db.session.commit()
    return jsonify({})


if __name__ == '__main__':
    app.run(debug=False, port=1111, host="0.0.0.0")
