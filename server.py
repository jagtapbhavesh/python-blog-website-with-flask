from flask import Flask, render_template, flash, redirect , url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '298393783ce3827bs2463t383v283934'

posts = [
    {
    'author':'Bhavesh Jagtap',
    'title':'Blog post 1',
    'content':'First blog post',
    'date_posted' : "april 20, 2018"
    },
    {
    'author':'Raj khan',
    'title':'Blog post 2',
    'content':'Second blog post',
    'date_posted' : "april 21, 2018"
    }
]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts= posts)
@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register',form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login',form=form)

if __name__ == "__main__":
    app.run(debug=True)
