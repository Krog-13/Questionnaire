from app import db
from app.auth import bp
from flask import redirect, url_for, flash, render_template
from flask_login import login_user, logout_user, current_user, login_required
from app.auth.forms import LoginForm, RegisterForm
from app.models import Users


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        email = Users.query.filter_by(email=form.email.data).first()
        if email is None or not email.check_password(form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('auth.login'))
        login_user(email, remember=form.remember_me)
        return redirect(url_for('main.index'))
    return render_template('auth/login.html', title='Sing in', form=form)


# registration route
@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = Users(fullname=form.fullname.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations you are now a registered user!')
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', title='Register', form=form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))