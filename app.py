from flask import Flask, render_template, request, redirect, flask

from  flask_mail import Mail, Message 

app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USER_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'Your-email'
app.config['MAIL_PASSWORD'] = ' Ýour-email pass'
app.config['MAIL_DEFAULT_SENDER'] = 'Your-email'


mail = Mail(App)