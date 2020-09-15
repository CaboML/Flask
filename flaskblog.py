#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 11:29:34 2019

@author: tiagocabo
"""

# need to create an virtualenvironment


from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__) # create app variable
app.config['SECRET_KEY'] = '3e6ed80862da4fdd3f01114bb8a9de9e'


# dictionaries to be upload to the blog
# emulates a database call
posts = [
            {
               'author': 'Tiago Cabo',
               'title': 'My first blog post',
               'content':'First attempt to add content',
                'date_posted': 'January 21, 2019'
                },
                    {'author': 'Patricia Carneiro',
               'title': 'Second blog post',
               'content':'Second attempt to add content',
                'date_posted': 'January 19, 2019'
                            }
        ]


@app.route('/') 
@app.route('/home')   #renders backend. route page of our website. slash mean homepage
# this kind of call are called decorators. 
def home():
    return render_template('home.html', posts= posts)


@app.route('/about')   #renders backend. route page of our website. slash mean homepage
# this kind of call are called decorators. 
def about():
    return render_template('about.html', title="New About Page")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
    
    
    