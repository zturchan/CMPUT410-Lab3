#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()
name=form.getvalue("name")
family=form.getvalue("family")
cs="liked" if form.getvalue("cs") else "disliked"
print "Content-type:text/html"
print
print '<style type="text/css">form { background-color: blue}</style>'
print 'Form 2<br/>'
print 'Name is'
print name
print '<br/>family is'
print family
print '<br/>cs is'
print cs
print '<br/><form method="post" action="form1.py">'
print '<textarea name="birthday" cols="40" rows="1" placeholder="birthday">'
print '</textarea>'
print '<textarea name="hobby" cols="40" rows="1" placeholder ="hobby">'
print '</textarea>'
print '<input type="checkbox" name="bacon">Is bacon awesome</input>'
print '<br/>'
print '<input type="submit" value="Submit">'
print '</form>'

