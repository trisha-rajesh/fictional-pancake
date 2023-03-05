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

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Voter Form Submission</title>")
print("</head>")
print("<body>")
print("<h1>Thank you for submitting your voter form!</h1>")
print("<p>Name: " + str(name) + "</p>")
print("<p>Age: " + str(age) + "</p>")
print("<p>Gender: " + str(gender) + "</p>")
print("<p>City: " + str(city) + "</p>")
print("<p>Candidates:")
for candidate in candidates:
    print("<br>" + str(candidate))
print("</p>")
print("</body>")
print("</html>")