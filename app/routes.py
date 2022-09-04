from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/update') 
def get_ses(): 
 	return redirect(url_for('olxShowing'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('update'))
    return render_template('login.html',  title='Sign In', form=form)

