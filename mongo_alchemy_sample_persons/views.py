from flask import Blueprint, jsonify, request

from mongo_alchemy_sample_persons.forms import PersonForm
from mongo_alchemy_sample_persons.models import Person
from mongo_alchemy_sample_util.constants import HTTPMethod, Pagination, URLPrefix
from mongo_alchemy_sample_util.exceptions import BadRequest

blueprint = Blueprint('persons', __name__, url_prefix=URLPrefix.PERSONS)


@blueprint.route('', methods=[HTTPMethod.POST])
def save_person():
    form = PersonForm()
    if form.validate():
        person = form.save()
        return jsonify(person.to_json())
    raise BadRequest(form)


@blueprint.route('/<mongo_id>')
def view_person(mongo_id):
    person = Person.query.get_or_404(mongo_id)
    return jsonify(person.to_json())


@blueprint.route('/<mongo_id>', methods=[HTTPMethod.PUT])
def update_person(mongo_id):
    person = Person.query.get_or_404(mongo_id)
    form = PersonForm()
    if form.validate():
        form.instance = person
        person = form.save()
        return jsonify(person.to_json())
    raise BadRequest(form)


@blueprint.route('/<mongo_id>', methods=[HTTPMethod.DELETE])
def delete_person(mongo_id):
    person = Person.query.get_or_404(mongo_id)
    person.remove()
    return jsonify(person.to_json())


@blueprint.route('')
def list_persons():
    page = int(request.args[Pagination.PAGE]) if Pagination.PAGE in request.args else 1
    size = int(request.args[Pagination.SIZE]) if Pagination.SIZE in request.args else 10

    return jsonify([person.to_json() for person in Person.query.paginate(page=page, per_page=size).items])
