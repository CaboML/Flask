#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 11:29:34 2019

@author: tiagocabo
"""

# need to create an virtualenvironment


from flask import Flask, render_template, url_for
app = Flask(__name__) # create app variable


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

# need to make cs code directory
# run: export FLASK_APP=flaskblog.py
# then run flask run
    
# the ip adress is http://127.0.0.1:5000
# or http://localhost:5000

#debug mode allows the weppage to refresh every change and update
    
# USE: export FLASK_DEBUG=1
    
## TO have the debug mode
    


@app.route('/about')   #renders backend. route page of our website. slash mean homepage
# this kind of call are called decorators. 
def about():
    return render_template('about.html', title="New About Page")


if __name__ == '__main__':
    app.run(debug=True)
    
    
    