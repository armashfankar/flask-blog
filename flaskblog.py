from flask import Flask, render_template, url_for

app = Flask(__name__)

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

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about_us():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)