from flask import render_template, Blueprint, request, redirect, Response, jsonify

from models import db, Contact
contacts_bp = Blueprint('contacts', __name__, template_folder='templates')


@contacts_bp.route('/contacts')
def view_all_contacts():
    contacts = Contact.query.all()
    return render_template('contacts/list.html', **{"contacts": contacts})


@contacts_bp.post('/api/contacts')
def add_contacts():
    contact = Contact()
    contact.name = request.form["name"]
    contact.phone = request.form["phone"]
    db.session.add(contact)
    db.session.commit()
    return redirect('/contacts')


@contacts_bp.delete('/api/contacts/<int:contact_id>')
def delete_contacts(contact_id):
    contact = Contact.query.filter_by(id=contact_id).first()
    db.session.delete(contact)
    db.session.commit()
    return jsonify({})
