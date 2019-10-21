# -*- coding: utf-8 -*-
"""
Onyx Project
https://onyxlabs.fr
Software under licence Creative Commons 3.0 France
http://creativecommons.org/licenses/by-nc-sa/3.0/fr/
You may not use this software for commercial purposes.
"""

from boilerplate_skill.index import boilerplate
from flask_login import login_required
from flask import render_template

from boilerplate_skill.api import *


@boilerplate.route('/' , methods=['GET','POST'])
@login_required
def index():
    return render_template('boilerplate/index.html')

@boilerplate.route('/config' , methods=['GET','POST'])
@login_required
def config():
    return render_template('boilerplate/config.html')

@boilerplate.route('/widget')
@login_required
def widget():
    return render_template('boilerplate/widget.html')
