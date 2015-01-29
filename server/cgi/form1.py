#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()
birthday=form.getvalue("birthday")
hobby=form.getvalue("hobby")
#bacon = form.getvalue("bacon")
bacon="liked" if form.getvalue("bacon") else "disliked"
print "Content-type:text/html"
print
print '<style type="text/css">form { background-color: red}</style>'
print 'Form 1<br/>'
print 'Hobby is'
print hobby
print '<br/>birthday is'
print birthday
print '<br/>Bacon is'
print bacon
print '<br/><form method="post" action="form2.py">'
print '<textarea name="name" cols="40" rows="1" placeholder="name">'
print '</textarea>'
print '<textarea name="family" cols="40" rows="1" placeholder ="family">'
print '</textarea>'
print '<input type="checkbox" name="cs">I love CS</input>'
print '<br/>'
print '<input type="submit" value="Submit">'
print '</form>'

