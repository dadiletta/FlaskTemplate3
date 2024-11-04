"""
WELCOME
"""
from flask import render_template

# our objects
from . import views


######################
#### STATIC PAGES ####
######################
# Displays the home page.
@views.route('/')
@views.route('/index')
@views.route('/index.html')
# Users must be authenticated to view the home page, but they don't have to have any particular role.
# Flask-Security will display a login form if the user isn't already authenticated.
def index():
    return render_template('pages/index.html')


@views.get('/home-bakery')
def home_bakery():
    return render_template('pages/home-bakery.html')

# If you want to add a new page, you can do so by adding a new route and a new function.
# For example, to add a page at /about, you could add the following code:
#   
# @views.route('/about')
# def about():
#     return render_template('pages/about.html')