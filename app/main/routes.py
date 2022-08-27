from app import db
from app.main import bp
from flask import request, redirect, url_for, flash, render_template, current_app
from flask_login import current_user, login_required
from app.main.forms import ProfileForm
from app.models import Profile, Users
import utils


@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
    page = request.args.get('page', 1, type=int)
    dossier = Users.query.order_by(Users.email.desc()).paginate(
        page, current_app.config['DOSSIER_PER_PAGE'], False)
    next_url = url_for('main.index', page=dossier.next_num) \
        if dossier.has_next else None
    prev_url = url_for('main.index', page=dossier.prev_num) \
        if dossier.has_prev else None
    return render_template('index.html', title='Home', posts=dossier.items,
                           next_url=next_url, prev_url=prev_url)


@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    data = Profile.query.filter_by(user_id=id).first_or_404()
    age = utils.get_age(data.birthday)
    form = ProfileForm()
    if form.validate_on_submit():
        data.city = form.city.data
        data.education = form.education.data
        data.mastery = form.mastery.data
        data.skill = form.skill.data
        data.birthday = form.birthday.data
        data.contact = form.contact.data
        db.session.commit()
        flash('Ваши данные отредоктированны')
        return render_template('userv.html', user=data, form=form, age=age)
    return render_template('user.html', user=user, form=form, data=data, id=id)


@bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    check_exist = Profile.query.filter_by(user_id=current_user.id).first()
    if check_exist:
        return redirect(url_for('main.edit', id=current_user.id))
    form = ProfileForm()
    if form.validate_on_submit():
        profile = Profile(
            city=form.city.data,
            education=form.education.data,
            mastery=form.mastery.data,
            skill=form.skill.data,
            birthday=form.birthday.data,
            contact=form.contact.data,
            specialist=current_user)
        db.session.add(profile)
        db.session.commit()
        flash('Анкета успешно заполнена')
        return redirect(url_for('main.index'))
    return render_template('profile.html', form=form)


@bp.route('/user/<id>', methods=['GET', 'POST'])
def user(id):
    data = Profile.query.filter_by(user_id=id).first_or_404()
    age = utils.get_age(data.birthday)
    return render_template('userv.html', user=data, age=age)