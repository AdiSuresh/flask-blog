from flask import render_template, flash, url_for, redirect
from flaskblog.forms import RegistrationForm, LoginForm
# from flaskblog.models import User, Post
from flaskblog import app

posts = [
    {
        'author': 'Peter Parker',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'April 20th, 2018'
    },
    {
        'author': 'Mary Jane',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'April 21th, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts, title='Home')


@app.route("/about")
def about():
    return render_template("about.html", title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    else:
        print("\n!!!ERROR!!!\nNot able to register\n")
    return render_template(
        'register.html', title='Register to write blogs', form=form
    )


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        cond_1 = (form.email.data == 'admin@blog.com')
        cond_2 = (form.password.data == 'password')
        if cond_1 and cond_2:
            flash('Login was successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash(
                'Login unsuccessful. Please check username and password',
                'danger'
            )
    return render_template('login.html', title='Login', form=form)
