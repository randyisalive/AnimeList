from flask import Flask, render_template, redirect, request, session
from flask_debugtoolbar import DebugToolbarExtension
from controller.authentication import *
from controller.home import *
from controller.article import *
from controller.super_user import *
from controller.forum import *

from flask import send_from_directory
import os

UPLOAD_FOLDER = './user_profile'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = '1'
app.debug = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


toolbar = DebugToolbarExtension(app)

app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(home, url_prefix='/')
app.register_blueprint(article, url_prefix='/article')
app.register_blueprint(super_user, url_prefix='/admin')
app.register_blueprint(forum, url_prefix='/forum')




if __name__ == '__main__':
    app.run()