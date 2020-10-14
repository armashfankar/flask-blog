from flask import Flask, render_template, url_for, flash, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fc8c93515b9f7b4243dcca90637b3d45'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


posts = [
    {
        'author': 'Armash Fankar',
        'title' : 'How to create flask application?',
        'content': 'In this Python Flask Tutorial, we will be learning how to use templates. Templates allow us to reuse sections of code over multiple routes and are great for serving up dynamic HTML pages.',
        'date_posted': 'October 10, 2020' 
    },
    {
        'author': 'Saima Fankar',
        'title' : 'How to create python application?',
        'content': 'In this Python Flask Tutorial, we will be learning how to use templates. Templates allow us to reuse sections of code over multiple routes and are great for serving up dynamic HTML pages.',
        'date_posted': 'October 09, 2020' 
    }
]

about = 'Welcome to [store name], your number one source for all things [product, ie: shoes, bags, dog treats]. We\'re dedicated to giving you the very best of [product], with a focus on [three characteristics, ie: dependability, customer service and uniqueness.] Founded in [year] by [founder\'s name], [store name] has come a long way from its beginnings in a [starting location, ie: home office, toolshed, Houston, TX.]. When [store founder] first started out, his/her passion for [passion of founder, ie: helping other parents be more eco-friendly, providing the best equipment for his fellow musicians] drove him to [action, ie: do intense research, quit her day job], and gave him the impetus to turn hard work and inspiration into to a booming online store. We now serve customers all over [place, ie: the US, the world, the Austin area], and are thrilled to be a part of the [adjective, ie: quirky, eco-friendly, fair trade] wing of the [industry type, ie: fashion, baked goods, watches] industry.<br>We hope you enjoy our products as much as we enjoy offering them to you. If you have any questions or comments, please don\'t hesitate to contact us.'


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about-us')
def about_us():
    return render_template('about.html', title='About', about=about)

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'asdasdasd':
            flash('Login Succesfull!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Failed!', 'danger')

    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)