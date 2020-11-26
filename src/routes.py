from src import src
from flask import render_template, redirect
from src.forms import ContactForm
from src.email import send_message

@src.route('/', methods=['GET', 'POST'])
@src.route('/index', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        phone = form.phone.data
        send_message(email, name, message, phone)
        return redirect('/index')
    return render_template('index.html', form=form)