#!/usr/bin/env python
import cgi

# Get the form data
form = cgi.FieldStorage()

# Get the name, age, gender, and city values from the form
name = form.getvalue('name')
age = form.getvalue('age')
gender = form.getvalue('gender')
city = form.getvalue('city')

# Get the candidate values from the form as a list
candidates = form.getlist('candidates')
