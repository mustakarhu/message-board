# Import necessary libraries to make a web app.
from flask import Flask, redirect, url_for, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import json

# Import the functions from <func.py>. You will mainly work on these functions
from func import read, write, checkLen

# Instantiate a Flask object
app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'


# Create a form class using FlaskForm. The form has 2 input fields <name, message> and a submit button
class InputForm(FlaskForm):
    name = StringField('Name :', [DataRequired()]) # DataRequired is a function that forces the form to be filled
    message = StringField('Message:', [DataRequired()])

    post = SubmitField('Post')


# This is the function that will run when you go to index.html
@app.route('/', methods=('GET', 'POST')) # This is the syntax to make a decorator. Google if you want to learn more
def index():
    ""
    ''' We store guest messages in a json file.
    First we open it to load the data.
    Then we pass the data to the read() function to transform it into the (<name>, <date>, <message>) format.
    The transformed data will become a list containing the rows with the format above.
    Finally we can pass the list to render_template() to display the messages when we visit index.html.
    '''
    with open('data.json', 'r') as file:
        data = json.load(file)
        rows = read(data)
        num_messages_to_show = checkLen(rows) # We also want to check how many messages are in the data

    # Here we instantiate a form object
    form = InputForm()

    ''' If the user enters valid inputs and presses Post, the code block below will run.
    We retrieve the user's name and message and store them in name and message.
    Then we update the rows list to add the received message and return it.
    Finally we can update the data json file using json.dump().    
    '''
    if form.validate_on_submit():
        name = form.name.data
        message = form.message.data

        data = write(rows, name, message)
        with open('data.json', 'w') as file:
            json.dump(data, file)

        return redirect(url_for('index')) # We also want to refresh the index page to show the change

    # In the render_template, you can pass the variables to be used in the html file. This is to connect the back-end to the front-end
    return render_template('index.html', rows=rows, num_messages_to_show=num_messages_to_show, form=form)


# This code will tell the Flask object "app" to run when you start the program
if __name__ == "__main__":
    app.run()
