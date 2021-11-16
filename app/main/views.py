from flask import render_template, redirect, request, flash
from flask_login import login_required, current_user
from . import main
from .. import db
from ..models import Listing
from .forms import BioForm, ListForm


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/find')
def find():
    return render_template('find.html')

@main.route('/user', methods=['GET', 'POST'])
@login_required
def user():

    bioform = BioForm()
    if request.method == 'GET':
        bioform.username.data = current_user.username
        if current_user.bio is None or bool(current_user.bio) is False:
            bioform.bio.description = 'Type your personal bio here'
        else:
            bioform.bio.data = current_user.bio

        if current_user.country is None or bool(current_user.country) is False:
            bioform.country.description = 'Input country if you wish'
        else:
            bioform.country.data = current_user.country

        if current_user.city is None or bool(current_user.city) is False:
            bioform.city.description = 'Input city if you wish'
        else:
            bioform.city.data = current_user.city
    if bioform.validate_on_submit():
        if bioform.username is not None:
            current_user.username = bioform.username.data
            current_user.bio = bioform.bio.data
            current_user.country = bioform.country.data
            current_user.city = bioform.city.data
            db.session.add(current_user)
            db.session.commit()
            return redirect('user')
        flash('Username must be stated.')

    listform = ListForm()
    if listform.validate_on_submit():
        new_listing = Listing()
        new_listing.user_id = current_user.id
        new_listing.header = listform.header.data
        new_listing.game = listform.game.data
        new_listing.platform = listform.platform.data
        new_listing.info = listform.info.data
        db.session.add(new_listing)
        db.session.commit()
        return redirect('user')

    listings = Listing.query.filter_by(user_id=current_user.id).all()

    return render_template('user.html', bioform=bioform, listform=listform, listings=listings)


@main.route('/modify', methods=['GET', 'POST'])
@login_required
def modify():
    listform = ListForm()
    if current_user.id == int(request.args['user']):
        listing_id = request.args['listing']
        modify = Listing.query.filter_by(id = listing_id).first()
        if request.method == 'GET':
            listform.id.data = modify.id
            listform.header.data = modify.header
            listform.game.data = modify.game
            listform.platform.data = modify.platform
            listform.info.data = modify.info
        if listform.validate_on_submit():
            modify.id = listform.id.data
            modify.header = listform.header.data
            modify.game = listform.game.data
            modify.platform = listform.platform.data
            modify.info = listform.info.data
            db.session.commit()
            return redirect('user')
    else:
        return redirect('user')
    return render_template('modify.html', listform=listform)

@main.route('/delete')
@login_required
def delete():
    if current_user.id == int(request.args['user']):
        listing_id = request.args['listing']
        delete = Listing.query.filter_by(id = listing_id).first()
        db.session.delete(delete)
        db.session.commit()
    return redirect('user')

@main.route('/admin')
@login_required
def admin():
    return render_template('admin.html')